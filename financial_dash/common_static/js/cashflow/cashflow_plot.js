// highcharts plot

// color palatte
var color_palette = ['#3A301C', '#5D4C2C', '#917645', '#B89D6A', '#D1BF9E', '#D7CFC1', '#BCCCE4', '#98B0D5', '#3E78B8'];


// pie chart body
function pie_charts(plot_area, data_series, plot_title) {
    chart = Highcharts.chart(plot_area, {
        colors: color_palette,
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 0,
            plotShadow: false,
            backgroundColor: null,
            type: 'pie'
        },
        title: {
            text: plot_title
        },
        tooltip: {
            pointFormat: '{series.name}: <b>${point.y:,.0f}</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                },
            }
        },
        series: data_series,
    });
};


// percentage area plot
function line_area(plot_area, data_series, x_axis, plot_title) {
    chart = Highcharts.chart(plot_area, {
        colors: ['#3E78B8'],
        chart: {
            type: 'area',
            backgroundColor: null,
        },
        title: {
            text: plot_title
        },
        xAxis: {
            categories: x_axis,
            tickmarkPlacement: 'on',
            title: {
                enabled: false
            },
        },
        yAxis: {
            title: {
                text: 'Capital'
            }
        },
        tooltip: {
            pointFormat: '${point.y:,.0f}<br/>',
            split: true
        },
        plotOptions: {
            area: {
                stacking: 'normal',
                lineColor: '#DCDFE4',
                lineWidth: 1,
                marker: {
                    lineWidth: 1,
                    lineColor: '#DCDFE4'
                }
            }
        },
        series: data_series,
    });
};
