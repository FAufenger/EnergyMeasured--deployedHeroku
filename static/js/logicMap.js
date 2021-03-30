function createMap() {

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
      // "Title1": Can add values in from createmap(),
      // "Title2": Can add values in from createmap()
  };

  // Create the map object with options
  var map = L.map("map-id", {
    center: [37.09, -95.71],
    zoom: 3,
    layers: [lightmap]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps)
  .addTo(map);
}

createMap();


// function createMarkers(response) {

//   // Pull the "Quakes" property off of response.data(features)
//   var data1 = response.element_in_data1;

//   // Initialize an array to hold earthquake markers
//   var marker1 = [];
//   var magnitude = [];

//   // Loop through the stations array
//   for (var index = 0; index < data1.length; index++) {
//       var element_in_data1 = data1[index];
//       // To pull list of coordinates from coord list
//       var coordList = element_in_data1.geometry.coordinates;

//       /////// Earthquakes Layer ///////
//       // For each latitude and longitude, create a marker and bind a popup with the data
//       var someMark = L.marker(coordList.slice(0, 2).reverse())
//           .bindPopup("<h3>" + features.properties.place + "</h3><h3>Magnitude: " + features.properties.mag + "</h3><h3>Depth: "+ coordList.slice(2, 3) + "</h3>");
//       // Add earthquarkmark to preset list
//       marker1.push(someMark);

//       // ////// Magnitude Layer ///////
//       // // Add magnitude color to visiulation
//       // var depthOfQuake = coordList.slice(2, 3)
//       // var magnitudeList = L.circleMarker(coordList.slice(0, 2).reverse(), {
//       //     color: "white",
//       //     fillColor: chooseColor(depthOfQuake),
//       //     fillOpacity: 0.4,
//       //     weight: 1.5,
//       //     radius: radiusHelper(features.properties.mag)
//       // })
//       //     .bindPopup("<h3>" + features.properties.place + "<h3><h3>Magnitude: " + features.properties.mag + "</h3><h3>Depth: "+ coordList.slice(2, 3) + "</h3>");
//       // ;

//       // //  Add magnitude to list for map 
//       // magnitude.push(magnitudeList);

//       //console.log(coordList.slice(2, 3));
//   };
//   // // Troubleshooting checking values
//   // console.log(coordList.slice(2, 3));
//   // console.log(magnitude);

//   // Create a layer group made from the bike markers array, pass it into the createMap function
//   createMap(L.layerGroup(marker1));
// };


// // Perform an API call to the EarthQuake API to get information. Call createMarkers when complete
// d3.json(someUrl, createMarkers);



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
