$(document).ready(function () {

	/* =================== mobile sign in menu =================== */
	$("#sign-up-btn").click(
		function (e) { 
			e.preventDefault();

			// move the triangle
			$(".triangle").animate({
				marginLeft: '14.5rem',
			}, 550);

			$(".sign-in-section.mobile").hide();
			$(".create-account-section.mobile").fadeIn(549);
			
			$(".menu-list.mobile #sign-in-btn").toggleClass("current");
			$(".menu-list.mobile #sign-up-btn").toggleClass("current");
		}
	);

	$("#sign-in-btn").click(
		function (e) { 
			e.preventDefault();
			
			// move the triangle
			$(".triangle").animate({
				marginLeft: '4.5rem',
			}, 550);

			$(".create-account-section.mobile").hide();
			$(".sign-in-section.mobile").fadeIn(549);

			$(".menu-list.mobile #sign-in-btn").toggleClass("current");
			$(".menu-list.mobile #sign-up-btn").toggleClass("current");
		}
	);

	/* =================== desktop sign in menu =================== */
	$("#go-to-sign-up-btn").click(
		function (e) { 
			e.preventDefault();

			// hide elements 
			$(".sign-in-container").hide();
			$(".new-user-container").hide();
			$(".logo-container.left *").hide();

			// slide transformation
			$(".right-side").animate({
				right: '30%',
				width: '70%',
				backgroundColor: '#30353f',
				borderTopLeftRadius: '10px',
				borderTopRightRadius: '0px',
				borderBottomLeftRadius: '10px',
				borderBottomRightRadius: '0px',
			}, 550);

			$(".left-side").animate({
				left: '70%',
				width: '30%',
				backgroundColor: '#006FF2',
				borderTopLeftRadius: '0px',
				borderTopRightRadius: '10px',
				borderBottomLeftRadius: '0px',
				borderBottomRightRadius: '10px',
			}, 550);

			// show elements
			$(".logo-container.right *").fadeIn(551);

			$(".sign-up-container").css("display", "flex");
			$(".old-user-container").css("display", "flex");

			$(".sign-up-container").fadeIn(551);
			$(".old-user-container").fadeIn(551);
		}
	);


	$("#go-to-sign-in-btn").click(
		function (e) { 
			e.preventDefault();

			// hide elements
			$(".logo-container.right *").hide();
			$(".sign-up-container").hide();
			$(".old-user-container").hide();

			// slide transformation
			$(".right-side").animate({
				width: '30%',
				right: '0',
				backgroundColor: '#006FF2',
				borderTopLeftRadius: '0px',
				borderTopRightRadius: '10px',
				borderBottomLeftRadius: '0px',
				borderBottomRightRadius: '10px',
			}, 550);

			$(".left-side").animate({
				left: '0',
				width: '70%',
				backgroundColor: '#30353f',
				borderTopLeftRadius: '10px',
				borderTopRightRadius: '0px',
				borderBottomLeftRadius: '10px',
				borderBottomRightRadius: '0px',
			}, 550);

			// show elements
			$(".logo-container.left *").fadeIn(551);

			$(".sign-in-container").css("diplay", "flex");
			$(".new-container").css("diplay", "flex");

			$(".sign-in-container").fadeIn(551);
			$(".new-user-container").fadeIn(551);
		}
	);
});