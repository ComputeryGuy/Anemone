import React from "react"

class Button extends React.Component {
	render () {
		return (

			<div class="button-container">
				<a href="#" class="button">{this.props.buttonText}</a>
			</div>

		);
	}
}

export default Button;