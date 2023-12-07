console.log("store.js is running");

$(document).ready(function() {
    $('#add-button').click(function(event) {
        event.preventDefault();

        // Get url
        var url = $(this).data('url');
        
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                product_id: $(this).val(),
                quantity: $('#select option:selected').text(),
                csrfmiddlewaretoken: csrf_token,
                action: 'post',
            },
            success: function(json) {
                console.log(json);

                document.getElementById('cart_qty').textContent = json.product_quantity;
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ":" + xhr.responseText);
            }
        });
        console.log("acess ajax sucessfully");
    })
})