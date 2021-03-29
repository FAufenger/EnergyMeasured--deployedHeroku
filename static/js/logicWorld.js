function buildPlot4() {
    /* data route */
    const url = "/api/data4";
    
    d3.json(url).then(function(dataImport) {

        // var country_list_unique = []
        // var country_name = []
        // var code_list = []
        // var year_list_unique = []
        // var solar_list = []
        // var wind_list = []
        // var hydro_list = []
        // var geo_biomass_other_list = []

        // Create a contains function
        Array.prototype.contains = function(v) {
            for (var i = 0; i < this.length; i++) {
              if (this[i] === v) return true;
            }
            return false;
          };
        // Use contains function to find desired unique values  
        Array.prototype.uniqueCountry = function() {
            var arr = [];
            for (var i = 0; i < this.length; i++) {
              if (!arr.contains(this[i][0])) {
                arr.push(this[i][0]);
              }
            }
            return arr;
          }
        

        var country_list_unique = dataImport.uniqueCountry();
  

        function getCountryData(chosenCountry) {
            currentYear = []
            currentSolar = [];
            currentWind = [];
            currentHydro = [];
            currentGeoBiomassOther = [];
            for (var i = 0 ; i < dataImport.length ; i++){
                if ( dataImport[i][0] === chosenCountry) {
                    currentYear.push(dataImport[i][2]);
                    currentSolar.push(dataImport[i][3]);
                    currentWind.push(dataImport[i][4]);
                    currentHydro.push(dataImport[i][5]);
                    currentGeoBiomassOther.push(dataImport[i][6]);
                }
    
            }
        };
        
        

        // Default Country Data
        setBubblePlot('Africa');
    
        function setBubblePlot(chosenCountry) {
            getCountryData(chosenCountry);
            
            
            // Set data to be plotted
            trace1 = {
                "x": currentYear,
                "y": currentSolar,
                "name": 'Solar',
                "marker": {"color": "#EDCA1C"},
                "type": "lines+markers"
            };
            trace2 = {
                "x": currentYear,
                "y": currentWind,
                "name": 'Wind',
                "marker": {"color": "#ED1CD1"},
                "type": "lines+markers"
            };
            trace3 = {
                "x": currentYear,
                "y": currentHydro,
                "name": 'Hyrdo',
                "marker": {"color": "#1C6CED"},
                "type": "lines+markers"
            };
            trace4 = {
                "x": currentYear,
                "y": currentGeoBiomassOther,
                "name": 'Geo Biomass and Other',
                "marker": {"color": "#1CED41"},
                "type": "lines+markers"
            };

            var data = [trace1, trace2, trace3, trace4];

            const layout = {
                width: 800,
                height: 400,
                title: 'Power Generation on a Global Scale',
                xaxis: {tickfont: {
                    size: 14,
                    color: 'rgb(107, 107, 107)'
                }},
                yaxis: {
                title: 'Terawatt-hour',
                titlefont: {
                    size: 16,
                    color: 'rgb(107, 107, 107)'
                },
                tickfont: {
                    size: 14,
                    color: 'rgb(107, 107, 107)'
                }
                },
                //margin: { t: 50, r: 500, l: 500, b: 50 }
            };

            Plotly.newPlot("linePlotWorld1", data, layout);
        }
        
        var innerContainer = document.querySelector('[data-num="0"');
        var plotEl = innerContainer.querySelector('.plot');
        var countrySelector = innerContainer.querySelector('.countrydata');

        function assignOptions(textArray, selector) {
            for (var i = 0; i < textArray.length;  i++) {
                var currentOption = document.createElement('option');
                currentOption.text = textArray[i];
                selector.appendChild(currentOption);
            }
        }

        assignOptions(country_list_unique, countrySelector);

        function updateCountry(){
            setBubblePlot(countrySelector.value);
        }

        countrySelector.addEventListener('change', updateCountry, false);
    });
}

 

buildPlot4();
console.log('hello')
// function buildPlot5() {
//     /* data route */
//     const url = "/api/data4";
//     d3.json(url).then(function(response) {

//         console.log(response);
        
//         const data = response;

//         const layout = {
//             width: 400,
//             height: 400,
//             margin: { t: 50, r: 500, l: 500, b: 50 }
//         };

//         Plotly.newPlot("barPlot", data, layout);
//     });
// }




// buildPlot5();
