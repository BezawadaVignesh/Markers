var barconfig = {
    type: 'bar',
    data: {
      datasets: [
        {
        data: bar_data,
        //backgroundColor: ['#e49f0a', '#46c016', '#b43827', '#1a086b'],
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
  window.onload = function() {
    //var ctx = document.getElementById('pie-chart').getContext('2d');
    window.myBar = new Chart(document.getElementById('bar-chart').getContext('2d'), barconfig)
    console.log(line_data)
  };  