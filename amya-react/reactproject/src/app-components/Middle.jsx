import React from 'react'
import Notification from '../reuse-components/Notification'
import Button from '../reuse-components/Button'
import InfoSquare from '../reuse-components/InfoSquare'

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

							<InfoSquare number={"100"} subHeader={"Total Points"} />

							<InfoSquare number={"3"} subHeader={"New Tasks"} />

							<InfoSquare number={"5"} subHeader={"Completed Tasks"} />

							<InfoSquare number={"40"} subHeader={"Points Earned Today"} />

						</div>

					</div>

					<div class="task-avail-container">

						<h1 id="current-points-avil">40pts</h1>
			
						<p>
							available from 6 <span class="add-blue">unclaimed</span> tasks
						</p>
			
						<Button buttonClass={"button-container"} buttonText={"go to tasks"}/>
					</div>

					<div class="recent-notifs-container">

						<div class="notifs-header">
							<h2>Recent Notifications</h2>
							<Button buttonClass={"button-container"} buttonText={"go to notifications"}/>
						</div>

						<div class="a-notification-container">
							<Notification currImage={daren}/>
							<Notification currImage={rapheal}/>
			
						</div>

						<Button buttonClass={"button-container mobile"} buttonText={"go to notifications"}/>
					</div>

				</div>
			</section>
		);
	}
}

export default Middle;