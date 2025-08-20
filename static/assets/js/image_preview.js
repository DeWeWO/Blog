let selectedFiles = [];

document.addEventListener('DOMContentLoaded', function() {
    setupImagePreview();
});

function setupImagePreview() {
    // Images field-ni topamiz
    const imagesField = document.querySelector('#div_id_images');
    if (!imagesField) return;

    // Custom upload area yaratamiz
    const uploadHTML = `
        <div class="mb-3">
            <label class="form-label"></label>
            <div class="file-input-wrapper" onclick="document.getElementById('id_images').click()">
                <div class="upload-text">
                    <div class="upload-icon"><i class="fa-solid fa-upload"></i></div>
                    Rasm(lar) qo'shish uchun bosing
                </div>
            </div>
            <div id="image-preview-container" class="image-preview-container"></div>
        </div>
    `;

    // Yangi elementni qo'shamiz
    imagesField.insertAdjacentHTML('beforebegin', uploadHTML);
    
    // Original field-ni yashiramiz
    imagesField.style.display = 'none';

    // Input change event
    const imageInput = document.getElementById('id_images');
    if (imageInput) {
        imageInput.addEventListener('change', function(e) {
            const files = Array.from(e.target.files);
            
            selectedFiles = []; // Reset
            files.forEach(file => {
                if (file.type.startsWith('image/')) {
                    selectedFiles.push(file);
                }
            });
            
            updateImagePreview();
        });
    }
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
                <button type="button" class="remove-image" onclick="removeImage(${index})"><i class="fa-solid fa-circle-xmark fa-2xl" style="color: #9e9e9e;"></i></button>
            `;
            container.appendChild(previewDiv);
        };
        reader.readAsDataURL(file);
    });
    
    updateFileInput();
}

function removeImage(index) {
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