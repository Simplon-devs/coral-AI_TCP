console.log("my_coral");  // outputs 'coral'

class User {
    constructor(id, username, role, email) {
        this.id = id;
        this.username = username;
        this.role = role;
        this.email = email;
    }
}

fetch('/my_coral', {
    method: 'POST',
})
    .then(response => response.json())
    .then(data => {
        const user = new User(data.id, data.username, data.role, data.email);
        update_user(user.username, user.email)
    });


function update_user(username, email) {


    usernameJS = document.querySelector('.usernameJS');
    emailJS = document.querySelector('.emailJS');
    usernameJS.innerHTML = username;
    emailJS.innerHTML = email;
}


