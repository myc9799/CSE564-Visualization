  const age_chart_1 = (data) => {
            var width = 600
           height = 400
           margin = 40

       var radius = Math.min(width, height) / 2 - margin

       var svg = d3.select("#first_age")
                   .append("svg")
                   .attr("width", width)
                   .attr("height", height)
                   .append("g")
                   .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")

       var color1 = d3.scaleOrdinal()
                    .domain(data.map((d) => d.class))
                    .range(["#ddeea8", "#fbe8a4", "#efa86c", "#d35e50", "#7ab8ab","#96caa8"])

       var pie = d3.pie()
                    .value(function(d) {return d.num; })

       var data_ready = pie(data)

       var arc = d3.arc()
                    .innerRadius(radius*0.9)
                    .outerRadius(radius*0.6)

       var arcs = svg.selectAll(".arc")
                    .data(data_ready)
                    .enter().append("g")
                    .attr("class", "arc")
                    .attr("class", "lines")
                    .attr("class", "labels")

       var outerArc = d3.arc()
                    .outerRadius(radius * 0.9)
                    .innerRadius(radius * 0.9)

       arcs.append('path')
                    .attr('d',arc)
                    .attr('fill', function(d){ return(color1(d.data.class)) })
                    .style("opacity", 0.7);


       arcs.append("g").classed('lines', true)
       arcs.append("g").classed('labels', true)

       var polyline = svg.select('.lines')
                    .selectAll('polyline')
                    .data(data_ready)
                    .enter().append('polyline')
                    .attr('points', function(d) {
                        var pos = outerArc.centroid(d);
                        pos[0] = radius * 0.95 * (midAngle(d) < Math.PI ? 1 : -1);
                        return [arc.centroid(d), outerArc.centroid(d), pos]
                    })

       var label = svg.select('.labels')
                            .selectAll('text')
                           .data(data_ready)
                           .enter()
                           .append('text')
                           .text(function(d){ return d.data.class})
                           .attr("font-family",  "Open Sans")
                           .attr("font-size", "12px")
                           .attr("fill", "#3c3f41")
                           .attr('dy', '-.3em')
                           .attr('transform', function(d) {
                                  var pos = outerArc.centroid(d);
                                  pos[0] = radius * 0.95 * (midAngle(d) < Math.PI ? 1 : -1);
                                  return 'translate(' + pos + ')';
                           })

       function midAngle(d) {
            return d.startAngle + (d.endAngle - d.startAngle) / 2;
       }

svg.append("text")
    	   .attr("text-anchor", "middle")
           .attr("font-family", "Open Sans")
           .attr("font-size", "16px")
           .attr("fill", "#5c6363")
    	   .text("Age Distribution");

  }


