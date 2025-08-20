let selectedFiles = [];
let deletedImages = [];

document.addEventListener('DOMContentLoaded', function() {
    setupImagePreview();
    setupExistingImages();
});

function setupImagePreview() {
    const imagesField = document.querySelector('#div_id_images');
    if (!imagesField) return;

    const uploadHTML = `
        <div class="mb-3">
            <label class="form-label"></label>
            <div class="file-input-wrapper" onclick="document.getElementById('id_images').click()">
                <div class="upload-text">
                    <div class="upload-icon"><i class="fa-solid fa-upload"></i></div>
                    Yangi rasm(lar) qo'shish uchun bosing
                </div>
            </div>
            <div id="image-preview-container" class="image-preview-container"></div>
        </div>
    `;

    imagesField.insertAdjacentHTML('beforebegin', uploadHTML);
    imagesField.style.display = 'none';

    const imageInput = document.getElementById('id_images');
    if (imageInput) {
        imageInput.addEventListener('change', function(e) {
            const files = Array.from(e.target.files);
            
            files.forEach(file => {
                if (file.type.startsWith('image/')) {
                    selectedFiles.push(file);
                }
            });
            
            updateImagePreview();
        });
    }
}

function setupExistingImages() {
    const existingImagesContainer = document.getElementById('existing-images-container');
    if (!existingImagesContainer) return;

    // Mavjud rasmlarni ko'rsatish
    const existingImages = existingImagesContainer.querySelectorAll('.existing-image');
    existingImages.forEach(imageDiv => {
        const removeBtn = imageDiv.querySelector('.remove-existing-image');
        if (removeBtn) {
            removeBtn.addEventListener('click', function() {
                const imageId = this.dataset.imageId;
                deletedImages.push(imageId);
                imageDiv.style.display = 'none';
                updateDeletedImagesInput();
            });
        }
    });
}

function updateImagePreview() {
    const container = document.getElementById('image-preview-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    selectedFiles.forEach((file, index) => {
        const reader = new FileReader();
        reader.onload = function(e) {
            const previewDiv = document.createElement('div');
            previewDiv.className = 'image-preview';
            previewDiv.innerHTML = `
                <img src="${e.target.result}" alt="Preview">
                <button type="button" class="remove-image" onclick="removeNewImage(${index})">×</button>
            `;
            container.appendChild(previewDiv);
        };
        reader.readAsDataURL(file);
    });
    
    updateFileInput();
}

function removeNewImage(index) {
    selectedFiles.splice(index, 1);
    updateImagePreview();
}

function updateFileInput() {
    const dt = new DataTransfer();
    selectedFiles.forEach(file => {
        dt.items.add(file);
    });
    
    const input = document.getElementById('id_images');
    if (input) {
        input.files = dt.files;
    }
}

function updateDeletedImagesInput() {
    let input = document.querySelector('input[name="deleted_images"]');
    if (!input) {
        input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'deleted_images';
        document.querySelector('form').appendChild(input);
    }
    input.value = deletedImages.join(',');
}