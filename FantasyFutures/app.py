from flask import Flask, render_template
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/index.html')
def toHome():  # put application's code here
    return render_template('index.html')

@app.route('/weeklyInsights.html')
def weeklyInsights():
  return render_template('weeklyInsights.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/analyze.html')
def analyze():
    return render_template('analyze.html')

import pandas as pd

#Importing CSVs
df = pd.read_csv('FantasyRankings2.csv')
df_teams = pd.read_csv('TeamDefenses.csv')

#Dropping useless columns, replacing NaN data with 0s
#Filtering players by those who actively participate in the NFL
df = df.drop(['2PM', '2PP','-9999'], axis=1)
df.fillna(0)
df = df.loc[(df['GamesStarted'] > 0)]


#Returns a player's personal score
#Broken up into three categories - WR, RB, TE, each weighted separately

def getPlayerScore(playerName):
    player = df.loc[df['PlayerName'] == playerName]
    player = player.iloc[0]
    player_projection = 0
    if player['Position'] == 'WR':
        #SnapShare% Algorithm Values for WRs
        if player['SnapPercent'] > .95:
            player_projection+=5*.125
        elif player['SnapPercent'] > .93:
            player_projection+=4*.125
        elif player['SnapPercent'] > .89:
            player_projection+=3*.125
        elif player['SnapPercent'] > .80:
            player_projection+=2*.125
        elif player['SnapPercent'] > .70:
            player_projection+=1*.125
        #TotalSnaps Algorithm Values for WRs
        totalSnaps = df.sort_values(by=['Snaps'], ascending=False)
        totalSnaps = totalSnaps.loc[df['Position'] == 'WR']
        if player['PlayerName'] in totalSnaps.iloc[:7].values:
            player_projection+=5*.175
        elif player['PlayerName'] in totalSnaps.iloc[:13].values:
            player_projection+=4*.175
        elif player['PlayerName'] in totalSnaps.iloc[:24].values:
            player_projection+=3*.175
        elif player['PlayerName'] in totalSnaps.iloc[:32].values:
            player_projection+=2*.175
        elif player['PlayerName'] in totalSnaps.iloc[:40].values:
            player_projection+=1*.175
        #TargetShare Algorithm Values for WRs
        if player['TargetPercent'] >= .3:
            player_projection+=5*.125
        elif player['TargetPercent'] >= .27:
            player_projection+=4*.125
        elif player['TargetPercent'] >= .245:
            player_projection+=3*.125
        elif player['TargetPercent'] >= .2:
            player_projection+=2*.125
        elif player['TargetPercent'] >= .16:
            player_projection+=1*.125
        #TargetAverage Algorithm Values for WRs
        player["TargetAverage"] = player['Targets']/player['GamesStarted']
        if player['TargetAverage'] >= 12:
            player_projection+=5*.3
        elif player['TargetAverage'] >= 10:
            player_projection+=4*.3
        elif player['TargetAverage'] >= 7.75:
            player_projection+=3*.3
        elif player['TargetAverage'] >= 7:
            player_projection+=2*.3
        elif player['TargetAverage'] >= 6:
            player_projection+=1*.3
        #RedzoneTargetShare Algorithm Values for WRs
        if player['RedZoneTargetShare'] >= .375:
            player_projection+=5*.075
        elif player['RedZoneTargetShare'] >= .305:
            player_projection+=4*.075
        elif player['RedZoneTargetShare'] >= .25:
            player_projection+=3*.075
        elif player['RedZoneTargetShare'] >= .15:
            player_projection+=2*.075
        elif player['RedZoneTargetShare'] >= .10:
            player_projection+=1*.075
        #YardsPerGame Algorithm Values for WRs
        player["YardsPerGame"] = player['ReceivingYards']/player['GamesStarted']
        if player['YardsPerGame'] >= 100:
            player_projection+=5*.2
        elif player['YardsPerGame'] >= 80:
            player_projection+=4*.2
        elif player['YardsPerGame'] >= 65:
            player_projection+=3*.2
        elif player['YardsPerGame'] >= 52.5:
            player_projection+=2*.2
        elif player['YardsPerGame'] >= 45.5:
            player_projection+=1*.2
    elif player['Position'] == 'RB':
        #SnapShare% Algorithm Values for RBs
        if player['SnapPercent'] > .95:
            player_projection+=5*.25
        elif player['SnapPercent'] > .93:
            player_projection+=4*.25
        elif player['SnapPercent'] > .89:
            player_projection+=3*.25
        elif player['SnapPercent'] > .80:
            player_projection+=2*.25
        elif player['SnapPercent'] > .70:
            player_projection+=1*.25
        #TotalSnaps Algorithm Values for RBs
        totalSnaps = df.sort_values(by=['Snaps'], ascending=False)
        totalSnaps = totalSnaps.loc[df['Position'] == 'RB']
        if player['PlayerName'] in totalSnaps.iloc[:7].values:
            player_projection+=5*.175
        elif player['PlayerName'] in totalSnaps.iloc[:13].values:
            player_projection+=4*.175
        elif player['PlayerName'] in totalSnaps.iloc[:24].values:
            player_projection+=3*.175
        elif player['PlayerName'] in totalSnaps.iloc[:32].values:
            player_projection+=2*.175
        elif player['PlayerName'] in totalSnaps.iloc[:40].values:
            player_projection+=1*.175
        #TargetShare Algorithm Values for RBs
        if player['MarketShareCarries'] >= .19:
            player_projection+=5*.075
        elif player['MarketShareCarries'] >= .13:
            player_projection+=4*.075
        elif player['MarketShareCarries'] >= .10:
            player_projection+=3*.075
        elif player['MarketShareCarries'] >= .085:
            player_projection+=2*.075
        elif player['MarketShareCarries'] >= .075:
            player_projection+=1*.075
        #TargetAverage Algorithm Values for RBs
        player["TargetAverage"] = player['Targets']/player['GamesStarted']
        if player['TargetAverage'] >= 5:
            player_projection+=5*.125
        elif player['TargetAverage'] >= 4:
            player_projection+=4*.125
        elif player['TargetAverage'] >= 3:
            player_projection+=3*.125
        elif player['TargetAverage'] >= 2:
            player_projection+=2*.125
        elif player['TargetAverage'] >= 1:
            player_projection+=1*.125
        #RedzoneTargetShare Algorithm Values for RBs
        if player['RedZoneCarries'] >= .25:
            player_projection+=5*.1
        elif player['RedZoneCarries'] >= .15:
            player_projection+=4*.1
        elif player['RedZoneCarries'] >= .10:
            player_projection+=3*.1
        elif player['RedZoneCarries'] >= .075:
            player_projection+=2*.1
        elif player['RedZoneCarries'] >= .05:
            player_projection+=1*.1
        #YardsPerRush Algorithm Values for RBs
        if player['YardsPerRush'] >= 5.5:
            player_projection+=5*.05
        elif player['YardsPerRush'] >= 5:
            player_projection+=4*.05
        elif player['YardsPerRush'] >= 4.5:
            player_projection+=3*.05
        elif player['YardsPerRush'] >= 3.5:
            player_projection+=2*.05
        elif player['YardsPerRush'] >= 2.5:
            player_projection+=1*.05
        #ReceivingYardsPerGame Algorithm Values for RBs
        player["YardsPerGame"] = player['ReceivingYards']/player['GamesStarted']
        if player['YardsPerGame'] >= 35:
            player_projection+=5*.075
        elif player['YardsPerGame'] >= 24:
            player_projection+=4*.075
        elif player['YardsPerGame'] >= 19:
            player_projection+=3*.075
        elif player['YardsPerGame'] >= 15:
            player_projection+=2*.075
        elif player['YardsPerGame'] >= 10:
            player_projection+=1*.075
        #RushingYardsPerGame Algorithm Values for RBs
        player["RushYardsPerGame"] = player['RushYards']/player['GamesStarted']
        if player['RushYardsPerGame'] >= 80:
            player_projection+=5*.15
        elif player['RushYardsPerGame'] >= 70:
            player_projection+=4*.15
        elif player['RushYardsPerGame'] >= 65:
            player_projection+=3*.15
        elif player['RushYardsPerGame'] >= 50:
            player_projection+=2*.15
        elif player['RushYardsPerGame'] >= 40:
            player_projection+=1*.15
    elif player['Position'] == 'TE':
        #SnapShare% Algorithm Values for TEs
        if player['SnapPercent'] > .95:
            player_projection+=5*.125
        elif player['SnapPercent'] > .93:
            player_projection+=4*.125
        elif player['SnapPercent'] > .89:
            player_projection+=3*.125
        elif player['SnapPercent'] > .80:
            player_projection+=2*.125
        elif player['SnapPercent'] > .70:
            player_projection+=1*.125
        #TotalSnaps Algorithm Values for TEs
        totalSnaps = df.sort_values(by=['Snaps'], ascending=False)
        totalSnaps = totalSnaps.loc[df['Position'] == 'TE']
        if player['PlayerName'] in totalSnaps.iloc[:7].values:
            player_projection+=5*.25
        elif player['PlayerName'] in totalSnaps.iloc[:13].values:
            player_projection+=4*.25
        elif player['PlayerName'] in totalSnaps.iloc[:24].values:
            player_projection+=3*.25
        elif player['PlayerName'] in totalSnaps.iloc[:32].values:
            player_projection+=2*.25
        elif player['PlayerName'] in totalSnaps.iloc[:40].values:
            player_projection+=1*.25
        #TargetShare Algorithm Values for TEs
        if player['TargetPercent'] >= .3:
            player_projection+=5*.125
        elif player['TargetPercent'] >= .27:
            player_projection+=4*.125
        elif player['TargetPercent'] >= .245:
            player_projection+=3*.125
        elif player['TargetPercent'] >= .2:
            player_projection+=2*.125
        elif player['TargetPercent'] >= .16:
            player_projection+=1*.125
        #TargetAverage Algorithm Values for TEs
        player["TargetAverage"] = player['Targets']/player['GamesStarted']
        if player['TargetAverage'] >= 12:
            player_projection+=5*.3
        elif player['TargetAverage'] >= 10:
            player_projection+=4*.3
        elif player['TargetAverage'] >= 7.75:
            player_projection+=3*.3
        elif player['TargetAverage'] >= 7:
            player_projection+=2*.3
        elif player['TargetAverage'] >= 6:
            player_projection+=1*.3
        #RedzoneTargetShare Algorithm Values for TEs
        if player['RedZoneTargetShare'] >= .375:
            player_projection+=5*.075
        elif player['RedZoneTargetShare'] >= .305:
            player_projection+=4*.075
        elif player['RedZoneTargetShare'] >= .25:
            player_projection+=3*.075
        elif player['RedZoneTargetShare'] >= .15:
            player_projection+=2*.075
        elif player['RedZoneTargetShare'] >= .10:
            player_projection+=1*.075
        #YardsPerGame Algorithm Values for TEs
        player["YardsPerGame"] = player['ReceivingYards']/player['GamesStarted']
        if player['YardsPerGame'] >= 100:
            player_projection+=5*.125
        elif player['YardsPerGame'] >= 80:
            player_projection+=4*.125
        elif player['YardsPerGame'] >= 65:
            player_projection+=3*.125
        elif player['YardsPerGame'] >= 52.5:
            player_projection+=2*.125
        elif player['YardsPerGame'] >= 45.5:
            player_projection+=1*.125
    return player_projection
def getQBScore(playerName):
    player = df.loc[df['PlayerName'] == playerName]
    team = player.iloc[0]['Team']
    quarterback = df.loc[(df['Team'] == team) & (df['Position'] == 'QB')]
    quarterback = quarterback.sort_values(by=['AttemptedPasses'], ascending=False)
    quarterback = quarterback.iloc[0]
    qb_score = 0
    if quarterback['PasserRating'] >= 105:
        qb_score+=5*.2
    elif quarterback['PasserRating'] >= 92.5:
        qb_score+=4*.2
    elif quarterback['PasserRating'] >= 85:
        qb_score+=3*.2
    elif quarterback['PasserRating'] >= 81:
        qb_score+=2*.2
    elif quarterback['PasserRating'] >= 78:
        qb_score+=1*.2
    quarterback["YardsPerPass"] = quarterback['PassingYards']/quarterback['AttemptedPasses']
    if quarterback['YardsPerPass'] >= 8.5:
        qb_score+=5*.25
    elif quarterback['YardsPerPass'] >= 7.5:
        qb_score+=4*.25
    elif quarterback['YardsPerPass'] >= 7:
        qb_score+=3*.25
    elif quarterback['YardsPerPass'] >= 6.75:
        qb_score+=2*.25
    elif quarterback['YardsPerPass'] >= 6.5:
        qb_score+=1*.25
    quarterback["Y/G"] = quarterback['PassingYards']/quarterback['GamesPlayed']
    if quarterback['Y/G'] >= 300:
        qb_score+=5*.25
    elif quarterback['Y/G'] >= 275:
        qb_score+=4*.25
    elif quarterback['Y/G'] >= 265:
        qb_score+=3*.25
    elif quarterback['Y/G'] >= 250:
        qb_score+=2*.25
    elif quarterback['Y/G'] >= 230:
        qb_score+=1*.25
    quarterback["Completion%"] = quarterback['CompletedPasses']/quarterback['AttemptedPasses']
    if quarterback['Completion%'] >= .68:
        qb_score+=5*.1
    elif quarterback['Completion%'] >= .665:
        qb_score+=4*.1
    elif quarterback['Completion%'] >= .65:
        qb_score+=3*.1
    elif quarterback['Completion%'] >= .61:
        qb_score+=2*.1
    elif quarterback['Completion%'] >= .57:
        qb_score+=1*.1
    return qb_score

def getTeamScore(playerName):
    player = df.loc[df['PlayerName'] == playerName]
    team = df_teams.loc[(df_teams['Team'] == player.iloc[0]['Team'])]
    team_score = 0
    player = player.iloc[0]
    team = team.iloc[0]
    if (player['Position'] == 'WR') | (player['Position'] == 'TE'):
        if team['RedZoneScoringAttempts/Game'] >= 4:
            team_score += 5 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 3.7:
            team_score += 4 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 3.15:
            team_score += 3 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 2.75:
            team_score += 2 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 2.5:
            team_score += 1 * .1
        if team['TeamPPG'] >= 27:
            team_score += 5 * .35
        elif team['TeamPPG'] >= 24.5:
            team_score += 4 * .35
        elif team['TeamPPG'] >= 23:
            team_score += 3 * .35
        elif team['TeamPPG'] >= 20:
            team_score += 2 * .35
        elif team['TeamPPG'] >= 17:
            team_score += 1 * .35
        if team['TeamPPG'] >= 27:
            team_score += 5 * .35
        elif team['TeamPPG'] >= 24.5:
            team_score += 4 * .35
        elif team['TeamPPG'] >= 23:
            team_score += 3 * .35
        elif team['TeamPPG'] >= 20:
            team_score += 2 * .35
        elif team['TeamPPG'] >= 17:
            team_score += 1 * .35
        if team['TeamPassY/G'] >= 275:
            team_score += 5 * .35
        elif team['TeamPassY/G'] >= 245:
            team_score += 4 * .35
        elif team['TeamPassY/G'] >= 230:
            team_score += 3 * .35
        elif team['TeamPassY/G'] >= 220:
            team_score += 2 * .35
        elif team['TeamPassY/G'] >= 200:
            team_score += 1 * .35
        if team['PointDifferential'] >= 7.5:
            team_score += 5 * .2
        elif team['PointDifferential'] >= 3:
            team_score += 4 * .2
        elif team['PointDifferential'] >= 0:
            team_score += 3 * .2
        elif team['PointDifferential'] >= -2:
            team_score += 2 * .2
        elif team['PointDifferential'] >= -3.75:
            team_score += 1 * .2
    if player['Position'] == 'RB':
        if team['RedZoneScoringAttempts/Game'] >= 4:
            team_score += 5 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 3.7:
            team_score += 4 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 3.15:
            team_score += 3 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 2.75:
            team_score += 2 * .1
        elif team['RedZoneScoringAttempts/Game'] >= 2.5:
            team_score += 1 * .1
        if team['TeamPPG'] >= 27:
            team_score += 5 * .35
        elif team['TeamPPG'] >= 24.5:
            team_score += 4 * .35
        elif team['TeamPPG'] >= 23:
            team_score += 3 * .35
        elif team['TeamPPG'] >= 20:
            team_score += 2 * .35
        elif team['TeamPPG'] >= 17:
            team_score += 1 * .35
        if team['TeamRushY/G'] >= 160:
            team_score += 5 * .4
        elif team['TeamRushY/G'] >= 140:
            team_score += 4 * .4
        elif team['TeamRushY/G'] >= 120:
            team_score += 3 * .4
        elif team['TeamRushY/G'] >= 100:
            team_score += 2 * .4
        elif team['TeamRushY/G'] >= 89:
            team_score += 1 * .4
        if team['PointDifferential'] >= 7.5:
            team_score += 5 * .2
        elif team['PointDifferential'] >= 3:
            team_score += 4 * .2
        elif team['PointDifferential'] >= 0:
            team_score += 3 * .2
        elif team['PointDifferential'] >= -2:
            team_score += 2 * .2
        elif team['PointDifferential'] >= -3.75:
            team_score += 1 * .2
    return team_score

def getOpposingTeamScore(playerName):
    player = df.loc[df['PlayerName'] == playerName]
    team = df_teams.loc[(df_teams['Team'] == player.iloc[0]['Team'])]
    if team.iloc[0]['Opponent'] == 'BYE':
        return None
    opponent = df_teams.loc[(df_teams['Team']) == team.iloc[0]['Opponent']]
    opponent = opponent.iloc[0]
    player = player.iloc[0]
    opposing_score = 0
    if (player['Position'] == 'WR') | (player['Position'] == 'TE'):
        if opponent['PPGAllowed'] >= 26:
            opposing_score += 5 * .3
        elif opponent['PPGAllowed'] >= 24:
            opposing_score += 4 * .3
        elif opponent['PPGAllowed'] >= 21:
            opposing_score += 3 * .3
        elif opponent['PPGAllowed'] >= 18:
            opposing_score += 2 * .3
        elif opponent['PPGAllowed'] >= 17:
            opposing_score += 1 * .3

        if opponent['ReceivingYardsAllowed'] >= 265:
            opposing_score += 5 * .4
        elif opponent['ReceivingYardsAllowed'] >= 235:
            opposing_score += 4 * .4
        elif opponent['ReceivingYardsAllowed'] >= 215:
            opposing_score += 3 * .4
        elif opponent['ReceivingYardsAllowed'] >= 200:
            opposing_score += 2 * .4
        elif opponent['ReceivingYardsAllowed'] >= 185:
            opposing_score += 1 * .4

        if opponent['Blitz%'] < 18:
            opposing_score += 5 * .15
        elif opponent['Blitz%'] < 23:
            opposing_score += 4 * .15
        elif opponent['Blitz%'] < 26:
            opposing_score += 3 * .15
        elif opponent['Blitz%'] < 29:
            opposing_score += 2 * .15
        elif opponent['Blitz%'] < 32.5:
            opposing_score += 1 * .15

        if opponent['Pressure%'] < 18:
            opposing_score += 5 * .15
        elif opponent['Pressure%'] < 20:
            opposing_score += 4 * .15
        elif opponent['Pressure%'] < 24:
            opposing_score += 3 * .15
        elif opponent['Pressure%'] < 25.5:
            opposing_score += 2 * .15
        elif opponent['Pressure%'] < 29:
            opposing_score += 1 * .15
    elif player['Position'] == 'RB':
        if opponent['PPGAllowed'] >= 26:
            opposing_score += 5 * .4
        elif opponent['PPGAllowed'] >= 24:
            opposing_score += 4 * .4
        elif opponent['PPGAllowed'] >= 21:
            opposing_score += 3 * .4
        elif opponent['PPGAllowed'] >= 18:
            opposing_score += 2 * .4
        elif opponent['PPGAllowed'] >= 17:
            opposing_score += 1 * .4

        if opponent['RushingYardsAllowed'] >= 150:
            opposing_score += 5 * .6
        elif opponent['RushingYardsAllowed'] >= 130:
            opposing_score += 4 * .6
        elif opponent['RushingYardsAllowed'] >= 119:
            opposing_score += 3 * .6
        elif opponent['RushingYardsAllowed'] >= 110:
            opposing_score += 2 * .6
        elif opponent['RushingYardsAllowed'] >= 100:
            opposing_score += 1 * .6
    return opposing_score

def getTotalScore(playerName):
    if getOpposingTeamScore(playerName) is None:
        return .8 * getPlayerScore(playerName) + .1 * getQBScore(playerName) + .1 * getTeamScore(playerName)
    return .75 * getPlayerScore(playerName) + .1 * getQBScore(playerName) + .1 * getTeamScore(playerName) + .05 * getOpposingTeamScore(playerName)





te_df = df[df['Position'] == 'TE']
te_df = te_df.sort_values(by=['PPR'], ascending=False)
te_df = te_df[:35]
values =[]
for index, row in te_df.iterrows():
    values.append(getTotalScore(row['PlayerName']))
te_df['Rankings'] = values
te_df = te_df.sort_values(by=['Rankings'], ascending=False)




pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    {table}
  </body>
</html>.
'''

# OUTPUT AN HTML FILE
with open('fanrankste.html', 'w') as f:
    f.write(html_string.format(table=te_df.to_html(classes='mystyle')))


# @app.route('/weeklyInsights.html', methods=("POST", "GET"))
# def html_table():

#     return render_template('weeklyInsights.html',  tables=[df.to_html(classes='data', header="true")])

if __name__ == '__main__':
    app.run()
