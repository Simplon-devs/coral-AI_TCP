"use strict";


function seeMoreButtonClicked() {

    let img_to_reveal = 12;
    let images = document.getElementsByClassName('hidden_img');

    for (let i = 0; i < img_to_reveal; i++) {

        if (images.length == 0) {
            let btn = document.getElementsByClassName('btn-custom col-2');
            btn[0].style.display = 'none';
            break;
        }
        images[0].style.display = 'inline';
        images[0].classList.remove('hidden_img');
    }

}


function test_connection() {
    fetch('/test_connection', {
        method: 'GET',
    }).then(response => {
        response.json().then(data => {
            if (!data.connected) {
                fetch('/logout', {
                    method: 'GET',
                })

            }
        });
    });
}

window.addEventListener('load', () => {
    test_connection();
});
