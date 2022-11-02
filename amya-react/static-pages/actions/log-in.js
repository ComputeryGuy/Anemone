
// just type "jq" to access all jQuery snippets
$(document).ready (function() {
	const signupBtn = document.querySelector('.signupBtn');
	const signinBtn = document.querySelector('.signinBtn');
	const btnBx = document.querySelector('.right-section');
	const signinBx = document.querySelector('.sign-in-section');
	const signupBx = document.querySelector('.sign-up-section');
	const signupBtnBx = document.querySelector('.new-user-container');

	function delay(milliseconds){
		return new Promise(resolve => {
			setTimeout(resolve, milliseconds);
		});
	}

	signupBtn.onclick = async function() {
		btnBx.classList.add('active');
		signinBx.classList.add('none');
		await delay(550);
		signupBx.classList.remove('none');
	}

	signinBtn.onclick = async function() {
		btnBx.classList.remove('active');
		signupBx.classList.add('none');
		signupBtnBx.classList.add('none');
		await delay(550);
		signinBx.classList.remove('none');
		signupBtnBx.classList.remove('none');
	}

	
});