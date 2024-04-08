from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
# we set an request to the api, and output it into JSON format
    data = get(BASE_URL+ ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    # this would get the json link corresponding to the scoreboard
    scoreboard = get_links()['currentScoreboard']
    '''
    data = get(BASE_URL + scoreboard).json()
    
    # as we are getting a python dictionary, we can use keys() to get all the keys in the dictionary. if we don't do it, we would only get a very messy output
    printer.pprint(data.keys())
    '''

    # After searching we would like to look closer to info about games.
    '''
    data = get(BASE_URL + scoreboard).json()['games']
    printer.pprint(data.keys())
    '''


    # we would get an error saying our list object has no attribute 'keys'
    # That our games is a list of different games. we would need to write a for loop to handle this

    games = get(BASE_URL + scoreboard).json()['games']
    
    for game in games:
        # printer.pprint(game.keys())
        # break
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")

def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['teams']

    # printer.pprint(teams.keys())
    # lambda function: we would check every element in teams(x) and check is the team name equal to 'Team'. If not, we would keep the elementm, if yes we would exclude it from our teams dictionary
    teams = filter(lambda x: x['name'] != "Team", teams)
    teams.sort(key = lambda x: int(x['ppg']['rank']))
    for i, team in teams:
        name =  team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        print(f"{i +1}, {name} - {nickname} - {ppg}")



# get_scoreboard()
# printer.pprint(data)

