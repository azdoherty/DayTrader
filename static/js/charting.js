
$('#pltbtn').on('click', function (e) {
    var symbol = $("#symbol").val();
    // placeholder start and end dates until 
    // added to front end
    var start = "2018-10-01"
    var stop = "2019-04-05"
    var url = window.location.origin + "/symbol/" + symbol;
    var args = "?start=" + start + "&stop=" + stop;
    url += args
    $.get(url, function(data, status){
        console.log(data)
        console.log(status)
        //clearChart();
        plotSymbol(data);
       
    });
})

var plotSymbol = function(data){
    Chart.defaults.global.responsive = true;
    var chartData = {
        labels : data.labels,
        datasets : [{
            label: data.symbol,
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(75,192,192,0.4)",
            borderColor: "rgba(75,192,192,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(75,192,192,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(75,192,192,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data : data.data,
            spanGaps: false
        }]
      }
      var ctx = document.getElementById("myChart").getContext("2d");
            
          // create the chart using the chart canvas
          var myChart = new Chart(ctx, {
            type: 'line',
            data: chartData,
        });
    
        myChart.update()
};

var clearChart = function(){
    var ctx = document.getElementById("myChart").getContext("2d");
    ctx.destroy()
}