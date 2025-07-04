// Register plugin for center text
const centerTextPlugin = {
  id: 'centerText',
  afterDatasetsDraw(chart) {
    const { ctx, width, height } = chart;
    ctx.save();

    const opts = chart.config.options.plugins.centerText;
    ctx.font = `${opts.fontSize || 24}px ${opts.fontFamily || 'Arial'}`;
    ctx.fillStyle = opts.color || '#000';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    const textX = width / 2;
    const textY = height / 2;
    ctx.fillText(opts.text, textX, textY);

    ctx.restore();
  }
};

Chart.register(centerTextPlugin);

// Chart data
const chartData = {
  labels: ['Red', 'Blue', 'Yellow'],
  datasets: [{
    data: [45, 25, 30],
    backgroundColor: ['#f28b82','#aecbfa','#fff475']
  }]
};

// Compute total
const total = chartData.datasets[0].data.reduce((a, b) => a + b, 0);

const config = {
  type: 'doughnut',
  data: chartData,
  options: {
    cutout: '60%',
    plugins: {
      centerText: {
        text: `Total: ${total}`,
        color: '#333',
        fontSize: 28,
        fontFamily: 'Arial'
      },
      legend: {
        position: 'bottom'
      }
    }
  }
};

// Render the chart
new Chart(document.getElementById('myChart'), config);
