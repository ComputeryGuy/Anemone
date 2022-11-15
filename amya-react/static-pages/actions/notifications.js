$(document).ready(function () {

	/* =================== ADDS SCROLL TO NOTIFS TABLE =================== */
	// get the current # of notifications/bullitens
	var notif_length = $(".todays-notification-container .a-notification").length;

	// if the curr # is greater than 3
	if (notif_length > 3) {
		$(".todays-notification-container").css("height", "69vh"); // change the height of the container
		$(".todays-notification-container").css("overflow-y", "scroll"); // change to scroll
	}
	

	/* =================== ADDS SCROLL TO COMP TASKS TABLE =================== */
	// get the current # of rows
	var table_length = $(".table .row.data").length;

	if (table_length > 4) {
		$(".row-data-container").css("height", "59vh");
		$(".row-data-container").css("overflow-y", "scroll");
	}
	

	/* =================== OPENS 'CREATE NOTIF' FORM =================== */
	// add notification btn -
	$("#add-notif-btn").click(
		function (e) { 
			e.preventDefault();
			$("#add-notif-form-container").show({
				duration: '1000'
			});
		}
	);

	/* =================== CLOSE 'CREATE NOTIF' FORM =================== */
	$("#exit-btn").click(
		function (e) { 
			e.preventDefault();
			$("#add-notif-form-container").hide({
				duration: '1000'
			});
		}
	);
});