console.log('is this working2');

function buildPlot() {
    /* data route */
    const url = "/api/data";
    d3.json(url).then(function(response) {

        console.log(response);
        
        const data = response;

        const layout = {
            width: 400,
            height: 500,
            margin: { t: 0, r: 0, l: 5, b: 0 }
        };

        Plotly.newPlot("circlePlot", data, layout);
    });
}

buildPlot();
console.log('is this working');

// console.log('is this working2');
// function buildPlot() {
//     /* data route */
//     const url = "/api/data";
//     d3.json(url).then(function(response) {

//     console.log(response);
    
//       const data = response;

//       const layout = {
//         scope: "usa",
//         title: "US Percentage",
//         showlegend: false,
//         height: 600,
//               // width: 980,
//         geo: {
//           scope: "usa",
//           projection: {
//             type: "albers usa"
//           },
//           showland: true,
//           landcolor: "rgb(217, 217, 217)",
//           subunitwidth: 1,
//           countrywidth: 1,
//           subunitcolor: "rgb(255,255,255)",
//           countrycolor: "rgb(255,255,255)"
//         }
//       };

//       Plotly.newPlot("plot", data, layout);
//     });
// }

// buildPlot();
// console.log('is this working');