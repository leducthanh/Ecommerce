$(document).ready(function(){
	$(document).on('click','.dele-cart',function(e){
		e.preventDefault();
		var url = $(this).attr('href');
		$.ajax({
			url:url,
			type:'GET',
			success:function(res){
				$('#menu-cart').load(location.href + ' #menu-cart');
				$('#cart-cus').load(location.href + ' #cart-cus');
			}
		});

	});
	$(document).on('change', '.qty', function() {
		var qty = $(this).val();
		if (qty == '') {
			var qty = 1;
		};
		var id = $(this).attr('id'); 
		var url = id+'/'+qty;
		$.ajax({
			url:url,
			type:'GET',
			success:function(res){
				$('#menu-cart').load(location.href + ' #menu-cart');
				$('#cart-cus').load(location.href + ' #cart-cus');
			}
		});
	});
	$(document).on('change', '.size', function() {
		var size = $(this).val();
		var id = $(this).attr('id');
		var url = id+'/'+size;
		$.ajax({
			url:url,
			type:'GET',
			success:function(res){
				$('#menu-cart').load(location.href + ' #menu-cart');
				$('#cart-cus').load(location.href + ' #cart-cus');
			}
		});
	});
});
(function($) {
  $.fn.inputFilter = function(inputFilter) {
    return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function() {
      if (inputFilter(this.value)) {
        this.oldValue = this.value;
        this.oldSelectionStart = this.selectionStart;
        this.oldSelectionEnd = this.selectionEnd;
      } else if (this.hasOwnProperty("oldValue")) {
        this.value = this.oldValue;
        this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
      }
    });
  };
}(jQuery));


// Install input filters.
$(".uintTextBox").inputFilter(function(value) {
  return /^\d*$/.test(value); });
$("#intLimitTextBox").inputFilter(function(value) {
  return /^\d*$/.test(value) && (value === "" || parseInt(value) <= 500); });
$("#intTextBox").inputFilter(function(value) {
  return /^-?\d*$/.test(value); });
$("#floatTextBox").inputFilter(function(value) {
  return /^-?\d*[.,]?\d*$/.test(value); });
$("#currencyTextBox").inputFilter(function(value) {
  return /^-?\d*[.,]?\d{0,2}$/.test(value); });
$("#basicLatinTextBox").inputFilter(function(value) {
  return /^[a-z]*$/i.test(value); });
$("#extendedLatinTextBox").inputFilter(function(value) {
  return /^[a-z\u00c0-\u024f]*$/i.test(value); });
$("#hexTextBox").inputFilter(function(value) {
  return /^[0-9a-f]*$/i.test(value); });