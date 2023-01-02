# Phourtnight
<!-- Breif description of the project -->
**Phourtnight** is a web-based application that allows roommates to create and manage tasks and notifications using our gameification feature. A live demo can be found [here](https://youtu.be/EuGNqnLFR6w).

## Table of Contents
- [General Information](https://github.com/LenixC/Anemone/edit/master/Readme.md#general-information)
- [Technology Used](https://github.com/LenixC/Anemone/edit/master/Readme.md#technology-used)
- [Features](https://github.com/LenixC/Anemone/edit/master/Readme.md#features)
- [Screenshots](https://github.com/LenixC/Anemone/edit/master/Readme.md#screenshots)
- [Installation](https://github.com/LenixC/Anemone/edit/master/Readme.md#installation)
- [Game Guide](https://github.com/LenixC/Anemone/edit/master/Readme.md#game-guide)
- [Project Status](https://github.com/LenixC/Anemone/edit/master/Readme.md#project-status)
- [Acknowledgements](https://github.com/LenixC/Anemone/edit/master/Readme.md#acknowledgements)

### General Information
<!-- What is the purpose of your project? -->
Phourtnight is a collaborative game that may be played with any number of people who share a house. The purpose of the game is to accumulate points by completing tasks, levelling up, and obtaining lootboxes containing special rewards.

### Technology Used
- Django - version 4.1.4
- HTML
- CSS
- jQuery
- AJAX

### Features
- Create a household for you and your roommates to join.
- Create, assign, and manage tasks within your household.
- Create notifications for all roommates to see.
- Track the winning roommate during the current fortnight on the leaderboard.
- Obtain fun lootboxes with a "noun-adjective" pair as an incentive to compete and complete tasks against roommates.

### Screenshots
<img width="1425" alt="Landing" src="https://user-images.githubusercontent.com/65798231/210187109-c0967bac-194d-45c6-986c-b7647c6a1729.png">

### Installation
In order to access our application, please first navigate to the following link: [here](http://phourtnight-dev.us-west-2.elasticbeanstalk.com/login/). Upon loading the page, please create an account and log-in with your username and password.

### Game Guide
#### Task Creation
Members of the household create tasks that must be completed. Every member of the household can see craeted tasks and will be found in the "Uncalimed" column on the task board. From here, every member can bid.

#### Bidding
Members bid the lowest number of points they are willing to complete a task for. After 24 hours the task is assigned to the lowest bidder. If no one bids, the task is assigned at random.

#### Obtaining Points
Once a member is assigned a task, the now claimed task will show in the "To Do" column of the task board. Once a member has started a task, only they can move the task from the "To Do" column to the "In Progress" column. This will help members keep track of the tasks currently being completed. Members have until the specified deadline to compelete tasks. Upon completion, the member who claimed the task can drag-and-drop the task into the "Completed" column and are awared points accordingly.

All tasks on the task board are visible to all members in the household.

Points gained over the course of a two week period - a Phourtnight - will show in the leaderboard. The member with the most points at the end wins the Phourtnight.

#### Kudos
In addition, members can award other members in their household with points for actions they deem beneficial, wheither that be acts of kindness, short notice favours, or anything else.

#### Levelling Up
When a member gains enough points, they level up. A member who has levelled up will gain a lootbox which contains a "noun-adjective" pair. These pairs will be found in the settings page and can be used for customisation options which will be displayed on the members's leaderboard. The more a member levels up, the more lootboxes a member receives, and the more customisation options a member unlocks.

### Project Status
This project was **completed** on December 5th, 2022. 

### Acknowledgements 
- Many thanks to all the teammembers in KALPY Tech. for the dedicated efforts in completing this project.
- **Phourtnight** by KALPY Tech. is licensed under CC BY-NC-SA 4.0.
- Please note, the project **Phourtnight** has no claim or association to the game "Fortnight" created and licensed by Epic Games.
