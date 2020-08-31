const world_map = () => {


        var width = document.getElementById('container').offsetWidth;
        var height = width / 2 + 100;

        var topo, projection, path, svg, g, pop_data, gdp_data;

        var tooltip = d3.select("#container")
                    .append("div")
                    .attr("class", "tooltip hidden");

       //d3.select(window);

        setup(width,height);

        function setup(width,height){
              projection = d3.geoMercator()
                .translate([(width/2), (height/2)])
                .scale( width / 2 / Math.PI);

              path = d3.geoPath().projection(projection);

              svg = d3.select("#container")
                  .append("svg")

                  .attr("width", width)
                  .attr("height", height)
                  .append("g");

        }



        d3.json("../static/json/world-topo-min.json", function(error, world) {
            var countries = topojson.feature(world, world.objects.countries).features;
            topo = countries;
            draw(topo);
        });

        d3.json("../static/json/pop.json", function(error, pop){
            pop_data = pop;
        });

        d3.json("../static/json/gdp.json", function(error, gdp){
            gdp_data = gdp;
        });

        function draw(topo) {
           var country =  svg.selectAll(".country").data(topo)
              .enter().insert("path")
              .attr("class", "country")
              .attr("d", path)
              .attr("id", function(d,i) { return d.id; })
              .attr("title", function(d,i) { return d.properties.name; })
              .style("fill", function(d, i) { return d.properties.color; });

            var offsetL = document.getElementById('container').offsetLeft+20;
            var offsetT = document.getElementById('container').offsetTop+10;

            country.on("mouseover", function(d,i) {
                var gdp = 'None';
                var pop = 'None';
                var mouse = d3.mouse(svg.node()).map( function(d) { return parseInt(d); } );

                pop_data.forEach(function(ele){
                        if(ele.class.toLowerCase() == d.properties.name.toLowerCase())
                        {
                            pop = ele.num;
                            d.properties.name = ele.class;
                        }
                });

                gdp_data.forEach(function(ele){
                        if(ele.class.toLowerCase() == d.properties.name.toLowerCase())
                            {gdp = ele.num;}
                });

                if(gdp !='None'){
                    tooltip.classed("hidden", false)
                            .attr("style", "left:"+(mouse[0])+"px;top:"+(mouse[1])+"px")
                            .html(d.properties.name +"<br> number of cases per 100k:"+pop+"<br> GDP per person:"+gdp);

                }


            })
                   .on("mouseout",  function(d,i) {
                        tooltip.classed("hidden", true);
            })
                    .on("click", function(d,i){

                        console.log(d.properties.name)
                        setInterval(function query() {
                                    $.ajax({
                                        url: "update_map",
                                        type: "POST",
                                        data: d.properties.name,
                                        dataType: "text"
                                    })
                                }, 1000);

             });
        }


        function redraw() {
            width = document.getElementById('container').offsetWidth;
            height = width / 2;
            d3.select('svg').remove();
            setup(width,height);
            draw(topo);
        }


}