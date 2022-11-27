$(document).ready(function () {

	// reference: https://codepen.io/indamix/pen/AJNazx

	/* requestAnimationFrame polyfill */
	(function(w) {
		var lastTime = 0,
			vendors = ['webkit', /*'moz',*/ 'o', 'ms'];

		for (var i = 0; i < vendors.length && !w.requestAnimationFrame; ++i) {
			w.requestAnimationFrame = w[vendors[i] + 'RequestAnimationFrame'];
			w.cancelAnimationFrame = w[vendors[i] + 'CancelAnimationFrame']
				|| w[vendors[i] + 'CancelRequestAnimationFrame'];
		}

		if (!w.requestAnimationFrame)
			w.requestAnimationFrame = function(callback, element) {
				var currTime = +new Date(),
					timeToCall = Math.max(0, 16 - (currTime - lastTime)),
					id = w.setTimeout(function(){ callback(currTime + timeToCall) }, timeToCall);
				lastTime = currTime + timeToCall;
				return id;
			};

		if (!w.cancelAnimationFrame)
			w.cancelAnimationFrame = function(id){
			clearTimeout(id);
		};
	})(this);

	/* Slot Machine */
	var noun = 'noun';
	$(noun).css({
		"color":"transparent",
		"text-shadow": "0 0 8px #000",
	});
	
	var adjective = 'adjective'
	var sm = (function (undefined) {

		var tMax = 3000, // animation time, ms
			height = 210,
			speeds = [100],
			r = [],
			reels = [
				['a', noun],
				['d', adjective],
				['g', 'h']
			],
			$reels, $msg,
			start;

		function init(){
			$reels = $('.reel').each(function(i, el){
				el.innerHTML = '<div><p>' + reels[i].join('</p><p>') + '</p></div><div><p>' + reels[i].join('</p><p>') + '</p></div>'
			});

			// $msg = $('.msg');

			$('button').click(action);
		}

		function action() {
			if (start !== undefined) return;

			for (var i = 0; i < 2; ++i) {
				// actually randomises the result
				// speeds[i] = Math.random() + .5;	
				// r[i] = (Math.random() * 3 | 0) * height / 3;

				// will always land on the same text (just changes the speed)
				speeds[i] = 2 + .5;	
				r[i] = (2 * 2 | 0) * height / 2;
			}
			// $msg.html('Spinning...');
			animate();
		}

		function animate (now) {
			if (!start) {start = now;}
			var t = now - start || 0;

			for (var i = 0; i < 2; ++i) {
				$reels[i].scrollTop = (speeds[i] / tMax / 2 * (tMax - t) * (tMax - t) + r[i]) % height | 0;
			}
			if (t < tMax) {
				requestAnimationFrame(animate);
			}

			else {
				start = undefined;
				check();
			}
		}

		return {init: init}

	})();

	$(sm.init);
});