var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
  };
  
  // Define dimensions of the chart area
  var chartWidth = svgWidth - margin.left - margin.right;
  var chartHeight = svgHeight - margin.top - margin.bottom;
  
  // Select body, append SVG area to it, and set its dimensions
  var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);
  
  // Append a group area, then set its margins
  var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

  d3.csv("data.csv").then(function(PopuData) {
  //  d3.csv("data.csv", function(error, PopuData){

    // Throw an error if one occurs
    //if (error) {
    //console.log(error);} 
  //console.log("line 30");
    // Print the forceData
    //console.log(PopuData);
//console.log("TEST");
          // cast the data from the csv as numbers
  PopuData.forEach(function(data) {
    data.poverty = +data.poverty;
    data.obesity = +data.obesity;
  });
 
 // Create a scale for your independent (x) coordinates
  var xScale = d3.scaleLinear()
    .domain(d3.extent(PopuData, data => data.poverty))
    .range([0, chartWidth]);


  // Create a scale for your dependent (y)  coordinates
  var yScale = d3.scaleLinear()
    .domain(d3.extent(PopuData, data => data.obesity))
    .range([chartHeight, 0]);

  var bottomAxis = d3.axisBottom(xScale);
  var leftAxis = d3.axisLeft(yScale);

  chartGroup.append("g")
  .call(leftAxis);

  chartGroup.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(bottomAxis);

    var circlesGroup = chartGroup.selectAll("circle")
    .data(PopuData)
    .enter()
    .append("circle")
    .attr("cx", function(data, index){
      return xScale(data.poverty)
    })
    .attr("cy", function(data,index){
      return yScale(data.obesity)
    })
    .attr("r",15)
    .attr("fill", "lightblue")
    //.attr("width", xScale)
    //.attr("height", data => chartHeight - yScale(data));
  
  var toolTip = d3.tip()
  .attr("class", "d3-tip")
  .offset([80, -60])
  .html(function(data) {
    
    // var abbrName = data.abbr;
    // var povertyRate = +data.poverty;
    // var obesityRate = +data.obesity;
    return (`State:${data.abbr}<br>Poverty:${data.poverty}<br>Obesity:${data.obesity}`);
  });

  chartGroup.call(toolTip);

  circlesGroup.on("click", function(data) {
    toolTip.show(data, this);
  })
    // onmouseout event
    .on("mouseout", function(data, index) {
      toolTip.hide(data);
    });

  chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (chartHeight / 2))
      .attr("dy", "1em")
      .attr("class", "aText")
      .text("Obesity (%)");

// Append x-axis labels
  chartGroup.append("text")
    .attr("transform", `translate(${chartWidth}, ${chartHeight + margin.top + 300})`)
    .attr("class", "aText")
    .text("Poverty (%)");
});
  

