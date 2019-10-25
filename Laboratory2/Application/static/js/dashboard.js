window.addEventListener("load", (e) => {

     $('#client_distribution_select').on("change", function () {
         var value = $(this).find("option:selected").val();
         $.getJSON(`/client_distribution/${value}`, data => {
            Plotly.newPlot('client_distribution_data', data, {});
        })
     });

     $('#products_shops_population_select').on("change", function () {
         var value = $(this).find("option:selected").val();
         $.getJSON(`/products_shops_population/${value}`, data => {
            Plotly.newPlot('products_shops_population_graph', data, {});
        })
     });
});
