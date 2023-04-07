import logging
import logging.handlers
from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

import interfaces


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
        self.__logger.debug("App object created")
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

            return render_template("index.html")

        except TemplateNotFound:

            abort(404)