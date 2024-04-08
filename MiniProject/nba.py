from nba_api.stats.static import players
from nba_api.live.nba.endpoints import scoreboard
from pprint import PrettyPrinter

# Find players by full name.
# print(players.find_players_by_full_name('james'))

printer = PrettyPrinter()
# Today's Score Board
games = scoreboard.ScoreBoard()

# dict
_scoreboard = games.get_dict()
games = _scoreboard['scoreboard']['games']

for game in games:
    # awayteam and hometeam dictionaary
    awayteam = game['awayTeam']
    hometeam = game['homeTeam']
    awayteamname = awayteam['teamName']
    hometeamname = hometeam['teamName']
    awayteamscore = awayteam['score']
    hometeamscore = hometeam['score']
    print(f"{awayteamname} VS {hometeamname}")
    print(f"Score is {awayteamscore} : {hometeamscore}")
    print("--------------------------------------------------------")
    # break
# printer.pprint(games.keys())

# dict_keys(['gameDate', 'leagueId', 'leagueName', 'games'])
# dict_keys(['gameId', 'gameCode', 'gameStatus', 'gameStatusText', 'period', 'gameClock', 'gameTimeUTC', 'gameEt', 'regulationPeriods', 'ifNecessary', 'seriesGameNumber', 'gameLabel', 'gameSubLabel', 'seriesText', 'seriesConference', 'poRoundDesc', 'gameSubtype', 'homeTeam', 'awayTeam', 'gameLeaders', 'pbOdds'])