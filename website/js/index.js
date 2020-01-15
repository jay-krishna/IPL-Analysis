// var dataset=[1,2,3,4,5];

// d3.select('body').selectAll('p').data(dataset).enter().append('p').text('D3 is :)');

d3.csv("/data/combined_batting.csv").get(function(data){
	console.log(data);
});