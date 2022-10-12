import React from "react"

class InfoSquare extends React.Component {
	render () {
		return (
			
			<div class="info-square">
				<h1>{this.props.number}</h1>
				<h3>{this.props.subHeader}</h3>
			</div>
		);
	}

}

export default InfoSquare;