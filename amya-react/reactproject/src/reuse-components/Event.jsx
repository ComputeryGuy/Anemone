import React from 'react'

class Event extends React.Component {
	render () {
		return (
			<div class="a-event">
				<h4>{this.props.eventName}</h4>
				<p>{this.props.myTime} | {this.props.myDate}</p>
			</div>
		);
	}
}

export default Event;