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
        let City = JSON.stringify(data["City"]);
        let Continent = JSON.stringify(data["Continent"]);
        let Country = JSON.stringify(data["Country"]);
        let IP = JSON.stringify(data["IP"]);
        let ISP = JSON.stringify(data["ISP"]);
        let Mobile = JSON.stringify(data["Is a mobile device"]);
        let Latitude = JSON.stringify(data["Latitude"]);
        let Longitude = JSON.stringify(data["Longitude"]);
        let Region = JSON.stringify(data["Region Name"]);
        let DNS = JSON.stringify(data["Reverse DNS Lookup"]);
        let Time = JSON.stringify(data["Time Zone"]);
        let Zip = JSON.stringify(data["Zip"]);
        //document.getElementById('IP_INFO').style.display = 'none'
        window.alert(
            'City: ' + City.substring(1, City.length - 1) +
            '\nContinent: ' + Continent.substring(1, Continent.length - 1) +
            '\nCountry: ' + Country.substring(1, Country.length - 1) +
            '\nIP: ' + IP.substring(1, IP.length - 1) +
            '\nISP: ' + ISP.substring(1, ISP.length - 1) +
            '\nIs this a mobile device: ' + Mobile.substring(1, Mobile.length - 1) +
            '\nLatitude: ' + Latitude.substring(1, Latitude.length - 1) +
            '\nLongitude: ' + Longitude.substring(1, Longitude.length - 1) +
            '\nRegion: ' + Region.substring(1, Region.length - 1) +
            '\nReverse DNS: ' + DNS.substring(1, DNS.length - 1) +
            '\nTime Zone: ' + Time.substring(1, Time.length - 1) +
            '\nZip Code: ' + Zip.substring(1, Zip.length - 1)
        );
        /*document.getElementById('IP_City').innerHTML = 'City: ' + City.substring(1, City.length - 1);
        document.getElementById('IP_Continent').innerHTML = 'Continent: ' + Continent.substring(1, Continent.length - 1);
        document.getElementById('IP_Country').innerHTML = 'Country: ' + Country.substring(1, Country.length - 1);
        document.getElementById('IP_IP').innerHTML = 'IP: ' + IP.substring(1, IP.length - 1);
        document.getElementById('IP_ISP').innerHTML = 'ISP: ' + ISP.substring(1, ISP.length - 1);
        document.getElementById('IP_Mobile').innerHTML = 'Is this a mobile device: ' + Mobile.substring(1, Mobile.length - 1);
        document.getElementById('IP_Latitude').innerHTML = 'Latitude: ' + Latitude.substring(1, Latitude.length - 1);
        document.getElementById('IP_Longitude').innerHTML = 'Longitude: ' + Longitude.substring(1, Longitude.length - 1);
        document.getElementById('IP_Region').innerHTML = 'Region: ' + Region.substring(1, Region.length - 1);
        document.getElementById('IP_DNS').innerHTML = 'Reverse DNS: ' + DNS.substring(1, DNS.length - 1);
        document.getElementById('IP_Time').innerHTML = 'Time Zone: ' + Time.substring(1, Time.length - 1);
        document.getElementById('IP_Zip').innerHTML = 'Zip Code: ' + Zip.substring(1, Zip.length - 1);*/
    }

}

function WEATHER() {
    fetch('/api/weather/')
        .then(response => response.json())
        .then(data => save_data(data)) // Result from the `response.json()` call
        .catch(error => console.error(error));

    function save_data(data) {
        let today = JSON.stringify(data['0']['detailedForecast']);
        let tonight = JSON.stringify(data['1']['detailedForecast']);
        let tomorrow = JSON.stringify(data['2']['detailedForecast']);
        document.getElementById('Today').innerHTML = today.substring(1, today.length - 1);
        document.getElementById('Tonight').innerHTML = tonight.substring(1, tonight.length - 1);
        document.getElementById('Tomorrow').innerHTML = tomorrow.substring(1, tomorrow.length - 1);
    }


}


function NEWS() {
    fetch('/api/news/')
        .then(response => response.json())
        .then(data => save_data(data)) // Result from the `response.json()` call
        .catch(error => console.error(error));

    function save_data(data) {
        var ul = document.createElement('ul');
        document.getElementById('news').appendChild(ul);
        for (let count = 0; count < Object.keys(data).length-1; count++) {

            var li = document.createElement('li');
            ul.appendChild(li);
            /*let entry = "<p><img src=" + data[count]['Image URL'] +
                " width='66' height='66' align='left' style='padding: 3px'/></p>" +
                "<p><strong>Title</strong>: " +
                data[count]['Title'] +
                "<br><strong>Source</strong>: " +
                data[count]['Source'] + "</p>" +
                "<p>" + data[count]['Description'] + "   " +
                "<a href='" + data[count]['External URL'] + "'><br>Read More</a></p>"*/
            let entry =
                "<p><strong>Title</strong>: " +
                data[count]['Title'] +
                "<br><strong>Source</strong>: " +
                data[count]['Source'] + "</p>" +
                "<p>" + data[count]['Description'] + "   " +
                "<a href='" + data[count]['External URL'] + "'><br>Read More</a></p>"
            li.innerHTML += entry;
        }

    }


}

/*
'Title' + data[count]['Title'] +
                'Source' + data[count]['Source'] +
                data[count]['Description'] +
                " " + "<a href='" + data[count]['External URL'] + "'>Read More</a>";
 */


function QoD() {
    fetch('/api/quote/')
        .then(response => response.json())
        .then(data => save_data(data)) // Result from the `response.json()` call
        .catch(error => console.error(error));

    function save_data(data) {
        let author = JSON.stringify(data['Author']);
        let quote = JSON.stringify(data['Quote']);
        document.getElementById('QoD_Quote').innerHTML = quote.substring(1, quote.length - 1);
        document.getElementById('QoD_Author').innerHTML = "-" + author.substring(1, author.length - 1);
    }


}