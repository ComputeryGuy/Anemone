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

			// on open reset form values to default
			$(':input','#add-notif-form-container')
				.not(':button, :submit, :reset, :hidden')
				.val('')
				.prop('checked', false)
				.prop('selected', false);
			
			$("#add-notif-form-container").show({
				duration: '1000'
			});
		}
	);

	/* =================== CLOSE 'CREATE NOTIF' FORM =================== */
	$("#exit-btn").click(
		function (e) { 
			e.preventDefault();

			// on exit reset form values to default
			$(':input','#add-notif-form-container')
				.not(':button, :submit, :reset, :hidden')
				.val('')
				.prop('checked', false)
				.prop('selected', false);
			
			$("#add-notif-form-container").hide({
				duration: '1000'
			});
		}
	);

	/* =================== RESTRICT DUE DATE =================== */
	// return today's date as MM/DD/YYYY
	var d = new Date(); // creates a date object
	var month = d.getMonth()+1; // gets the month
	var day = d.getDate(); // gets the day

	// returns today's date as YYYY-MM-DD
	var maxDate = d.getFullYear() + '-' 
	+ ((''+month).length<2 ? '0' : '') + month + '-' +
	((''+day).length<2 ? '0' : '') + day;

	// restricts due date input to only selecting dates after today's date
	$('#notif-deadline').attr('min', maxDate);

});