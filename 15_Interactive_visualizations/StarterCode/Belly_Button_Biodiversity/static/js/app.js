function buildMetadata(sample) {
  var metadataURL = `/metadata/${sample}`;
  d3.json(metadataURL).then(function(response) {
      var data =response;
      var samplemeta =  d3.select("#sample-metadata");
      samplemeta.html("");
      Object.entries(data).forEach(([key,value]) => {
          samplemeta.append("p").text(`${key}:${value}`);
      });
  });
}

function buildCharts(sample) {
  var sampledataURL = `/samples/${sample}`;
  d3.json(sampledataURL).then(function(response) {
    //if (error) return console.log(error);
      var values_pie =  response["sample_values"];
      var labels_pie = response["otu_labels"];
      var x_otu_id = response["otu_ids"];
      var y_values = response["sample_values"];

      console.log(values_pie, labels_pie);
      console.log(x_otu_id, y_values);

      var data1 = [{
          values: values_pie.splice(0,10),
          labels: x_otu_id.splice(0,10),
          //text: labels_pie.splice(0,10),
          type: 'pie'
        }];

      Plotly.newPlot('pie', data1);
      
      var trace2 = {
          x: x_otu_id,
          y: y_values,
          mode: "markers",
          marker: {
              size: values_pie,
              color:x_otu_id,
              labels: labels_pie,
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

      Plotly.newPlot('bubble', data2, layout2);

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
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();

