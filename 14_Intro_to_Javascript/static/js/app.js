// from data.js
var tableData = data;

//console.log(tableData);

/* data.forEach(function(city) {
    console.log(city);
}); */

var tbody = d3.select("tbody");

tableData.forEach((city) => {
    var row = tbody.append("tr");
    Object.entries(city).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });

  var button = d3.select("#filter-btn");

  

  button.on("click", function() {

    //d3.event.preventDefault();
    
    var inputField = d3.select("#datetime");

    var inputValue = inputField.property("value");
  
    console.log(inputValue);
  
    var filteredData = tableData.filter(info => info.datetime === inputValue);

    console.log(filteredData);

    d3.select("tbody").selectAll('*').remove();

    var tbody_new = d3.select("tbody")

    filteredData.forEach((city) => {
        var row = tbody_new.append("tr");
        Object.entries(city).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
        });
    });

  });

// YOUR CODE HERE!
