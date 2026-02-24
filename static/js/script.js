function checkStatus() {
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('api-response').innerText = "API Response: " + JSON.stringify(data);
        });
}