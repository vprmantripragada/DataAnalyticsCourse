function buildMetadata(sample) {
    var metadataURL = "/metadata/${sample}";
    d3.json(metadataURL).then(function(data) {
        var samplemeta =  d3.select("#sample-metadata");
        samplemeta.html("");
        Object.defineProperties(data).forEach(([key,value]) => {
            samplemeta.append("pair").text('${key}:${value}');
        });
    });
}

function buildCharts(sample) {
    var sampledataURL = "/samples/${sample}";
    d3.json(sampledataURL).then(function(data) {
        var values =  data["sample_values"];
        var labels = data["otu_labels"];
        var x_otu_id = data["otu_ids"];
        var y_values = data["sample_values"];

        var trace1 = {
            values: values.splice(0,10),
            labels: labels.splice(0,10),
            type: 'pie'
          };

        data = [trace1];
        var layout = {
            text: values.splice(0,10)
        };

        Plotly.newplot('pie', data, layout);
        
        var trace2 = {
            x: x_out_id,
            y: y_values,
            mode: "markers",
            marker: {
                size: values,
                color:x_otu_id,
                labels: labels,
                type: 'scatter',
                opacity: 0.5
            }
          };

        data2 = [trace2];
        var layout2 = {
            xaxis: {title: 'Otu_ID'},
            yaxis: {title: 'Sample values'},
            showlegend: true
        };

        Plotly.newplot('bubble', data2, layout2);

    });
}

function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/names").then((sampleNames) => {
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = sampleNames[0];
      buildCharts();
      buildMetadata();
    });
  }
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildCharts();
    buildMetadata();
  }
  
  // Initialize the dashboard
  init();