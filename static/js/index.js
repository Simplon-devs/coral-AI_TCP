"use strict";

function seeMoreButtonClicked() {
    
    let images = document.getElementsByClassName('hidden_img');
    let hidden_img_count = images.length;
    let img_to_reveal = 12;

    for (let i = 0; i < hidden_img_count; i++) {
        if (i < img_to_reveal) {
            images[i].style.display = 'inline';
        }
        else {
            break;
        }
      }
    


  }