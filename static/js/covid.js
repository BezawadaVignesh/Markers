var pieconfig = {
  type: 'pie',
  data: {
      labels: pie_labels,
      datasets: [{
          data = pie_data,
          backgroundColor: [
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(255, 99, 132, 0.2)',
          ],
          borderColor: [
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(255, 99, 132, 1)',
          ],
          borderWidth: 1
      }]
  },
  options: {
      title: {
          display: true,
          text: "Covid Global View"
      },
      legend: {
          display: true,
          position: "left",
      }
  }
}
window.onload = function() {
  //var ctx = document.getElementById('pie-chart').getContext('2d');
  window.myBar = new Chart(document.getElementById('bar-chart').getContext('2d'), pieconfig );/*
  window.myBar = new Chart(document.getElementById('bar-chart').getContext('2d'), 
  {
      type: 'bar',
      data: {
          labels: ['Recovered', 'Active', 'Deaths'],
          datasets: [{
              data: [123655222, 12533652, 98565214],
              backgroundColor: [
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(255, 99, 132, 0.2)',
              ],
              borderColor: [
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(255, 99, 132, 1)',
              ],
              borderWidth: 1
          }]
      },
      options: {
          title: {
              display: true,
              text: "Covid Global View"
          },
          legend: {
              display: true,
              position: "left",
          }
      }
  }
  );*/
  
};
var barconfig = {
  type: 'bar',
  data: {
    datasets: [
      {
      data: bar_data,
      backgroundColor: ['#e49f0a', '#46c016', '#b43827', '#1a086b'],
      label: 'Population in million'
    },
    {
      data: bar_data,
      backgroundColor: ['#e49f0a', '#46c016', '#b43827', '#1a086b'],
      label: 'Population in million'
    }],
    labels: bar_labels
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'bottem',
      },
      title: {
        display: true,
        text: 'Chart.js Line Chart'
      }
    }
  },
};

var lineconfig = {
  type: 'line',
  
  data: {
    datasets: [
    {
      data: line_data[0],
      label: 'Confirmed',
      fill: false,
      borderColor: ['rgba(0,0,125,0.5)'],
      
    },
    {
      data: line_data[1],
      label:'Recovered',
      fill: false,
      borderColor: ['rgba(0,150,0,0.5)'],
      
    }
  ],
    labels:  line_labels
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Line Chart'
      }
    }
  },
  
};
/*
window.onload = function() {
  var ctx = document.getElementById('pie-chart').getContext('2d');
  window.myPie = new Chart(ctx, pieconfig);
  window.myBar = new Chart(document.getElementById('bar-chart').getContext('2d'), barconfig)
  window.myLine = new Chart(document.getElementById('line-chart').getContext('2d'), lineconfig)
  console.log(line_data)
};*/