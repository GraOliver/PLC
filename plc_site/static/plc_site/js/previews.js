document.addEventListener('DOMContentLoaded', function() {
    const inputImage = document.getElementById('id_image');
    const preview   = document.getElementById('preview-image');

    inputImage.addEventListener('change', function() {
      const file = this.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        preview.src = e.target.result;
      };
      reader.readAsDataURL(file);
    });
  });

  inputPhotos.addEventListener('change', function() {
    const previewContainer = document.getElementById('preview-container');
    previewContainer.innerHTML = '';  // vide le conteneur
  
    Array.from(this.files).forEach(file => {
      const reader = new FileReader();
      reader.onload = e => {
        const img = document.createElement('img');
        img.src = e.target.result;
        img.style.maxWidth = '200px';
        img.style.margin = '0.5rem';
        img.style.borderRadius = '4px';
        previewContainer.appendChild(img);
      };
      reader.readAsDataURL(file);
    });
  });
  
