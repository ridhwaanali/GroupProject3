function Func(){
    fetch("./final.json")
    .then ((res) =>{ 
        return res.json();
    });
    var trace1= {
        x: 'GDP',
        y: '2022 POP',
        mode: 'markers',
        type: 'scatter', 
        marker: {size: 12}
    };
    var trace2= {
        x: 'GDP',
        y: '2022 POP',
        mode: 'line+markers',
        type: 'scatter', 
    };
    var data= [trace1, trace2];
    Ploty.newPlot('myDiv', data);
};