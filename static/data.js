function fetchdata(){
    Cash.innerText = $.ajax({ type: "GET",   
                    url: "/api/cash",   
                    async: false
                    }).responseText;
    Buying_Power.innerText = $.ajax({ type: "GET",   
                    url: "/api/buying_power",   
                    async: false
                    }).responseText;
    Current_balance.innerText = $.ajax({ type: "GET",   
                    url: "/api/current_balance",   
                    async: false
                    }).responseText;
    Gain.innerText = $.ajax({ type: "GET",   
                    url: "/api/gain",   
                    async: false
                    }).responseText;
    $.ajax({
    type: "GET",
    url: "/api/portfolio",
    dataType: "json",
    success: function(response){
        console.log(Object.keys(response))
        console.log(Object.values(response))
        new Chart(document.getElementById("pie-chart"), {
            type: 'pie',
            data: {
                labels: Object.keys(response),
                datasets: [{
                label: "US Dollars",
                backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                data: Object.values(response)
                }]
            },
            options: {
                title: {
                display: true,
                text: 'Portfolio Diversity'
                }
            }
        });
    }
    })
    $.ajax({
    type: 'GET',
    url: '/api/history',
    dataType: 'json',
    success : function(response){
    console.log(response)
    console.log(Object.keys(response))
    console.log(Object.values(response))
    new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
        labels: Object.keys(response),
        datasets: [{ 
            data: Object.values(response),
            borderColor: "#3e95cd",
            fill: false
            }
        ]
        },
        options: {
        title: {
            display: true,
            text: 'Portfolio Value(in $USD)'
        },
        legend: {
        display: false
        }
        }
    });
    }
    })
    var $body = $('#transactions');
    $body.empty()
    $.ajax({
    type: 'GET',
    url: '/api/orders',
    dataType: 'json',
    success: function(response){
    const keys = Object.keys(response)
    keys.forEach((key,index) => {
        var tableEntry = `<tr>`
        console.log(key)
        for (let i = 0; i < response[key].length; i++) {
        tableEntry += `<td>${response[key][i]}</td>`;   
        }
        tableEntry += '<tr>'
        $body.append(tableEntry)
    });
    }
    })
}
    fetchdata()
    $(document).ready(function(){
    setInterval(fetchdata,60000);
});