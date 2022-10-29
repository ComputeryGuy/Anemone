// TODO: make it so that you can only move cards on desktop
$(document).ready(function () {

	// make is so I can move tasks around on the page
	$(".column").sortable ({
		cursor: 'move',
		connectWith: '.column'
	});

	// make the Add Task button show the form (= slide in)
	$(".right-buttons-container .button.right").click(function (e) { 
		e.preventDefault();
		$("#form-container").show({
			duration: '1000'
		});

	});

	// make the x on the form close the form (= slide out)
	$("#exit-btn").click(function (e) { 
		e.preventDefault();
		$("#form-container").hide({
			duration: '1000'
		});
	});

	// make the submit button on the form close the form -- submit does some weird stuff
	// $("#submit-btn").click(function (e) { 
	// 	e.preventDefault();
	// 	$("#form-container").hide();
	// });
	

	// if "Repeats?" is checked then show the expaned info about repeat
	$(".repeat-toggle-container #repeat_toggle").click(
		function () {
			if ( $(this).prop("checked") == true) {
				// alert ("Checkbox is checked.")

				// show the extra info regarding repeats
				$(".repeat-expanded").show(); 

				// scroll on overflow
				$(".task-form-container").css({"overflow-y":"scroll"});
			}
			else {
				$(".repeat-expanded").hide();

				// else, remove scroll bar
				$(".task-form-container").css({"overflow-y":"visible"});
			}
		}
	);
	
});