import React from 'react'
import Notification from '../reuse-components/Notification'
import Button from '../reuse-components/Button'

import daren from '../assets/pictures/nrd-y3kC_7Qhmjk-unsplash.jpg'
import rapheal from '../assets/pictures/filippo-ruffini-6rsnRElhycs-unsplash.jpg'

class Middle extends React.Component {
	render () {
		return (
			<section class="middle-section">

				<div class="welcome-container">
					<h1>Welcome back, Lenix!</h1>
				</div>

				<div class="information-container">

					<div class="info-square-container">

						<div class="small-info-squares">

							<div class="info-square">
								<h1>100</h1>
								<h3>Total Points</h3>
							</div>

							<div class="info-square">
								<h1>3</h1>
								<h3>New Tasks</h3>
							</div>

							<div class="info-square">
								<h1>5</h1>
								<h3>Completed Tasks</h3>
							</div>

							<div class="info-square">
								<h1>40</h1>
								<h3>Points Earned Today</h3>
							</div>

						</div>

					</div>

					<div class="task-avail-container">

						<h1 id="current-points-avil">40pts</h1>
			
						<p>
							available from 6 <span class="add-blue">unclaimed</span> tasks
						</p>
			
						<Button buttonText={"go to tasks"}/>
					</div>

					<div class="recent-notifs-container">

						<div class="notifs-header">
							<h2>Recent Notifications</h2>
							<Button buttonText={"go to notifications"}/>
						</div>

						<div class="a-notification-container">
							<Notification currImage={daren}/>
							<Notification currImage={rapheal}/>
			
						</div>

						<div class="button-container mobile">
							<a class="button" href="#">go to notifications</a>
						</div>
					</div>

				</div>
			</section>
		);
	}
}

export default Middle;