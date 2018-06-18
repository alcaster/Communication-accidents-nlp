
var map = L.map('map').setView([52.22977, 21.01178], 15);

mapLink = '<a href="{http://openstreetmap.org}">OpenStreetMap</a>'


L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
            }).addTo(map);

/*var polygon = L.polygon([
    [52.23112, 21.01017],
    [52.22827, 21.01532],
    [52.22931, 21.00762]
]).addTo(map);*/

//var popup = L.popup();

function MyClick(e) {
    
    var r = document.getElementById("radius").value;
    var corner1 = L.latLng(52.23006, 21.00195);
    var circle = L.circle(corner1, r, {color: "#f03", fillColor: "#f03", fillOpacity: 0.5}).addTo(map);
    /*popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
    circle
        .setLatLng(e.latlng)    
        .openOn(map);*/
}
