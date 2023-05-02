console.log("my_coral");  // outputs 'coral'

class User {

    constructor(id, username, role, email, register_date) {

        this.date = new Date(register_date);
        this.id = id;
        this.username = username;
        this.role = role;
        this.email = email;

        let options = { dateStyle: 'short' };
        this.register_date = this.date.toLocaleDateString(undefined, options);
    }
}
let user = null
fetch('/my_coral', {
    method: 'POST',
})
    .then(response => response.json())
    .then(data => {
        user = new User(data.id, data.username, data.role, data.email, data.register_date);
        update_user()
    });


function update_user() {


    usernameJS = document.querySelector('.usernameJS');
    emailJS = document.querySelector('.emailJS');
    register_dateJS = document.querySelector('.register_dateJS');
    usernameJS.innerHTML = user.username;
    emailJS.innerHTML = user.email;
    register_dateJS.innerHTML = user.register_date;
}


