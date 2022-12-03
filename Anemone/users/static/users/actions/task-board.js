	// TODO: updated to match task-board.html
	$( document ).ready(function() {

	/* =================== GETS CSRF TOKEN =================== */
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);

				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');

	/* =================== MOVE TASK CARD =================== */
	// tasks can only move between 'to do', 'in progress', and 'completed'
	$(".column.move").sortable ({
		cursor: 'move',
		connectWith: '.column.move',
		items: ".{{ user.pk }}",
		update: function(event, ui) {
			if (this === ui.item.parent()[0]) {
				var data = new Object();
				data.type = "task_move";
				data.id = ui.item.attr("id");
				data.new_pos = ui.item.parent().attr("id");
				var jsonData = JSON.stringify(data);
				$.ajax({
					type: "POST",
					url: "{% url 'taskboard' %}",
					headers: { 'X-CSRFToken': csrftoken },
					//dataType: "json",
					data: jsonData,
					contentType: "application/json",
					success: function(result) {
	//	$("#bidtext{{ task.id }}").text("Current bid: " + user_bid)
						var toDoCount = $("#to-do-column").children(".a-task").length;
						$("#to-do-total").text(toDoCount)
						var inProgCount = $("#in-prog-column").children(".a-task").length;
						$("#in-prog-total").text(inProgCount)
						var completeCount = $("#complete-column").children(".a-task").length;
						$("#complete-total").text(completeCount)
					},
					error: function(response) {
						alert("Something went wrong in processing your move.");
					}
				});
			}
		},
	});

	/* =================== GET USER BID =================== */
	{% for task in unclaimed_tasks %}
		$("#bid{{ task.id }}").on("keypress", 
			function (e) {
				// on enter
				if(e.which == 13) {
					//Ensure input is valid
					user_bid = parseInt($("#bid{{ task.id }}").val());

					if ( !Number.isInteger(user_bid) ) {
						alert("Your bid must be an integer.")
					} 
					else if ( user_bid >= {{ task.points }} && user_bid) {
						alert("Your bid must be lower than the current bid.");
					} 
					else if ( user_bid < 1 ) {
						alert("Your bid must be greater than 0")
					} 
					else { //Send payload
						var data = new Object();
						data.type = "user_bid";
						data.id = {{ task.id }};
						data.bid = user_bid;
						var jsonData = JSON.stringify(data);
						$.ajax({
							type: "POST",
							url: "{% url 'taskboard' %}",
							headers: { 'X-CSRFToken': csrftoken },
							//dataType: "json",
							data: jsonData,
							contentType: "application/json",
							success: function(result) {
								$("#bidtext{{ task.id }}").text("Current bid: " + user_bid)
							},
							error: function(response) {
								alert("Something went wrong in processing your bid.");
							}
						});
					}
				}
			}
		);
	{% endfor %}

	/* =================== SHOW AND HIDE CREATE TASK FORM =================== */
	// make the Add Task button show the form (= slide in)
	$(".right-buttons-container .button.right").click(
		function (e) {
			e.preventDefault();

			$(':input','#form-container')
				.not(':button, :submit, :reset, :hidden')
				.val('')
				.prop('checked', false)
				.prop('selected', false);

			$("#form-container").show({
				duration: '1000'
			});
		}
	);

	// make the x on the form close the form (= slide out)
	$("#exit-btn").click(function (e) { 
		e.preventDefault();

		$(':input','#form-container')
			.not(':button, :submit, :reset, :hidden')
			.val('')
			.prop('checked', false)
			.prop('selected', false);
			
		$("#form-container").hide({
			duration: '1000'
		});
	});

	/* =================== RETURN TODAY'S DATE =================== */
	// return today's date as MM/DD/YYYY
	var d = new Date(); // creates a date object
	var month = d.getMonth()+1; // gets the month
	var day = d.getDate(); // gets the day
	
	// concats them together
	var newOutput =  ((''+month).length<2 ? '0' : '') + month + '/' +
	((''+day).length<2 ? '0' : '') + day  + '/' +
	d.getFullYear();

	// returns the variable. If the output is not working would show 'today's date here'
	$("#todays-date").html(newOutput);

	// returns today's date as YYYY-MM-DD
	var maxDate = d.getFullYear() + '-' 
	+ ((''+month).length<2 ? '0' : '') + month + '-' +
	((''+day).length<2 ? '0' : '') + day;
	
	// restricts due date input to only selecting dates after today's date
	$('#end_date').attr('min', maxDate);
	
	/* =================== SHOW NUMBER OF DAYS LEFT BEFORE DUE DATE =================== */
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
});