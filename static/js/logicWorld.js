function buildPlot3() {
    /* data route */
    const url = "/api/data3";
    d3.json(url).then(function(response) {

        console.log(response);
        
        const data = response;

        const layout = {
            width: 400,
            height: 400,
            margin: { t: 50, r: 500, l: 500, b: 50 }
        };

        Plotly.newPlot("circlePlot", data, layout);
    });
}


// function buildPlot4() {
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



// buildPlot3();
// buildPlot4();