
// OLD
$(document).ready(function () {

	/* =================== MOVE TASK CARD =================== */
	// tasks can only move between 'to do', 'in progress', and 'completed'
	$(".column.move").sortable ({
		cursor: 'move',
		connectWith: '.column.move'
	});

	/* =================== SHOW AND HIDE TASK INFORMATION =================== */
	$(".a-task").click(
		function (e) { 
			e.preventDefault();
			
			// if the task does NOT have the class 'unclaimed'
			if ( !$(this).hasClass("unclaimed")){
				alert("this does not have the class 'unclaimed' ")
			}
		}
	);

	/* =================== GET USER BID =================== */
	$("#bid").on("keypress", 
		function (e) {
			// on enter
			if(e.which == 13) {
				// if the input is NOT empty
				if ( $("#bid").val().length != 0) {

					var user_bid = $("#bid").val();
					alert("User bid: " + user_bid)
				}
			}
		}
	);

	/* =================== SHOW AND HIDE CREATE TASK FORM =================== */
	// make the Add Task button show the form (= slide in)
	$(".right-buttons-container .button.right").click(
		function (e) {
			e.preventDefault();
			$("#form-container").show({
				duration: '1000'
			});
		}
	);

	// make the x on the form close the form (= slide out)
	$("#exit-btn").click(function (e) { 
		e.preventDefault();
		$("#form-container").hide({
			duration: '1000'
		});
	});

	/* =================== ADD SUB TASK =================== */
	// if the user presses the 'enter' key
	$("#sub_task_text").on("keypress", 
		function (e) {
			e.preventDefault();

			// in ascii the 'enter' key is 13
			if (e.which == 13) {
				
				// if the input is not empty
				if ( $("#sub_task_text").val().length != 0 ) {

					// show sub-task container
					$(".task-container").show();
	
					var x = $(".task-container").html();
					var y = '<div class="sub-task">' 
								+ $("#sub_task_text").val()
							+ '</div>';
	
					$(".task-container").html(x + y);
					$("#sub_task_text").val("");
				}
			}
		}
	);

	// if the user clicks on the add subtask btn
	$(".add-sub-task-btn").click(
		function (e) { 
			e.preventDefault();

			// show sub-task container
			$(".task-container").show();
			
			if ( $("#sub_task_text").val().length != 0 ) {

				var x = $(".task-container").html();
				var y = '<div class="sub-task">' 
							+ $("#sub_task_text").val()
						+ '</div>';

				$(".task-container").html(x + y);
				$("#sub_task_text").val("");
			}
			// else {
			// 	alert ("Enter some text!!!");
			// }
		}
	);

	/* =================== RETURN TODAY'S DATE =================== */
	// make 'Created: XX/XX/XXXX' is always set to today's date (note the following code is JS)

	var d = new Date(); // creates a date object
	var month = d.getMonth()+1; // gets the month
	var day = d.getDate(); // gets the day
	// concats them together
	var newOutput =  ((''+month).length<2 ? '0' : '') + month + '/' +
	((''+day).length<2 ? '0' : '') + day  + '/' +
	d.getFullYear();


	// returns the variable. If the output is not working would show 'today's date here'
	$("#todays-date").html(newOutput);
	
	/* =================== SHOW NUMBER OF DAYS LEFT BEFORE DUE DATE =================== */
	// TODO: here

	$("#end_date").change(
		function (e) { 
			e.preventDefault();
			var due_date = $("#end_date").val();

			var input_date = new Date(due_date);

			// calcuate the difference in number of days between

			// To calculate the time difference of two dates
			var Difference_In_Time = input_date.getTime() - d.getTime();
			
			// To calculate the no. of days between two dates
			var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);

			// round up then +1
			var result = Math.ceil(Difference_In_Days) + 1;
			
			$("#total-days").html(result);
		}
	);
	

	/* =================== SHOW AND HIDE REPEAT INFORMATION ON FORM =================== */
	// if "Repeats?" is checked then show the expaned info about repeat
	$(".repeat-toggle-container #repeat_toggle").click(
		function () {
			if ( $(this).prop("checked") == true) {
				// alert ("Checkbox is checked.")
				
				// show the extra info regarding repeats
				$(".repeat-expanded").show(); 
			}
			else {			
				// hide repeat extra information
				$(".repeat-expanded").hide();
			}
	});

	/* =================== CLOSE FORM ON SUBMIT =================== */
	// make the submit button on the form close the form
	
});