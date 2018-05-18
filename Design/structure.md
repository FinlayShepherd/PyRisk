# Structure
## High-level
* Python back-end (game logic)
* JavaScript (+ HTML/CSS) front-end (GUI)

## Client-Server interaction
* Client shows a GUI
* Interaction with the GUI sends event to the server
* Server processes action based on event
* Server sends response to relevant* clients (* in private messages, not all clients would see an update)
* Clients update GUI based on event

### Server needs to track:
* The current teams
* The current players
* The territories (includes neighbouring territories)
* The number of troops in each territory
* The player whose troops are in the territory
* The teams' mission cards
* The public messages
* The player who sent the public message
* The private messages
* The player who sent the private message
* The player/team who received the private message
* The total number of troops for each player (needs to be validated to prevent people from cheating)
* Current battle dice rolls
* The results of battles

### Client needs to track
* The current teams
* The current players
* The territories (includes neighbouring territories)
* The number of troops in each territory
* The team whose troops are in the territory
* The public messages
* The player who sent the public message
* The player who sent the private message
* The player/team who received the private message
* The total number of troops for each player (needs to be validated to prevent people from cheating)
* The results of battles

### Private info (teams)
* Mission cards
* Current army cards
* Private messages sent and received

### Public info
* The current teams
* The current players
* The territories (includes neighbouring territories)
* The number of troops in each territory
* The player whose troops are in the territory
* The public messages
* The player who sent the public message
* The total number of troops for each player (needs to be validated to prevent people from cheating)
* The results of battles

## Classes
* Config - holds all information needed to instantiate board
* Board - Used to separate code out from GUI
* Continent - Holds territories, name of continent, current occupying team, current bonus receiver (Team or 'contested')
* Territory - Holds number of troops, current occupying team, neighbouring territories
* Player - Holds name, ID, public messages sent?, private messages sent?, private messages received?
* Team - Holds players, colour, occupied territories, number of troops, mission card, army cards, current battle?, private messages received?
* Army card - type = 'army', troop ('infantry', 'cavalry', 'artillery', 'wildcard')
* Mission card - type = 'mission', conditions
* Condition - type ('destroy', 'conquer', 'occupy'), target (if type == 'destroy' -> Team; if type == 'conquer' -> Continent; if type == 'occupy' -> Territory + number of troops
* Gui - instantiates and holds the different GUI elements
* MessagePane - GUI elements for displaying and sending messages
* MapPane - GUI for displaying and interacting with territories
* CardPane - GUI for displaying the current army cards and mission card
There are probably more GUI elements needed
