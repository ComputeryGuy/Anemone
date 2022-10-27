// TODO: make it so that you can only move cards on desktop
$(document).ready(function () {
	$(".column").sortable ({
		cursor: 'move',
		connectWith: '.column'
	});
});