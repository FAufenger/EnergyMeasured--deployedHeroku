
function buildPlot() {
    /* data route */
    const url = "/api/data1";
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




buildPlot();


