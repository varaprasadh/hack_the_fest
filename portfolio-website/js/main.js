$(document).ready(function(){
    let $btns = $('.project-area .button-group button');
    $btns.click(function(e){
        $('.project-area .button-group button').removeClass('active');
        e.target.classList.add('active');

        let selector = $(e.target).attr('data-filter');
        $('.project-area .grid').isotope({
            filter:selector
        });
        return false;
    })


    // Onload trigger the button
    $('.project-area .button-group #main-btn').trigger('click');

    $('.project-area .grid .popup-link').magnificPopup({
        type:'image',
        gallery:{enabled:true}
    });


    // Owl carousel
    $('.site-main .clients-area .owl-carousel').owlCarousel({
        loop:true,
        autoplay:true,
        dots:true,
        responsive:{
            0:{
                items:1
            },
            560:{
                items:2
            }
        }
    })

    //Nav Menu
    let nav_offset_top = $('.header-area').height() + 50;
    function navBarFixed(){
        if($('.header-area').length){
            $(window).scroll(function(){
                let scroll = $(window).scrollTop();
                if(scroll>=nav_offset_top) {
                    
                    $('.header-area .main-menu').addClass('navbar_fixed');
                } else {
                    $('.header-area .main-menu').removeClass('navbar_fixed');

                }
            })
        }
    }

    navBarFixed();


});