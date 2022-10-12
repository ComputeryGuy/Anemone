import React from 'react'

class Notification extends React.Component {
	render () {
		return (
			<div class="a-notification">
				<div class="user-profile">
					<img src={this.props.currImage}/>
					<p class="user-name">Daren</p>
				</div>

				<div class="user-post">
					<p class="time-date-header">Posted: <span class="notif-style">07:50 AM | Wednesday, October 5, 2022</span></p>
					<h3 class="notif-title">My Parents are Coming</h3>
					<p class="notif-body">
						My parents are coming in from Oregon this weekend.
						We'll be visiting the apartment around noon to drop by and say hello.
					</p>
				</div>
			</div>
		);
	}
}


export default Notification;