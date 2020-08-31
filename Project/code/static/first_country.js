  const country_chart_1 = (data) => {
    var maxWidth = 900


    var margin = { top: 20, right: 20, bottom: 70, left: 50 },
      width = (maxWidth - margin.left - margin.right),
      height = 300 - margin.top - margin.bottom;

    var svg = d3.select("#first_country").append("svg")
      .attr("width", maxWidth)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    var x = d3.scaleBand()
      .range([0, width])
      .domain(data.map((d) => d.class));


    var y = d3.scaleLinear()
      .range([height, 0])
      .domain([0, d3.max(data, function (d) { return d.num; })]);

    // Set barWidth relative to the number of data
    const barWidth = () => (maxWidth / data.length * 0.3)

    svg.selectAll("rect")
      .data(data)
      .enter().append("rect")
      .style("fill", "#a8c9c1")
      .attr("x", function (d) { return x(d.class); })
      .attr("width", barWidth)
      .attr("y", function (d) { return y(d.num); })
      .attr("height", function (d) { return height - y(d.num); })

    var yAxis = d3.axisLeft()
      .scale(y)
      .tickSize(-width) //as wide as our graph
      .ticks(3);

    svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)

    var xAxis = d3.axisBottom()
      .scale(x);


    svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)

    svg.selectAll("label")
      .data(data)
      .enter()
      .append("text")
      .attr("class", "label")
      .attr("font-family", "Open Sans")
      .attr("font-size", "12px")
      .attr("fill", "#5c6363")
      .attr("y", function (d) { return y(d.num); })
      .attr("x", function (d) { return x(d.class); })
      .attr("dy", ".35em") //vertical align middle
      .attr("dx", ".7em") //vertical align middle
      .text(function (d) { return d.num; });


     svg.append("text")
              .attr("x", (width / 2))
              .attr("y", 0 - (margin.top / 2)+10)
              .attr("text-anchor", "middle")
              .attr("font-family", "Open Sans")
              .attr("font-size", "16px")
              .attr("fill", "#5c6363")
              .text("Top ten countries with most suicide cases");
  }

