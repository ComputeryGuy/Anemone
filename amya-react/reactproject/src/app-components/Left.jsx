import React from "react";

// import navigation componenet
import Nav from '../reuse-components/Nav'

class Left extends React.Component {
	render () {
		return (
			<section class="left-section">
				<Nav />
			</section>
		);
	}
}

export default Left;