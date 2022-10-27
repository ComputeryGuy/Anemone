// $(document)ready ... = prevents any jQuery code from running before the document finishes loading
$(document).ready(function () {



	// while holding the mouse down on a task...
	$(".a-task").mousedown(function () { 
		$(this).draggable({
			containment: ".task-column-container",
			snap: '.column',
			cursor: 'move'
		});
	});

	// when I un-hold the task...
	$(".a-task").mouseup(function () { 
		
	});

	// can sort the tasks
	$(".column").sortable ({
		cursor: 'move'
	});
});