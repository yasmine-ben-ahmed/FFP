window.onload = init ;
function init(){



    const mapElement = document.getElementById('mapid')
     var map = L.map(mapElement).setView([35, 9.5], 5);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);





    // FeatureGroup is to store editable layers
    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);
    var drawEditControl = new L.Control.Draw({
        draw: false,
        edit: {
            featureGroup: drawnItems
        }
    });
    var drawControl = new L.Control.Draw({
        edit: {
            featureGroup: drawnItems
        }
    });
    map.addControl(drawControl);

    
  
    map.on('draw:created', function (e) {
            layer = e.layer;
        const coordinates = layer.editing.latlngs[0][0]
        let polygon = [];
        coordinates.forEach((element) => {
            polygon.push(`${element.lng} ${element.lat}`);
        });
        polygon.push(`${coordinates[0].lng} ${coordinates[0].lat}`);
        polygonString = 'POLYGON (('+polygon.join(', ')+'))';
        document.getElementById('points').value=polygonString;
        drawnItems.addLayer(layer);
        drawControl.remove();
        drawEditControl.addTo(map);
    });


    

    map.on('draw:edited', function (e) {
        layer = e.layers;
        const coordinates = layer._layers[Object.keys(layer._layers)[0]]._latlngs[0];
        let polygon = [];
        coordinates.forEach((element) => {
            polygon.push(`${element.lng} ${element.lat}`);
        });
        polygon.push(`${coordinates[0].lng} ${coordinates[0].lat}`);
        polygonString = 'POLYGON (('+polygon.join(', ')+'))';
        document.getElementById('points').value=polygonString;
    });

    map.on('draw:deleted', function () {
        drawControl.addTo(map);
        drawEditControl.remove();
        document.getElementById('points').value='';
    });
  
}