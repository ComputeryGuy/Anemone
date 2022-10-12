import React from "react"

import Nav from './reuse-components/Nav'

// import main style -- css variables
import './styles/main-style.css'

// import tasks style -- desktop style
import './styles/tasks-style.css'


// TODO: How do you get the colour to move from dashboard to tasks?

class Tasks extends React.Component {
	render () {
		return (

			<div class="main-grid">
				<Nav />
				<h1>This is the tasks page</h1>
			</div>

		);
	}
}

export default Tasks;