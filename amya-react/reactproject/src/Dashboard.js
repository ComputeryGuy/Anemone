import React from "react"

import Left from './app-components/Left'
import Middle from './app-components/Middle'
import Right from './app-components/Right'

// import main style -- css variables
import './styles/main-style.css'

// import app style -- desktop style
import './styles/app-style.css'

// import app queries -- media queries for mobile and tablet
import './styles/app-queries.css'

class Dashboard extends React.Component {
	render () {
		return (
			<div class="main-grid">
				<Left />
				<Middle />
				<Right />
			</div>
		);
	}
}

export default Dashboard;