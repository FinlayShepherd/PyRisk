# Structure
## High-level
Server can be hosted on Nick's domain
* Python back-end (game logic)
* JavaScript (+ HTML/CSS) front-end (GUI)
* MySQL database

## Client-Server interaction
#### Login
* Client shows login GUI
* Username and password are sent to the server
* Server encrypts username and password and requests the encrypted details?
* If valid, logs in user and presents 'Make game/Join game' GUI
* If invalid, inform

#### Make game
* Can either select a new game or the most recent game (saved to profile?)
* Either way, new game server is started and client GUI is displayed - if most recent game, loads using saved config, if new game, loads using default config
* Client GUI lets people team up and choose colours in pre-game state

#### Join game
* Client sends join request to server
* If server has game process running (in pre-game state) then the client is allowed to join
* Client GUI lets people team up and choose colours in pre-game state

#### Gameplay
* Client shows a GUI
* Interaction with the GUI sends event to the server
* Server processes action based on event
* Server sends response to relevant* clients (* in private messages, not all clients would see an update)
* Clients update GUI based on event
Game loop checks for updates every x seconds

### Server needs to track:
* The current teams
* The current players
* The territories (includes neighbouring territories)
* The number of armies in each territory
* The player whose armies are in the territory
* The teams' mission cards
* The public messages
* The player who sent the public message
* The private messages
* The player who sent the private message
* The player/team who received the private message
* The total number of armies for each player (needs to be validated to prevent people from cheating)
* Current battle dice rolls
* The results of battles

### Client needs to track
* The current teams
* The current players
* The territories (includes neighbouring territories)
* The number of armies in each territory
* The team whose armies are in the territory
* The public messages
* The player who sent the public message
* The player who sent the private message
* The player/team who received the private message
* The total number of armies for each player (needs to be validated to prevent people from cheating)
* The results of battles

### Private info (teams)
* Mission cards
* Current army cards
* Private messages sent and received

### Public info
* The current teams
* The active team (the team whose turn it is)
* The current players
* The territories (includes neighbouring territories)
* The number of armies in each territory
* The player whose armies are in the territory
* The public messages
* The player who sent the public message
* The total number of armies for each player (needs to be validated to prevent people from cheating)
* The results of battles

## Classes
* Config - holds all information needed to instantiate board
* Board - Used to separate code out from GUI. Holds active team (whose turn it is)
* Continent - Holds territories, name of continent, current occupying teams, current bonus receiver (Team or 'contested')
* Territory - Holds number of armies, current occupying team, neighbouring territories
* Player - Holds name, ID, public messages sent?, private messages sent?, private messages received?
* Team - Holds players, colour, occupied territories, number of armies, mission card, army cards, current battle?, private messages received?
* Army card - type = 'army', army ('infantry', 'cavalry', 'artillery', 'wildcard')
* Mission card - type = 'mission', conditions
* Condition - type ('destroy', 'conquer', 'occupy'), target (if type == 'destroy' -> Team; if type == 'conquer' -> Continent; if type == 'occupy' -> Territory + number of armies
* Gui - instantiates and holds the different GUI elements
* MessagePane - GUI elements for displaying and sending messages
* MapPane - GUI for displaying and interacting with territories
* CardPane - GUI for displaying the current army cards and mission card
There are probably more GUI elements needed
