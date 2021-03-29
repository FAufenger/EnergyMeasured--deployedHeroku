function buildPlot2() {
    /* data route */
    const url = "/api/data2";
    d3.json(url).then(function(response) {

        const data = response;

        const layout = {
            title: 'US Power Generation',
            xaxis: {tickfont: {
                size: 14,
                color: 'rgb(107, 107, 107)'
              }},
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



buildPlot2();