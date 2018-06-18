document.addEventListener('DOMContentLoaded', function () {
    var map = L.map('mapid').setView([52.22977, 21.01178], 15);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiYWxjYXN0ZXIiLCJhIjoiY2ppZjJwMGd4MG96MTNwbzZ5ZXByenc4NyJ9.DU4_BDDy8X6SkkFD0p2Gsg'
    }).addTo(map);

    var circle = L.circle([52.22978, 21.01178], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
    }).addTo(map);

    $('#mainForm').submit(function (ev) {
        ev.preventDefault();
        $.get("api/get_data", {
            'fromDate': this.FromDate.value,
            'toDate': this.ToDate.value,
            'radius': this.Radius.value
        }, function (data) {
            alert(data.data)
        });
    });
}, false);
