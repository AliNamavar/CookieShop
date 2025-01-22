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

function addProductToCart(productId) {
    const productCount = $('#pro_qty_' + productId).val();
    $.get('/add-to-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        swal.fire({
            text: res.text,
            icon: res.icon,
            confirmButtonText: res.confirmButtonTextBack,
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
            // if (res.status === 'success') {
            $('#cartPriceAjax .cart__price span').text('$' + res.cart_total_price);

            // }
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
            } else if (res.status === 'success') {
                $(`#product-heart-${productId}`).addClass('active');
            }
            // else if (res.status === 'removed') {
            // // حذف کردن کلاس active
            // $(`#product-heart-${productId}`).removeClass('active');

        })

    })
}

function addProductToCartFavorite(event, productId) {
    const minProductCount = $('#min_value_count_' + productId).val();
    $.get('/add-to-cart?product_id=' + productId + '&count=' + minProductCount).then(res => {
        if (res.status === 'success') {
            $('#cartPriceAjax .cart__price span').text('$' + res.cart_total_price);
            Swal.fire({
                text: 'حداقل مقداری که میتونید این محصول رو خریداری کنید به سبد خرید شما اضافه شد میتوانید در سبد خرید مقدار را ویرایش کنید',
                icon: res.icon || 'success',
                reverseButtons: true
            }).catch(error => {
                console.error("SweetAlert Error:", error);
            });
        }
    }).catch(error => {
        console.error("AJAX Error:", error);
    });
}


function removeProductFavorite(ProductId) {
    $.get('/Favorite-rm-product?productId=' + ProductId).then(res => {
        if (res.status === 'success') {
            $('#ajax_rm_favorite_product').html(res.data);
            bindQuantityButtons();
        } else {
            console.error(res.message);

        }

    })
}


$(document).ready(function () {
    $('#addressForm').on('submit', function (event) {
        // جلوگیری از رفتار پیش‌فرض فرم
        event.preventDefault();

        // گرفتن URL از data-attribute فرم

        // گرفتن مقدار آدرس از فیلد
        var address = $('#id_address_address_check').val();

        // ارسال درخواست AJAX
        $.ajax({
            url: '/check-address/', // URL ویو که در data-url فرم قرار داده شده
            type: "POST",
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value // گرفتن CSRF Token از فرم
            },
            data: {
                address: address
            },
            success: function (res) {
                if (res.status === 'success') {
                    Swal.fire({
                        text: res.text || 'Operation completed successfully!',
                        icon: res.icon || "success",
                        confirmButtonText: res.confirmButtonTextBack || 'Ok'
                    });
                }
            },
            error: function () {
                Swal.fire({
                    text: "An error occurred while processing your request.",
                    icon: "error",
                    confirmButtonText: "Try Again"
                });
            }
        });
    });
});

setTimeout(function () {
    var messageBox = document.getElementById('message-box');
    if (messageBox) {
        messageBox.style.display = 'none';
    }
}, 3000);