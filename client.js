document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('ebookForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var title = document.getElementById('title').value;
        var topic = document.getElementById('topic').value;
        var audience = document.getElementById('audience').value;
        var chapters = document.getElementById('chapters').value;
        var subsections = document.getElementById('subsections').value;

        var ebookData = {
            title: title,
            topic: topic,
            audience: audience,
            chapters: chapters,
            subsections: subsections
        };

        console.log(ebookData);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/ebooks', true); 
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 201) {
                    console.log('Ebook data sent successfully');
                } else {
                    console.error('Failed to send ebook data');
                }
            }
        };
        xhr.send(JSON.stringify(ebookData));
    });
});

