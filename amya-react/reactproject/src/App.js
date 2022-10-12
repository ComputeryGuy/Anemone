import React from 'react'

import Dashboard from './Dashboard'
import Tasks from './Tasks'

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

function App () {
	return (
		<Router>
			<Switch>
				<Route exact path="/" component={Dashboard}/>
				<Route exact path="/tasks" component={Tasks}/>
			</Switch>
		</Router>
	);
}

export default App;