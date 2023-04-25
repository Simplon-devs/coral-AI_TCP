import logging
import logging.handlers
from flask import Flask, render_template, abort, request, redirect, url_for, session
from jinja2 import TemplateNotFound
import hashlib
import interfaces
import mysql as mysql
import mysql.connector
from entity.User import User


class Server(interfaces.Server_interface):

    def __init__(self,
                 logfile="log.txt"):
        
        self.__app = None
        self.__logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler(logfile,
                                                  maxBytes=1000000, 
                                                  backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s'))
        self.__logger.addHandler(fh)
        self.__logger.setLevel('DEBUG')
        logging.root.handlers = [fh]
        self.connected_user = None
        

    @property
    def app(self):
        if self.__app: return self.__app
        else: return self.__create_app

    
    @app.setter
    def app(self,
            new_value):
        
        raise AttributeError("You can't change the app object from outside of the class")

    def __create_app(self):
        """Create and returns a new Flask app"""

        self.__logger.debug("Creating app object")
        self.__app = Flask("The Coral Planters", template_folder='./templates', static_folder='./static')
        self.__app.config['SECRET_KEY'] = 'secret_key'
        self.__app.config['SESSION_TYPE'] = 'filesystem'

        self.__logger.debug("App object created")

        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/sign_in", "sign in", self.sign_in, methods=["GET", "POST"])
        self.app.add_url_rule("/sign_up", "sign up", self.sign_up)
        self.app.add_url_rule("/logout", "logout", self.logout)
        self.app.add_url_rule("/upload", "upload", self.upload)
        self.app.add_url_rule("/coral_info", "Show coral info", self.coral_info)
        self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="reefscapers2020_v3"
        )
        self.cursor = self.conn.cursor()
        return self.__app

    def run_test_server(self):
        """Runs the Flask app. For testing purpose only, don't use
        that in production"""

        if not self.__app: self.__app = self.__create_app()
        
        self.__logger.info("Running server in debug mode...")
        self.__app.run(debug=True, threaded=True)
    

    #########################################################################
    # ROUTING FUNCTIONS
    #########################################################################

    def index(self):

        """This method is called when a request is sent to the homepage"""
        try:

            user_images = []
            public_images = []
            import copy
            from base64 import b64encode
            from PIL import Image

            ##############################################################
            # CODE BELOW FOR TESTING PURPOSES ONLY, WILL BE REPLACED WITH
            # ACTUAL IMAGES
            ##############################################################
            img = Image.open("static/assets/photo_test.jpeg")
            img = img.resize((300, 300))
            img.save("static/assets/photo_test.jpg")

            
            with open("static/assets/photo_test.jpg", 'rb') as image:
                content = b64encode(image.read()).decode("utf-8")

            for i in range(20):
                user_images.append(copy.copy(content)) 
                public_images.append(copy.copy(content))
            
            if len(public_images) > 12: display_btn = True
            else: display_btn = False

            return render_template("index.html", 
                                   user_corals=user_images,
                                   public_corals=public_images,
                                   display_btn=display_btn)

        except TemplateNotFound:

            abort(404)
    
    def sign_in(self):

        self.__logger.info("Running server in debug mode...")

        if request.method == 'POST':
            # Do something with the submitted form data
            username = request.form['username']
            password = request.form['password']
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print("username : ", username, " password : ", hashed_password)
            try:
                sql_query = "SELECT id, username, role, email, fragment_id FROM utilisateurs WHERE username = %s AND password = %s"
                params = (username, hashed_password)
                self.cursor.execute(sql_query, params)
                res = self.cursor.fetchall()
                self.connected_user = User(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4])
                session['logged_in'] = True

                print(self.connected_user)
                self.conn.close()

                return redirect('/')
            except:
                return redirect('/sign_in')
        elif request.method == 'GET':
            try:
                
                return render_template("sign_in.html")
            except TemplateNotFound:
                abort(404)



    def sign_up(self):
        """TO BE MODIFIED TO HANDLE BOTH POST AND GET REQUESTS"""
        try:
            return render_template("sign_up.html")
        except TemplateNotFound:
            abort(404)

    def upload(self):
        """TO BE MODIFIED TO HANDLE BOTH POST AND GET REQUESTS"""
        try:
            return render_template("upload.html")
        except TemplateNotFound:
            abort(404)


    def coral_info(self):
        """
        Displays a page showing all information about a coral fragment.
        The page displays the following information:
        - four pictures showing all sides of the structure hosting
        the corals
        - A bounding box on all pictures showing where the coral is located
        on the structure
        - The structure identifier
        - The coral's status (species, bleached or dead)
        """

        try:
            return render_template("coral_info.html")
        except TemplateNotFound:
            abort(404)
    
    def logout(self):
        self.connected_user = None
        session['logged_in'] = None
        return redirect('/')
    
