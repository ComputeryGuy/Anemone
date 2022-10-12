import React from 'react'
import Event from '../reuse-components/Event'
import Button from '../reuse-components/Button'

class Right extends React.Component {
	render () {
		return (
			
			<section class="right-section">

				<div class="calendar">I am a calendar</div>

				<div class="event-container">

					<h2>Today's Events</h2>

					<Event eventName={"Event 1"} myTime={"08:00 AM - 09:00 AM"} myDate={"Thursday, Oct 6, 2022"}/>

					<Event eventName={"Event 2"} myTime={"10:00 AM - 11:00 AM"} myDate={"Thursday, Oct 6, 2022"}/>

					<Event eventName={"Event 2"} myTime={"12:00 PM - 02:00 PM"} myDate={"Thursday, Oct 6, 2022"}/>

					<Event eventName={"Event 4"} myTime={"04:00 AM - 05:00 PM"} myDate={"Thursday, Oct 6, 2022"}/>
				</div>

				<Button buttonClass={"button-container"} buttonText={"go to calendar"}/>

			</section>
		);
	}
}

export default Right;