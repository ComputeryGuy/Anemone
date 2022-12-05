$(document).ready(function () {

	/* =================== CLICKING ON SETTINGS MENU =================== */
	$("#user-prof").click(
		function (e) { 
			e.preventDefault();
			$("#update-acct").removeClass("desktop-current");
			$("#del-smthing").removeClass("desktop-current");
			$(this).addClass("desktop-current");
		}
	);

	$("#update-acct").click(
		function (e) { 
			e.preventDefault();
			$("#user-prof").removeClass("desktop-current");
			$("#del-smthing").removeClass("desktop-current");
			$(this).addClass("desktop-current");
		}
	);
	$("#del-smthing").click(
		function (e) { 
			$(this).addClass("desktop-current");
			$("#user-prof").removeClass("desktop-current");
			$("#update-acct").removeClass("desktop-current");
			e.preventDefault();
		}
	);
});