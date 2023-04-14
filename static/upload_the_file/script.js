var file = document.getElementById('file');
file.onchange = function(e) {
    var ext = this.value.match(/\.([^\.]+)$/)[1];
    switch (ext) {
        case 'doc':
        case 'docx':
        case 'txt':
        case 'rtf':
            break;
        default:
            this.value = '';
    }
};