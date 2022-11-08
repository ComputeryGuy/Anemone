$(document).ready(function () {

	$("#go-to-sign-up-btn").click(function (e) { 
		e.preventDefault();

		// hide the shadow
		$(".log-in-container").css("box-shadow", "none");

		// hide elements 
		$(".sign-in-container").hide();
		$(".new-user-container").hide();
		$(".logo-container.left *").hide();

		// slide transformation
		$(".right-side").animate({
			right: '26rem',
			width: '50rem',
			backgroundColor: '#30353f',
			borderTopLeftRadius: '10px',
			borderTopRightRadius: '0px',
			borderBottomLeftRadius: '10px',
			borderBottomRightRadius: '0px',
		}, 550);

		$(".left-side").animate({
			left: '50rem',
			width: '26rem',
			backgroundColor: '#006FF2',
			borderTopLeftRadius: '0px',
			borderTopRightRadius: '10px',
			borderBottomLeftRadius: '0px',
			borderBottomRightRadius: '10px',
		}, 550);

		// show elements
		$(".logo-container.right *").fadeIn(550);
		$(".sign-up-container").fadeIn(550);
		$(".old-user-container").fadeIn(550);

		// show box shadow after 550 delay
		$(".log-in-container").delay(550).fadeIn( 
			function(e) {
				$(this).css("box-shadow"," 0px 4px 20px 0px rgba(0, 0, 0, 45%)");
			}
		);
	});


	$("#go-to-sign-in-btn").click(function (e) { 
		e.preventDefault();

		// hide the shadow
		$(".log-in-container").css("box-shadow", "none");

		// hide elements
		$(".logo-container.right *").hide();
		$(".sign-up-container").hide();
		$(".old-user-container").hide();

		// slide transformation
		$(".right-side").animate({
			width: '26rem',
			right: '0rem',
			backgroundColor: '#006FF2',
			borderTopLeftRadius: '0px',
			borderTopRightRadius: '10px',
			borderBottomLeftRadius: '0px',
			borderBottomRightRadius: '10px',
		}, 550);

		$(".left-side").animate({
			left: '0rem',
			width: '50rem',
			backgroundColor: '#30353f',
			borderTopLeftRadius: '10px',
			borderTopRightRadius: '0px',
			borderBottomLeftRadius: '10px',
			borderBottomRightRadius: '0px',
		}, 550);

		// show elements
		$(".logo-container.left *").fadeIn(550);
		$(".sign-in-container").fadeIn(550);
		$(".new-user-container").fadeIn(550);

		// show box shadow after 550 delay
		$(".log-in-container").delay(550).fadeIn( 
			function(e) {
				$(this).css("box-shadow"," 0px 4px 20px 0px rgba(0, 0, 0, 45%)");
			}
		);
	});
});