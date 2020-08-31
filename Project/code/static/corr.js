const corr = () => {
    var margin = {top: 100, right: 20, bottom: 30, left: 20},
        width = 900 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

    var svg = d3.select("#corr_map")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("../static/json/corr.csv", function(data) {
        dimensions = d3.keys(data[0]).filter(function(d) { return d })

        var y = {}
        for (i in dimensions) {
            name = dimensions[i]
            y[name] = d3.scaleLinear()
                .domain( d3.extent(data, function(d) { return +d[name]; }) )
                .range([height, 0])
        }

        var color = d3.scaleOrdinal()
            .domain([10,20,30,45,65,80])
            .range(["#823935", "#89BEB2", "#C9BA83", "#CDA49E", "#DED38C","#DE9C53"])

        var y = {}
         for (i in dimensions) {
            name = dimensions[i]
            y[name] = d3.scaleLinear()
                .domain( d3.extent(data, function(d) { return +d[name]; }) )
                .range([height, 0])
         }

        x = d3.scalePoint()
            .range([0, width])
            .domain(dimensions);

        var highlight = function(d){

            selected_age = d.age

            d3.selectAll(".line")
                .transition().duration(200)
                .style("stroke", "lightgrey")
                .style("opacity", "0.2")

            d3.selectAll("." + selected_age)
              .transition().duration(200)
              .style("stroke", color(selected_age))
              .style("opacity", "0.5")
        }

        var doNotHighlight = function(d){
            d3.selectAll(".line")
                .transition().duration(200).delay(1000)
                .style("stroke", function(d){ return( color(d.age))} )
                .style("opacity", "0.2")
        }

        function path(d) {
              return d3.line()(dimensions.map(function(p) { return [x(p), y[p](d[p])]; }));
        }

        svg
            .selectAll("myPath")
            .data(data)
            .enter()
            .append("path")
              .attr("class", function (d) { return "line " + d.age } )
              .attr("d",  path)
              .style("fill", "none" )
              .style("stroke", function(d){ return( color(d.age))} )
              .style("opacity", 0.2)
              .on("mouseover", highlight)
              .on("mouseleave", doNotHighlight)

        svg.selectAll("myAxis")
            .data(dimensions).enter()
            .append("g")
            .attr("class", "axis")
            .attr("transform", function(d) { return "translate(" + x(d) + ")"; })
            .each(function(d) { d3.select(this).call(d3.axisLeft().ticks(5).scale(y[d])); })
            .append("text")
            .style("text-anchor", "middle")
            .attr("font-family", "Open Sans")
            .attr("font-size", "12px")
            .attr("fill", "#5c6363")
            .attr("y", -9)
            .text(function(d) { return d; })
            .style("fill", "#5c6363")
     })
}