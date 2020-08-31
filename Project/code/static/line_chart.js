const line_chart = (data) => {

     var    w = 1000
            h = 450

    var svg = d3.select("#line_chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h)


    var x = d3.scaleLinear().range([0, w-80]);
    var y = d3.scaleLinear().range([h-80, 0]);


  x.domain(d3.extent(data, function(d) { return d.year; }));
    y.domain([0, d3.max(data, function(d) { return d.num; })]);

    var xAxis = d3.axisBottom(x);
    var yAxis = d3.axisLeft(y).tickPadding(5).tickSizeInner(-(w-80));

    var chartLine = d3.line()
    	.x(function(d) { return x(d.year); })
    	.y(function(d) { return y(d.num); });


    var bisect = d3.bisector(function(d) {
      return d.year;
    }).left;

    var tooltip = d3.select('#line_chart')
    	.append('div')
    	.attr('class', 'svg-tooltip')
    	.style('opacity', 0);

    var marker = svg.append('circle')
    				.attr('cx', 0)
            .attr('cy', 0)
            .attr('r', 5)
            .attr('class', 'svg-line-marker')
            .style('stroke', '#6d827d')
            .style('fill', '#6d827d')
            .style('opacity', 0);

    var markerLine = svg.append('line')
            .classed("svg-line-marker-line", true)
            .attr('x1', w)
            .attr('y1', 40)
            .attr('x2', w)
            .attr('y2', h-50)
            .style('opacity', 0)
            .style('stroke', '#a8c9c1')
            .style('stroke-width', '10');


    svg.append("defs").append("clipPath")
      .attr("id", "clip")
      .append("rect")
      .attr("width", w-20)
      .attr("height", h-20);

    var focus = svg.append("g")
    	.attr("class", "focus")
    	.attr("transform", "translate(20,20)");

   focus.append("path")
     	.datum(data)
    	.attr("class", "svg-chart-line")
      .attr("d", chartLine);

    focus.append("g")
      .attr("class", "axis axis--x")
    	.attr("transform", "translate(0, "+(h-100)+")" )
      .call(xAxis);

    focus.append('g')
      .attr("class", "axis axis--y")
      .call(yAxis);


    var chartArea = svg.append('rect')
    	.attr('x', 0)
    	.attr('y', 0)
    	.attr('width', w)
    	.attr('height', h)
    	.style('fill', 'none')
    	.style('pointer-events', 'all');

    chartArea
    	.on("mouseover", function() {
      	d3.select(".svg-line-marker")
              .transition()
          		.duration(300)
          		.style("opacity", 20)
          		.style("stroke-width", 5);
        d3.select(".svg-line-marker-line")
                .transition().duration(300)
                .style("opacity", 20).style("stroke-width", 2);

      d3.select(".svg-tooltip")
        .transition().duration(300)
        .style("opacity", 20).style("stroke-width", 0.5);
    	})
    	.on("mouseout", function() {

      	d3.select(".svg-line-marker")
              .transition().duration(300)
          		.style("opacity", 0).style("stroke-width", 0.5);

      	d3.select(".svg-line-marker-line")
                .transition().duration(300)
                .style("opacity", 0).style("stroke-width", 0.5);

      d3.select(".svg-tooltip")
        .transition().duration(300)
        .style("opacity", 0).style("stroke-width", 0.5);

        })
        .on("mousemove", function() {
					var mouse = d3.mouse(this);
      		var xPos = mouse[0];
      		var x0 = x.invert(xPos - 20);
      		var i = bisect(data, x0);

      		var d = data[i];
      		if (d) {
            var xp = x(d.year)+20;
            var yp = y(d.num)+20;

            d3.select('.svg-tooltip').html(d.year + ": " +d.num);
            d3.select('.svg-tooltip')
            	.style('left', (xp+30 ) +'px')
            	.style('top', (yp-3) +'px');

            d3.select('.svg-line-marker')
              .style('opacity', 20).attr('transform', 'translate('+xp+', '+yp+')');
            d3.select('.svg-line-marker-line')
              .attr('y1', yp)
              .attr('x1', xp)
              .attr('x2', xp);
          }
        });

     svg.append("text")
                       .attr("x", (w / 2))
                       .attr("y", 0 - (margin.top / 2)+10)
                       .attr("text-anchor", "middle")
                       .attr("font-family", "Open Sans")
                       .attr("font-size", "16px")
                       .attr("fill", "#5c6363")
                       .text("The Trend of Suicide Cases in Top Ten countries");

}