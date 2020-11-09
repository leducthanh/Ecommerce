$(document).ready(function(){

	$('.add-cart').click(function(e){
		e.preventDefault();
		if ($(this).hasClass('disable')) {
			return false;
		};
		$(document).find('.add-cart').addClass('disable');
		var url = $(this).attr('href');
		var parent = $(this).parents('.product');
		var src = parent.find('img').attr('src');
		var cart = $("#cart-fly").position();
		var icon = $("#cart-fly-icon").position();
		var parTop = parent.offset().top;
		var parLeft = parent.offset().left;
		$.ajax({
			url:url,
			type:'GET',
			success:function(res){
				$('#menu-cart').load(location.href + ' #menu-cart');
			}
		});
		$('<img />',{
			class: 'product-img-fly',
			src: src
		}).appendTo('body').css({
			'top' : parTop,
			'left' : (parseInt(parLeft) + parseInt(parent.width())) - 50
		});
		setTimeout(function(){
			$(document).find('.product-img-fly').css({
				'top' : cart.top,
				'left' : cart.left + icon.left +30
			});
			setTimeout(function(){
				$(document).find('.product-img-fly').remove();
				$(document).find('.add-cart').removeClass('disable');
			},1000);
		},500);
	});
	$('.dele-cart-top').click(function(e){
		e.preventDefault();
		var url = $(this).attr('href');
		$.ajax({
			url:url,
			type:'GET',
			success:function(res){
				$('#menu-cart').load(location.href + ' #menu-cart');
			}
		});
	});
	$(document).on('click','.dele-cart-top',function(e){
		e.preventDefault();
		var url = $(this).attr('href');
		$.ajax({
			url:url,
			type:'GET',
			success:function(res){
				$('#menu-cart').load(location.href + ' #menu-cart');
			}
		});
	});
});


