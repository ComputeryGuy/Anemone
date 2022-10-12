import React from 'react'
import logo from '../assets/icons/logo-round.png'

class Nav extends React.Component {
	render () {
		return (
			<nav id="nav-sidebar">

				<div class="logo-container">
					<img id="logo" src={logo} alt="logo"/>
				</div>

				<div class="nav-sidebar-content">
					<ul class="list">

						<li class="list-item">
							<a href="." class="nav-link desktop-current">
								<span class="material-symbols-rounded mobile-current">dashboard</span>
								<span class="link">Dashboard</span>
							</a>
						</li>

						<li class="list-item">
							<a href="./tasks.html" class="nav-link">
								<span class="material-symbols-rounded">task_alt</span>
								<span class="link">Tasks</span>
							</a>
						</li>
		
						<li class="list-item">
							<a href="." class="nav-link">
								<span class="material-symbols-rounded">calendar_month</span>
								<span class="link">Calendar</span>
							</a>
						</li>

						<li class="list-item">
							<a href="." class="nav-link">
								<span class="material-symbols-rounded">notifications</span>
								<span class="link">Notifications <span id="notif-number">5</span></span>
							</a>
						</li>

						<li class="list-item">
							<a href="." class="nav-link">
								<span class="material-symbols-rounded">leaderboard</span>
								<span class="link">Leaderboard</span>
							</a>
						</li>

						<li class="list-item mobile">
							<a href="#" class="nav-link">
								<span class="material-symbols-rounded">settings</span>
								<span class="link">Settings</span>
							</a>
						</li>

						<li class="list-item mobile">
							<a href="#" class="nav-link">
								<span class="material-symbols-rounded">logout</span>
								<span class="link">Logout</span>
							</a>
						</li>

					</ul>

					<div class="list-bottom-content">

						<li class="list-item">
							<a href="#" class="nav-link">
								<span class="material-symbols-rounded">settings</span>
								<span class="link">Settings</span>
							</a>
						</li>

						<li class="list-item">
							<a href="#" class="nav-link">
								<span class="material-symbols-rounded">logout</span>
								<span class="link">Logout</span>
							</a>
						</li>

					</div>
				</div>
			</nav>
		);
	}
}

export default Nav;