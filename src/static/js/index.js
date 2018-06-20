document.addEventListener('DOMContentLoaded', function () {
    var map = L.map('mapid').setView([52.22977, 21.01178], 15);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiYWxjYXN0ZXIiLCJhIjoiY2ppZjJwMGd4MG96MTNwbzZ5ZXByenc4NyJ9.DU4_BDDy8X6SkkFD0p2Gsg'
    }).addTo(map);


    $('#mainForm').submit(function (ev) {
        ev.preventDefault();
        $.get("api/get_data", {
            'fromDate': this.FromDate.value,
            'toDate': this.ToDate.value,
            'radius': this.Radius.value
        }, function (data) {
            console.log(data.data);
            map.remove();
            map = L.map('mapid').setView([52.22977, 21.01178], 15);

            L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets',
                accessToken: 'pk.eyJ1IjoiYWxjYXN0ZXIiLCJhIjoiY2ppZjJwMGd4MG96MTNwbzZ5ZXByenc4NyJ9.DU4_BDDy8X6SkkFD0p2Gsg'
            }).addTo(map);

            var radius = document.getElementById("FormControlRadius").value;

            for(var i = 0; i < data.data.length; i++)
            {
                var x = data.data[i][0];
                var y = data.data[i][1];
                var delay = data.data[i][2];
                var color;

                if(delay == 0) color = "RoyalBlue";
                if(delay >= 1 && delay <= 15) color = 'green';
                if(delay >= 16 && delay <= 30) color = 'yellow';
                if(delay >= 31 && delay <= 60) color = 'DarkOrange';
                if(delay >= 61) color = 'red';

                var circle = L.circle([x, y], {
                            color: color,
                            fillColor: color,
                            fillOpacity: 0.5,
                            radius: radius,
                        }).addTo(map).bindPopup(delay.toString() + " sec");
            }
        });
    });


}, false);
