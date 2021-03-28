function buildPlot2() {
    /* data route */
    const url = "/api/data2";
    d3.json(url).then(function(response) {

        console.log(response);
        
        const data = response;

        const layout = {
            width: 400,
            height: 400,
            margin: { t: 50, r: 500, l: 500, b: 50 }
        };

        Plotly.newPlot("barPlot", data, layout);
    });
}



// buildPlot2();