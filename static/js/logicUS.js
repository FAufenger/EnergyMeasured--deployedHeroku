// Circle plot US
function buildPlot1() {

  /* data route */
  const url = "/api/data1";

  d3.json(url).then(function (response) {

    // Create a contains function
    Array.prototype.contains = function (v) {
      for (var i = 0; i < this.length; i++) {
        if (this[i] === v) return true;
      }
      return false;
    };

    // Use contains function to find desired unique values  
    Array.prototype.uniqueState = function () {
      var arr = [];
      for (var i = 0; i < this.length; i++) {
        if (!arr.contains(this[i][0])) {
          arr.push(this[i][0]);
        }
      }
      return arr;
    }


    var state_list_unique = response.uniqueState();

    function getStateData(chosenState) {
      currentValues = [];
      currentState = [];
      nuclear = [];
      coal = [];
      naturalGas =[];
      petroleum =[];
      hydro =[];
      geothermal =[];
      solar =[];
      wind = [];
      biomassOther =[];

      for (var i = 0; i < response.length; i++) {
        if (response[i][0] === chosenState) {
          currentState.push(response[i][0]);
          nuclear.push(response[i][1]);
          coal.push(response[i][2]);
          naturalGas.push(response[i][3]);
          petroleum.push(response[i][4]);
          hydro.push(response[i][5]);
          geothermal.push(response[i][6]);
          solar.push(response[i][7]);
          wind.push(response[i][8]);
          biomassOther.push(response[i][9]);
          currentValues.push(nuclear, coal, naturalGas, petroleum, hydro, geothermal, solar, wind, biomassOther);
        }
      }
    };
 
    
    // Default State Data
    setBubblePlot('Alabama');
    

    function setBubblePlot(chosenState) {
      getStateData(chosenState);


      trace1 = {
        type: "pie",
        showlegend: false,
        rotation: 0,
        textinfo: "text+percent",
        textposition: "outside",
        values: currentValues,
        text: ["Nuclear", "Coal", "Natural Gas", "Petroleum", "Hydro", "Geothermal", "Solar-PV", "Wind", "Biomass/ Other"],
        hoverinfo: "skip",
        autopct: '%1.1f%%',
        marker: {
          colors: ["#347C17", "#6960EC", "#43C6DB", "#3EA055", "#FFFF00", "#FF7F50", "#4B0082", "#C48189", "#B93B8F"],
          labels: ["Nuclear", "Coal", "Natural Gas", "Petroleum", "Hydro", "Geothermal", "Solar-PV", "Wind", "Biomass/ Other"],
          hoverinfo: "skip"
        },
        title: {
          text: `<b>Percentage Energy Usage</b> <br> ${currentState}`,
          font: { "size": 20 }
        },
      };
    
      const data = trace1;

      const layout = {
        // width: 400,
        height: 500,
        // //autosize: true,
        margin: { t: 5, r: 10, l: 10, b: 200 }
      };

      Plotly.newPlot("circlePlot", data, layout);
    }


    // var innerContainer = document.querySelector('[data-num="0"');
    var stateSelector = document.querySelector('.statedata1');

    function assignOptions(textArray, selector) {
        for (var i = 0; i < textArray.length; i++) {
            var currentOption = document.createElement('option');
            currentOption.text = textArray[i];
            selector.appendChild(currentOption);
        }
    }

    assignOptions(state_list_unique, stateSelector);

    function updateState() {
        setBubblePlot(stateSelector.value);
    }

    stateSelector.addEventListener('change', updateState, false);
  });
}





//  Line chart US
function buildPlot2() {
  /* data route */
  // Static chart so can imoort data directly through python in the app.py
  const url = "/api/data2";
  d3.json(url).then(function (response) {

    const data = response;

    const layout = {
      title: 'US Power Generation',
      xaxis: {
        tickfont: {
          size: 14,
          color: 'rgb(107, 107, 107)'
        }
      },
      yaxis: {
        title: 'Billion kilowatthours',
        titlefont: {
          size: 16,
          color: 'rgb(107, 107, 107)'
        },
        tickfont: {
          size: 14,
          color: 'rgb(107, 107, 107)'
        }
      },
      legend: {
        x: 0,
        y: 1.0,
        bgcolor: 'rgba(255, 255, 255, 0)',
        bordercolor: 'rgba(255, 255, 255, 0)'
      },
    };

    Plotly.newPlot("linePlotUS", data, layout);
  });
}


// Function call  
buildPlot1();
buildPlot2();