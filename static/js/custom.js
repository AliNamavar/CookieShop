function scrollToForm(event) {
    event.preventDefault();
    // location.reload();
    const form = document.getElementById('commentForm');
    if (form) {
        form.scrollIntoView({behavior: 'smooth'});
        form.focus();
    }
}

function fillpatternid(parentId, event) {

    event.preventDefault();


    $('#parent_id').val(parentId);
    console.log($('#parent_id').val());
    console.log(parentId);


    const form = document.getElementById('commentForm');
    if (form) {
        form.scrollIntoView({behavior: 'smooth'});
        setTimeout(function () {
            const firstInput = form.querySelector('input, textarea');
            if (firstInput) {
                firstInput.focus();
            }
        }, 500);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('feedbackForm').addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(this);
        fetch(this.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        }).then(response => response.json())
            .then(data => {
                Swal.fire({
                    text: data.text,
                    icon: data.icon,
                    confirmButtonText: 'باشه',
                    reverseButtons: true
                }).then(confirm => {
                    if (data.status === 'not_auth') {
                        window.location.href = '/login';
                    }
                }).then(() => {
                    if (data.status === 'success') {
                        $('#form_input_home').html(data.body);

                        $('.owl-carousel').owlCarousel({
                            loop: true,
                            margin: 10,
                            items: 2,
                            autoplay: true,
                            autoplayHoverPause: true
                        });
                    }
                });
            }).catch(error => {
            Swal.fire({
                text: 'خطایی رخ داده است',
                icon: 'error',
                confirmButtonText: 'باشه',
                reverseButtons: true
            });
        });
    });
});


// function addProductToCart(productId) {
//     const productCount = $('#pro_qty_' + productId).val();
//     $.get('/add-to-cart?product_id=' + productId + '&count=' + productCount).then(res => {
//         swal.fire({
//             text: res.text,
//             icon: res.icon,
//             showCancelButton: false,
//             confirmButtonText: res.confirmButtonTextBack,
//             reverseButtons: true
//         }).then(confirm => {
//             if (confirm.isConfirmed && res.status === 'not_auth') {
//                 window.location.href = '/login';
//             }
//         });
//     });
// }
function addProductToCart(productId) {
    const productCount = $('#pro_qty_' + productId).val();
    $.get('/add-to-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        swal.fire({
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonText: res.confirmButtonTextBack,
            reverseButtons: true
        }).then(confirm => {
            if (confirm.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        });

        if (res.status === 'success') {
            $('#cartPriceAjax .cart__price span').text('$' + res.cart_total_price);
        }
    });
}


$(document).ready(function () {
    bindQuantityButtons();
});


function removeProductCart(productID) {
    $.get('remove-product-cart?product_rm_id=' + productID).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
            bindQuantityButtons();
        }
    });
}


function update_detail_count(element) {
    var $this = $(element);
    var productId = $this.find('input').attr('id').split('_')[2];
    var new_count = parseInt($this.find('input').val());

    $.get('update-cart-product-count?product_id_count_edit=' + productId + '&new_count=' + new_count).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
            bindQuantityButtons();
            if (res.status === 'success') {
                $('#cartPriceAjax .cart__price span').text('$' + res.cart_total_price);
            }

        } else {
            console.error(res.message);
        }
    });
}


function bindQuantityButtons() {
    $('.pro-qty').each(function () {
        var $this = $(this);
        var productId = $this.find('input').attr('id').split('_')[2];
        var min_value_count = parseFloat($('#min_value_count_' + productId).val());

        if (!$this.find('.dec').length) {
            $this.prepend('<span class="dec qtybtn">-</span>');
        }

        if (!$this.find('.inc').length) {
            $this.append('<span class="inc qtybtn">+</span>');
        }

        $this.off('click', '.qtybtn').on('click', '.qtybtn', function () {
            var $button = $(this);
            var oldValue = parseFloat($button.parent().find('input').val());
            var newVal;
            if ($button.hasClass('inc')) {
                newVal = oldValue + 1;
            } else {
                newVal = oldValue > min_value_count ? oldValue - 1 : min_value_count;
            }
            $button.parent().find('input').val(newVal);
            update_detail_count($button.parent());
        });
    });
}


$(document).ready(function () {
    bindQuantityButtons();

    $('.pro-qty').on('change', 'input', function () {
        update_detail_count($(this).parent()); // فراخوانی تابع به‌روزرسانی پس از تغییر مقدار ورودی
    });
});


function fillpage(num) {
    $('#input-page-fill').val(num)
    $('#form-fill-page').submit();


}

function check_address() {
    var text = $('#id_address_address_check').val()
    $.post('check-address', {address: text}).then(res => {
        // if(res.status === 'success')
    })

}

function addProductToFavorite(productId) {
    // console.log(productId)
    $.get('/add-product-to-favorite?products_id=' + productId).then(res => {
        console.log(res)
        swal.fire({
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonText: res.confirmButtonTextBack,
            reverseButtons: true
        }).then(confirm => {
            if (confirm.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        })

    })
}


function addProductToCartFavorite(event, productId) {
    const minProductCount = $('#min_value_count_' + productId).val();
    $.get('/add-to-cart?product_id=' + productId + '&count=' + minProductCount).then(res => {
        console.log(res);
        Swal.fire({
            text: 'حداقل مقداری که میتونید این محصول رو خریداری کنید به سبد خرید شما اضافه شد میتوانید در سبد خرید مقدار را ویرایش کنید',
            icon: res.icon,
            showCancelButton: false,
            confirmButtonText: res.confirmButtonTextBack,
            reverseButtons: true
        }).then(confirm => {
            if (confirm.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        });
    });
}


function removeProductFavorite(ProductId) {
    console.log(ProductId)
    $.get('/Favorite-rm-product?productId=' + ProductId).then(res => {
        console.log(res)
        if (res.status === 'success') {
            $('#ajax_rm_favorite_product').html(res.data)
        }
    })
}