console.log("store.js is running");

$(document).ready(function() {
    // add product to cart
    $('#add-button').click(function(event) {
        event.preventDefault();
        add_product($(this));
    });

    // delete product from cart
    $('.delete-button').click(function(event) {
        event.preventDefault();
        delete_product($(this));
    });

    // update product quantity
    $('.update-button').click(function(event) {
        event.preventDefault();
        update_product($(this));
    })

    // message timer
    var message_timeout = document.getElementById('message-timer');
    if (message_timeout) {
        setTimeout(function() {
            message_timeout.style.display = 'none';
        }, 5000);
    }
});

function update_product(button) {
    var url = button.data('url');
    
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            product_id: button.data('index'),
            quantity: $('#select' + button.data('index') + ' option:selected').text(),
            csrfmiddlewaretoken: csrf_token,
            action: 'post',
        },
        success: function(json) {
            console.log(json);

            document.getElementById('cart_qty').textContent = json.product_quantity;
            document.getElementById('total').textContent = json.total_price;
            location.reload(true); // reload page
        },
        error: function(xhr, errmsg, err) {
            console.log(xhr.status);
        }
    })
}

function delete_product(button) {
    var url = button.data('url');
    console.log("acess delele_product function");

    $.ajax({
        type: 'POST',
        url: url,
        data: { 
            product_id: button.data('index'),
            csrfmiddlewaretoken: csrf_token,
            action: 'post',
        },
        success: function(json) {
            console.log(json);

            document.getElementById('cart_qty').textContent = json.product_quantity;
            document.getElementById('total').textContent = json.total_price;
            location.reload();  // reload page
        },
        error: function(xhr, errmsg, err) {
            console.log(xhr.status);
        }
    });
}

function add_product(button) {
    var url = button.data('url');
        
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            product_id: button.val(),
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
}