$(document).ready(function () {

	/* =================== SELECTED 'CREATE HOUSEHOLD' =================== */
	// if create pin is selected
	$("#create-sel").click(
		function (e) { 
			e.preventDefault();

			$("#select_form").hide();

			// reset view
			$("#gen-pin-btn").show();
			$(".your-pin-container").hide();
			$(".go-to-dash").hide();
			
			// change position of .woops
			$(".woops").css("right", "1.5rem");
<<<<<<< HEAD
			$(".woops").css("left", "83%");
=======
			$(".woops").css("left", "80%");
>>>>>>> master
			
			// show the container
			$(".create-selected-container").show();
		
		}
	);

	/* =================== SELECTED 'JOIN HOUSEHOLD' =================== */
	// if join household is selected
	$("#join-sel").click(
		function (e) { 
			e.preventDefault();
			$("#select_form").hide();
			$(".join-selected-container").show();
		}
	);

	/* =================== GENERATE HOUSEHOLD ACTION =================== */
	// click generate pin button
	$("#gen-pin-btn").click(
		function (e) { 
			e.preventDefault();

			// hide generate pin button
			$("#gen-pin-btn").hide();

			// hide go back button
			$(".woops").hide();

			// show load animation for 4s, then fade out
			$(".load-animation-container").show().delay(4000).fadeOut();
			// $(".load-animation-container").show();

			// hide your pin container for 5s then fade in
			$(".your-pin-container").hide().delay(5000).fadeIn();

			// change position of .woops
<<<<<<< HEAD
			$(".woops").css("right", "83%");
=======
			$(".woops").css("right", "80%");
>>>>>>> master
			$(".woops").css("left", "1.5rem");

			$(".woops").hide().delay(6000).fadeIn();

			
			// show go to dash
			$(".go-to-dash").hide().delay(6000).fadeIn();
		
		}
	);

	/* =================== GO BACK BUTTON =================== */
	$(".woops button").click(
		function (e) { 
			e.preventDefault();

			$("#select_form").show();
			$(".create-selected-container").hide();
			$(".join-selected-container").hide();
		}
	);

});