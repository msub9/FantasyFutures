# FantasyFutures
About FantasyFutures


        FantasyFutures is a project aiming to bridge the gap between the everyday fantasy football player and high quality, advanced statistical analysis. 


At its core, fantasy football is a game of high variance, asset management, and trend examination. To gain a deeper understanding of winning strategies and football players, fantasy football managers must dig beyond the basic stats and projections made available on mainstream fantasy platforms such as ESPN, Sleeper, and Yahoo. These projections are often unreliable and based on statistics/formulas that do not capture the nuance of football. On top of that, their formulas are not made available for the general public to analyze and improve. FantasyFutures solves this by providing advanced football statistics to fantasy football managers via streamlined, easy-to-use interfaces with stats and mathematically calculated grades that strongly correlate to fantasy performance.


The use of advanced analytics in fantasy football is far from groundbreaking. However, there currently is no website that offers a vast database of constantly-updated advanced football statistics (for free) while also prioritizing access to newer and more inexperienced fantasy newbies. Gaining knowledge on advanced stats and where to find them is difficult; With its detailed stat collections and searchable interface, FantasyFutures is a one-stop-shop for weekly and seasonal insights into YOUR players (via the import league feature) as well as the whole league.


Built With


        FantasyFeatures’s webpage was built with Flask, and utilizes Python. Data provided by Pro-Football-Reference.com and DailyRoto was used to generate the advanced statistics stored in FantasyFeatures’s databases. Logo was made using Figma.


Getting Started


        On the home page, you can navigate to any of the other pages using the buttons at the top of the header. Feel free to sign up for an account or log in to an existing account here. From there, you can go to the “Weekly Insights” page, which shows you the top players for the next week, or the “Analyze” page, which allows you to search up a player to get various advanced statistics (including our grades on the main four situational aspects).
Usage


        FantasyFeatures has many uses.Its primary feature is to be used to view your players’ stats and FantasyFeatures grades, as well as provide deeper statistical analysis on available free agents and their coming matchups. FantasyFeatures can also be used as a guide on players trending upwards and downwards statistically, and to view every football players’ advanced statistics. In the future, we hope to incorporate an import league feature which accesses all the data from your league specifically and provides user-specific insights.


Contributions


        FantasyFeatures was developed by Pranav Devabhaktuni, Mithun Subhash, Adi Gupta, and Arjun Birthi. Research on advanced football statistics and its correlation with fantasy production by Kenny Hyttenhove was kept in mind when developing the FantasyFeatures grading algorithms. Statistics were provided by Pro-Football-Reference.com and DailyRoto.


Definitions
Rank = Fantasy Ranking by Pro-Football-Reference.
PlayerName = Name of the player.
Team = Team that the player plays on.
Position = Primary position of player on the team.
Age = Age of player.
GamesPlayed = Number of games played by player.
GamesStarted = Number of games started by player.
CompletedPasses = Number of passes that was completed by the quarterback of the team.
AttemptedPasses = Number of passes attempted by quarterback of the team.
PassingYards = Number of yards gained by passing the football from the quarterback to various other players.
PassingTouchdowns = Touchdowns earned by passing the football from the quarterback to a player in or who runs into the endzone.
Interceptions = Number of times that the quarterback throws a ball that results in a catch by a player of the opposing team.
RushAttempts = Number of times that a player/team has attempted to rush in a game.
RushYards = Number of yards gained by rushing the ball.
YardsPerRush = Number of yards gained on average each time that a player/team tries rushing the ball.
RushingTouchdowns = Number of touchdowns earned by rushing the ball into the endzone.
Targets = Number of times the ball was thrown at the player by the quarterback.
Receptions = Number of times that the player got possession of the ball after being thrown at.
ReceivingYards = Number of yards that the player gains by receiving the ball (and running after the reception).
YardsPerReception = How many yards the player gains on average for each reception that they get.
ReceivingTouchdowns = Number of touchdowns the player earns by receiving the ball.
Fumbles = Number of times that a player fumbles, or loses control of the ball and has it picked up by another player.
FL = Fumbles Lost, or the number of fumbles by a player that results in the other team getting control of the ball.
TotalTouchdowns = Total touchdowns, whether receiving or rushing, made by a player or team.
2PM = 2 point conversion made after a touchdown.
2PP = Number of 2 point plays attempted after a touchdown.
FantPt = Number of fantasy points projected by the player.
PPR = Points per reception. This is a popular type of fantasy league scoring setting, where each reception by a player is awarded with an extra point.
DKPt = DraftKings Points. This is a representation of the number of points a player earns in DraftKings settings.
FDPt = FanDuel Points. This is a representation of the number of points a player earns in FanDuel settings.
VBD = Value Based Drafting. This is a strategy which assigns values to players based on how much fantasy output they provide as opposed to a replacement level player.
PositionRank = Rank when compared only to other players in the same position as the player.
OverallRank = Rank when compared to all players.
-9999 = Unique identifier for every player.
Opportunities = Chances that a player has to make a play with the ball.
RedZone = Area within 20 yards of the end zone, or touchdown area.
MarketShare = Percentage of the “market” of something. Ex. RedZone Opportunity Market Share, Red Zone Target Market Share.
RedZoneMarketShare = Market share of Red Zone opportunities.
RedZoneTargets = Number of targets in the Red Zone.
RedZoneCarries = Number of times the player carried the ball in the Red Zone.
MarketShareCarries = Market share of all carries made by the team.
Snaps = Number of times that the ball was “snapped” back. In other words, number of plays ran by the player or in the game.
TeamSnaps = Total number of snaps in the game, also all the snaps played by the team.
SnapPercent = Percentage of all team snaps played by the player.
SnapsPerGame = Average number of snaps played in one game by a player. This is in the form of a percent of the total team snaps.
RushPercent = Percent of plays that the team rushes.
TargetPercent = Percent of plays that the player is targeted on.
ReceptionRate = Rate of receptions over a number of targets.
YardsPerTarget = Number of yards gained by the player for every target that the player gets.
PasserRating = A metric based on various percentages of the quarterback that represents the strength of the passer.
Y/G = Yards per game. How many yards were produced by the player. Can be specified to be rushing yards per game or air/receiving yards per game.
Our own terminology:
* Player Score = Grades player attributes including snap share, total snap ranking, target share, average targets, yards per catch, red zone target share, rushing yards per game, and receiving yards per game.
* Quarterback Score = Grades player attributes based on the level of their quarterback. This includes their quarterback’s passer rating, yards per pass attempted, and completion percentage.
* Team Score = Grades player attributes based on the strength of the team’s offense and situation. Includes statistics such as team red zone scoring attempts per game, team PPG (points per game), team rushing yards per game, team receiving yards per game, and point differential.
* Opposing Team Score = Grades player attributes based on the matchup ahead. Utilizes stats of the opposing team’s defense, including PPG allowed, rushing yards allowed (for running backs), receiving yards allowed (for wide receivers and tight ends), blitz percentage, and pressure percentage.
We believe that these four aspects, together, can show us all the aspects surrounding a player.
