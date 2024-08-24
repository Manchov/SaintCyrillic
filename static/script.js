let dropArea = document.getElementById('drop-area');
let asciiArt = document.getElementById('ascii-art');

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when item is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight(e) {
    dropArea.classList.add('highlight');
}

function unhighlight(e) {
    dropArea.classList.remove('highlight');
}

function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;

    handleFiles(files);
}

function handleFiles(files) {
    ([...files]).forEach(uploadFile);
}

function uploadFile(file) {
    let url = '/';
    let formData = new FormData();
    formData.append('file', file);
    formData.append('screen_width', window.innerWidth);
    formData.append('screen_height', window.innerHeight);

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        asciiArt.textContent = data;
        asciiArt.classList.remove('hidden');
        dropArea.classList.add('hidden');
        document.querySelector('.my-form').classList.add('hidden');
    })
    .catch(() => { console.error('Upload failed'); });
}

dropArea.addEventListener('click', () => {
    // Ensure only the file input is triggered, preventing multiple dialogs
    if (!document.getElementById('fileElem').clicked) {
        document.getElementById('fileElem').click();
        document.getElementById('fileElem').clicked = true;
    }
});

asciiArt.addEventListener('dragenter', preventDefaults, false);
asciiArt.addEventListener('dragover', preventDefaults, false);
asciiArt.addEventListener('dragleave', preventDefaults, false);
asciiArt.addEventListener('drop', handleDrop, false);
