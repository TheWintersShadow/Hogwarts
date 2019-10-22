let weather = null;

function IP_LOOKUP() {
    let IP_ADDR = document.getElementById("IP-ADDR").value;
    console.log(IP_ADDR);
    postRequest('/api/geo_ip/', {IP: '129.174.182.52'})
        .then(data => console.log(data)) // Result from the `response.json()` call
        .catch(error => console.error(error));

    function postRequest(url, data) {
        return fetch(url, {
            method: 'POST', // 'GET', 'PUT', 'DELETE', etc.
            body: JSON.stringify(data), // Coordinate the body type with 'Content-Type'
        })
            .then(response => response.json())
    }
}

function WEATHER() {
    fetch('/api/weather/')
        .then(response => response.json())
        .then(data => {
            console.log(data) // Prints result from `response.json()` in getRequest
        })
        .catch(error => console.error(error))
}