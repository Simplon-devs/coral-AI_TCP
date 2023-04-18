var dropZone = document.getElementById('drop-zone');

dropZone.addEventListener('dragover', function(e) {
  e.preventDefault();
  this.classList.add('dragover');
});

dropZone.addEventListener('dragleave', function(e) {
  e.preventDefault();
  this.classList.remove('dragover');
});

dropZone.addEventListener('drop', function(e) {
  e.preventDefault();
  this.classList.remove('dragover');

  var file = e.dataTransfer.files[0];
  var reader = new FileReader();

  reader.onload = function(event) {
    var image = new Image();
    image.src = event.target.result;
    dropZone.appendChild(image);
  }

  reader.readAsDataURL(file);
});

document.getElementById("add-img-btn").addEventListener("click", function() {
  document.getElementById("file-input").click();
});