function IP_LOOKUP() {
    let IP_ADDR = document.getElementById("IP-ADDR").value;
    let IP_INFO = null;
    let data = {'IP': IP_ADDR};
    fetch('/api/geo_ip/', {
        method: 'POST',
        mode: 'same-origin', // no-cors, *cors, same-origin
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data), // Coordinate the body type with 'Content-Type'
    })
        .then(response => response.json())
        .then(data => save_data(data)) // Result from the `response.json()` call
        .catch(error => console.error(error));

    function save_data(data) {
        IP_INFO = data;
    }

}

function WEATHER() {
    let weather = null;
    fetch('/api/weather/')
        .then(response => response.json())
        .then(data => save_data(data)) // Result from the `response.json()` call
        .catch(error => console.error(error));

    function save_data(data) {
        weather = data;
        console.log(weather)
    }


}