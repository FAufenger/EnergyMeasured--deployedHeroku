/* data retrival route */
var urlStatePercent ="/api/data1";

function createMap(statePercentMarker) {

  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      tileSize: 512,
      zoomOffset: -1,
      maxZoom: 18,
      id: "light-v10",
      accessToken: API_KEY
  });
  var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      tileSize: 512,
      zoomOffset: -1,
      maxZoom: 18,
      id: "dark-v10",
      accessToken: API_KEY
  });
  var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: "mapbox/streets-v11",
      accessToken: API_KEY
  });
  var satellitenmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "satellite-v9",
    accessToken: API_KEY
  });
  
    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
      "Light Map": lightmap,
      "Dark Map": darkmap,
      "Street Map": streetmap,
      "Satellite Map": satellitenmap
  };

  // Create an overlayMaps object to hold the bikeStations layer
  var overlayMaps = {
       "US Energy Consumption per State": statePercentMarker
      // "Title2": Can add values in from createmap()
  };

  // Create the map object with options
  var map = L.map("map-id", {
    center: [37.09, -95.71],
    zoom: 3,
    layers: [lightmap]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}



function createMarkers(response) {

  // var data1 = response.element_in_data1;

  // Initialize an array to hold earthquake markers
  var marker1 = [];
  // var magnitude = [];

  // Loop through the stations array
  for (var index = 0; index < response.length; index++) {
      var element_in_data1 = response[index];
      
      // For each latitude and longitude, create a marker and bind a popup with the data
      var someMark = L.marker(element_in_data1.slice(11, 13))
          .bindPopup("<h5>Energy usage for :<b></h5><h5>"+ element_in_data1[0] +"</b></h5><hr><h5>Nuclear: " + element_in_data1[1] + "%</h5><h5>Coal: "+  element_in_data1[2] + "%</h5>" +
                    "<h5>Naturel Gas: " + element_in_data1[3] + "%</h5><h5>Petroleum: " + element_in_data1[4] + "%</h5><h5>Hydro: "+  element_in_data1[5] + "%</h5>" +
                    "<h5>Geothermal: " + element_in_data1[6] + "%</h5><h5>Solar: " + element_in_data1[7] + "%</h5><h5>Wind: "+  element_in_data1[8] + "%</h5>" +
                    "<h5>Biomass & Other: " + element_in_data1[9] + "%</h5>");

      // Add earthquarkmark to preset list
      marker1.push(someMark);
  };

  // Create a layer group made from the bike markers array, pass it into the createMap function
  createMap(L.layerGroup(marker1));
};


// Perform an API call to the EarthQuake API to get information. Call createMarkers when complete
d3.json(urlStatePercent, createMarkers);



///////////////////////////////////
//     Basic map test layout     //
///////////////////////////////////

// // Creating our initial map object
// // We set the longitude, latitude, and the starting zoom level
// // This gets inserted into the div with an id of 'map'
// var myMap = L.map("map-id", {
//   center: [37.09, -95.71],
//   zoom: 7
// });

// // Adding a tile layer (the background map image) to our map
// // We use the addTo method to add objects to our map
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: API_KEY
// }).addTo(myMap);
