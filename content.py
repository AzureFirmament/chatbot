

import requests
from urllib import  request
from urllib import parse
import hashlib
import json
import sqlite3

URL_football = "https://api-football-v1.p.rapidapi.com/v2/"
headers = {
   'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
   'x-rapidapi-key': "be9dba5c1dmsh68531726f507982p1e8494jsn9503eca03978"
   }

#   搜索国家联赛  https://api-football-v1.p.rapidapi.com/v2/league/country/england
#   get("https://api-football-v1.p.rapidapi.com/v2/leagues/search/{name}");
#
class LEAGUE:
    def __init__(self, id = None, country = None, name = None, logo = None, season = None):
        self.id = id
        self.country = country
        self.name = name
        self.logo = logo
        self.season = season
    def __str__(self):
        message = ""
        if self.name is not None:
            message = "The name of the league is called {}.".format(self.name)
        if self.country is not None:
            message += "The league is in {}.".format(self.country)
        if self.logo is not None:
            message += "The logo of the league is {}.".format(self.logo)
        return message

#{'team_id': 10, 'name': 'England', 'code': None,
# 'logo': 'https://media.api-sports.io/football/teams/10.png', 'country': 'England',
# 'founded': 1863, 'venue_name': 'Wembley Stadium', 'venue_surface': 'grass', 'venue_address': 'Stadium Way, Wembley, Brent',
# 'venue_city': 'London', 'venue_capacity': 90000}
class TEAM:
    def __init__(self, id = None, name = None, country = None, logo = None, founded = None, venue_name = None, venue_address = None, venue_city = None, venue_cap = None):
        self.id = id
        self.name = name
        self.country = country
        self.logo = logo
        self.founded = founded
        self.venue_name = venue_name
        self.venue_address = venue_address
        self.venue_city = venue_city
        self.venue_cap = venue_cap
    def __str__(self):
        message = ""
        if self.name is not None:
            message = "The name of the team is called {}.".format(self.name)
        if self.country is not None:
            message += "{} is in {}.".format(self.name, self.country)
        if self.logo is not None:
            message += "The logo of the team is {}.".format(self.logo)
        if self.founded is not None:
            message += '{} is founded in {}.'.format(self.name, self.founded)
        if self.venue_city is not None:
            message += "The venue of the team is in {}.".format(self.venue_city)
        if self.venue_name is not None:
            message += "The name of the venue is {}.".format(self.venue_name)
        if self.venue_address is not None:
            message += "The address of the venue is {}.".format(self.venue_address)
        if self.venue_cap is not None:
            message += "the capacity of the venue is {}.".format(self.venue_cap)
        return message

#{'player_id': 308, 'player_name': 'D. Sturridge', 'firstname': 'Daniel Andre', 'lastname': 'Sturridge',
# 'number': None, 'position': 'Attacker', 'age': 31, 'birth_date': '01/09/1989', 'birth_place': 'Birmingham',
# birth_country': 'England', 'nationality': 'England', 'height': '188 cm', 'weight': '76 kg'}

#{'player_id': 40, 'player_name': 'Andrés Felipe Solano Dávila', 'firstname': 'Andrés Felipe',
# 'lastname': 'Solano Dávila', 'number': None, 'position': 'Defender', 'age': 22, 'birth_date': '24/02/1998',
# 'birth_place': 'Santa Marta', 'birth_country': 'Colombia', 'nationality': 'Colombia', 'height': '176 cm',
# 'weight': '69 kg', 'injured': None, 'rating': None, 'team_id': 9570, 'team_name': 'Atlético Madrid II',
# 'league': 'Segunda B', 'season': '2019-2020', 'captain': 0, 'shots': {'total': 0, 'on': 0},
# 'goals': {'total': 1, 'conceded': 0, 'assists': 0, 'saves': 0}, 'passes': {'total': 0, 'key': 0, 'accuracy': 0},
# 'tackles': {'total': 0, 'blocks': 0, 'interceptions': 0}, 'duels': {'total': 0, 'won': 0},
# 'dribbles': {'attempts': 0, 'success': 0}, 'fouls': {'drawn': 0, 'committed': 0}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0},
# 'penalty': {'won': 0, 'commited': 0, 'success': 0, 'missed': 0, 'saved': 0}, 'games': {'appearences': 16, 'minutes_played': 1274, 'lineups': 14},
# 'substitutes': {'in': 2, 'out': 2, 'bench': 2}}
class PLAYER:
    def __init__(self, id = None, name = None, firstname = None, lastname = None, number = None, position = None, age = None, birth_date = None, birth_place = None,
                 birth_country = None, nationality = None, height = None, weight = None, team_id = None, team_name = None, games = None, goals = None, penalty = None,
                 cards = None, shots = None, passes = None, tackles = None, fouls = None, duels = None, dribbles = None, substitues = None, rating = None):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.position = position
        self.age = age
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.birth_place = birth_country
        self.nationality = nationality
        self.height = height
        self.weight = weight
        self.team_id = team_id
        self.team_name = team_name
        self.games = games
        self.goals = goals
        self.penalty = penalty
        self.cards = cards
        self.shots = shots
        self.passes = passes
        self.tackles = tackles
        self.fouls = fouls
        self.duels = duels
        self.dribbles = dribbles
        self.substitues = substitues
        self.rating = rating

    def __str__(self):
        message = ""
        if self.name is not None:
            message = "The name of the player is {}.".format(self.name)
        if self.number is not None:
            message += "The number of {} is {}.".format(self.name, self.number)
        if self.age is not None:
            message += "{} is {}.".format(self.name, self.age)
        if self.position is not None:
            message += "The position of the player is {}.".format(self.position)
        if self.nationality is not None:
            message += "The nationality of the player is {}.".format(self.nationality)
        if self.height is not None:
            message += "The height of {} is {}.".format(self.name, self.height)
        if self.weight is not None:
            message += "The weight of the player is {}.".format(self.weight)
        if self.team_name is not None:
            message += "The player plays in {}.".format(self.team_name)
        if self.games is not None:
            message += "The player participated in {} matches and have played for {} minutes.".format(self.games["appearances"], self.games["minutes_played"])
        if self.rating is not None:
            message += "The player's rating is {}.".format(self.rating)
        if self.goals is not None:
            if self.goals["conceded"] is  not None:
                message += "{} scored {} goals with {} assists.".format(self.name, self.goals["total"], self.goals["assists"])
            else:
                message += "{} conceded {} goals with {} saves.".format(self.name, self.goals["conceded"],
                                                                        self.goals["saves"])
        if self.shots is not None:
            message += "The player shot {} times with {} times in the within the frame.".format(self.shots["total"], self.shots["on"])
        if self.cards is not None:
            message += "The player got {} yellow cards and {} red cards".format(self.cards["yellow"], self.cards["red"])
        if self.passes is not None:
            message += "The player passed {} times, with key pass {} times and accuracy at {}.".format(self.passes["total"], self.passes["key"], self.passes["accuracy"])
        if self.tackles is not None:
            message += "The player tackled {} times, with {} blocks and {} interceptions.".format(self.tackles["total"], self.tackles["blocks"], self.tackles["interceptions"])
        if self.fouls is not None:
            message += "{} drew {} fouls and committed {} fouls.".format(self.name, self.fouls["drawn"], self.fouls["committed"])
        if self.duels is not None:
            message += "The player were involved in {} duels, with {} times wining.".format(self.duels["total"], self.duels["won"])
        if self.dribbles is not None:
            message += "{} tried {} times dribbling and succeeded for {} times.".format(self.name,self.dribbles["attempts"], self.dribbles["success"])

        return str(message)

#{'id': 1, 'name': 'J. Klopp', 'firstname': 'Jürgen', 'lastname': 'Klopp', 'age': 53, 'birth_date': '16/06/1967',
# 'birth_place': 'Stuttgart', 'birth_country': 'Germany', 'nationality': 'Germany', 'height': '191 cm', 'weight': '83 kg',
# 'team': {'id': 40, 'name': 'Liverpool'}, 'career': [{'team': {'id': 40, 'name': 'Liverpool'}, 'start': 'October 2015', 'end': None},
# {'team': {'id': 165, 'name': 'Borussia Dortmund'}, 'start': 'July 2008', 'end': 'July 2015'}, {'team': {'id': 164, 'name': 'Mainz 05'},
# 'start': 'February 2001', 'end': 'June 2008'}]}
class COACH:
    def __int__(self,id = None, name = None, firstname = None, lastname = None, age = None, birth_date = None,
                birth_place = None, birth_country = None, nationality = None, height = None, weight = None,
                team = None, career = None):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.birth_country = birth_country
        self.nationality = nationality
        self.height = height
        self.weight = weight
        if team is not None:
            self.team_id = team["id"]
            self.team_name = team["name"]
        else:
            self.team_id = self.team_name = None
        self.career = career
    def __str__(self):
        message = ""
        if self.name is not None:
            message += "The coach is {}.".format(self.name)
        if self.age is not None:
            message += "The coach is {} years old.".format(self.age)
        if self.nationality is not None:
            message += "{}'s nationality is {}.".format(self.name, self.nationality)
        if self.height is not None:
            message += "The height of the coach is {}.".format(self.height)
        if self.weight is not None:
            message += "The weight of the coach is {}.".format(self.weight)
        if self.team_name is not None:
            message += "{} is the coach of {}.".format(self.name, self.team_name)
        if self.career is not None:
            message += " Here is {}'s coach career".format(self.name)
            for team in self.career:
                if team["end"] is None:
                    temp = "now"
                else:
                    temp = team["end"]
                message += "{} was the coach of {} from {} to {}".format(self.name, team["team"]["name"], str(team["start"]), temp)
        return message

#{'fixture_id': 194205, 'league_id': 701, 'league': {'name': 'Premier League', 'country': 'England',
# 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'},
# 'event_date': '2010-08-15T15:00:00+00:00', 'event_timestamp': 1281884400,
# 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 38', 'status': 'Match Finished',
#  'statusShort': 'FT', 'elapsed': 90, 'venue': 'Anfield (Liverpool)', 'referee': None,
# 'homeTeam': {'team_id': 40, 'team_name': 'Liverpool', 'logo': 'https://media.api-sports.io/football/teams/40.png'},
# 'awayTeam': {'team_id': 42, 'team_name': 'Arsenal', 'logo': 'https://media.api-sports.io/football/teams/42.png'},
# 'goalsHomeTeam': 1, 'goalsAwayTeam': 1, 'score': {'halftime': '0-0', 'fulltime': '1-1', 'extratime': None, 'penalty': None}}
class FIXTURE:
    def __init__(self, id = None, league_id = None, league_ = None, event_date = None, firstHalfStart = None,
                 secondHalfStart = None, round = None, status = None, statusShort = None, elapsed = None,
                 venue = None, referee = None, hometeam = None, awayteam = None, goalsHomeTeam = None, goalsAwayTeam = None,
                 score = None):
        self.id = id
        self.league_id = league_id
        if league_ is not None:
            self.league = LEAGUE(name = league_["name"], country = league_["country"], logo = league_["logo"])
        else:
            self.league = LEAGUE()
        self.event_date = event_date
        self.firstHalfStart = firstHalfStart
        self.secondHalfStart = secondHalfStart
        self.round = round
        self.status = status
        self.statusShort = statusShort
        self.elapsed = elapsed
        self.venue = venue
        self.referee = referee
        if hometeam is not None:
            self.hometeam = TEAM(id = hometeam["team_id"], name = hometeam["team_name"], logo= hometeam["logo"])
        else:
            self.hometeam = TEAM()
        if awayteam is not None:
            self.awayteam = TEAM(id=awayteam["team_id"], name=awayteam["team_name"], logo=awayteam["logo"])
        else:
            self.awayteam = TEAM()
        self.goalsHomeTeam = goalsHomeTeam
        self.goalsAwayTeam = goalsAwayTeam
        self.score = score
    def __str__(self):
        message = ""
        if self.league is not None:
            message += " The fixture match is in {}, which is in {}, with logo {}.".format(self.league.name, self.league.country, self.league.logo)
        if self.event_date is not None:
            message += "The event date is at {}.".format(self.event_date)
        if self.round is not None:
            message += "The round is {}.".format(self.round)
        if self.hometeam and self.awayteam is not None:
            message += "The home team is {}, The away team is {}.".format(self.hometeam.name, self.awayteam.id)
        if self.status is not None:
            if self.status is "Match Finished":
                message += "The match is now finished."
                if self.score is not None:
                    message += "The score is {}-{}, with {} at half time and {} at full time.".format(self.goalsHomeTeam, self.goalsAwayTeam ,self.score["halftime"], self.score["fulltime"])
                    if self.score["extratime"] is not None:
                        message += "The score is {} in extratime.".format(self.score["extratime"])
                    if self.score["penalty"] is not None:
                        message += "The score is {} in penalty.".format(self.score["penalty"])
            elif self.status is "Not Started":
                message += "The match is not started."
            else:
                message += "The match is not finished yet."
        return message






def search_league(country = None, name = None, team_id = None, season = None):
    if country is not None:
        url = URL_football + "leagues/country/" + country
    elif name is not None:
        url = URL_football + "leagues/search/" + name
    elif team_id is not None:
        url = URL_football + "leagues/team/" + str(team_id)
    else:
        return None
    if season is not None:
        url = url +"/" + str(season)

    #return url
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索队伍
#   get("https://api-football-v1.p.rapidapi.com/v2/teams/team/{team_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/teams/league/{league_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/teams/search/{name}");
#   get("https://api-football-v1.p.rapidapi.com/v2/teams/search/{country}");
def search_team(team_id = None, league_id = None, name = None, country = None):
    if team_id is not None:
        url = URL_football + "teams/team/" + str(team_id)
    elif league_id is not None:
        url = URL_football + "teams/league/" + str(league_id)
    elif name is not None:
        url = URL_football + "teams/search/" + name
    elif country is not None:
        url = URL_football + "teams/search/" + country
    else:
        return None

    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result


#   依靠队伍id搜索fixture的比赛  https://api-football-v1.p.rapidapi.com/v2/fixtures/team/605
def search_fixture(team_id):
    url = URL_football + "fixtures/team/" + str(team_id)
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   通过赛季和队伍搜索阵容 https://api-football-v1.p.rapidapi.com/v2/players/squad/605/2018-2019
def search_squad(team_id, season = 2019):
    url = URL_football + "players/squad/" + str(team_id)
    if (season is not None):
        url = url + "/" + str(season)

    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   通过球员id搜索球员信息    get("https://api-football-v1.p.rapidapi.com/v2/players/search/{lastname}");
def search_player(lastname = None):
    url = URL_football + "players/search/" + lastname
    #print(url)
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索球员数据
#   get("https://api-football-v1.p.rapidapi.com/v2/players/player/{player_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/players/player/{player_id}/{season}");
#   get("https://api-football-v1.p.rapidapi.com/v2/players/team/{team_id}/{season}");
def search_player_statistics(player_id = None, team_id = None, season = None):
    if (team_id is not None):
        url = URL_football + "players/team/" + str(team_id)
        if (season is not None):
            url = url + "/" + str(season)

    elif(player_id is not None):
        url = URL_football + "players/player/" + str(player_id)
        if (season is not None):
            url = url + "/" + str(season)
    else:
        return None

    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#
#   搜索教练
#   get("https://api-football-v1.p.rapidapi.com/v2/coachs/coach/{coach_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/coachs/team/{team_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/coachs/search/{name}");
def search_coach(coach_id = None, team_id = None, coach_name = None):
    if(coach_id is not None):
        url = URL_football + "coachs/coach/" + str(coach_id)
    elif(team_id is not None):
        url = URL_football + "coachs/team/" + str(team_id)
    elif(coach_name is not None):
        url = URL_football + "coachs/search/" + coach_name
    else:
        return None
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索赛季全部球员    get("https://api-football-v1.p.rapidapi.com/v2/players/seasons");
def search_player_all(season):
    url = URL_football + "players/" + str(season)
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索最佳射手  get("https://api-football-v1.p.rapidapi.com/v2/topscorers/{league_id}");
def search_topscorer(league_id):
    url = URL_football + "topscorers/" + str(league_id)
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索fixture的所有球员数据
#   get("https://api-football-v1.p.rapidapi.com/v2/players/fixture/{fixture_id}");
#   没啥用！
def search_fixture_stastics(fixture_id):
    url = URL_football + "players/fixture/" + str(fixture_id)
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索转会数据
#   get("https://api-football-v1.p.rapidapi.com/v2/transfers/player/{player_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/transfers/team/{team_id}");
def search_transfer(player_id = None, team_id = None):
    if(player_id is not None):
        url = URL_football + "transfers/player/" + str(player_id)
    elif(team_id is not None):
        url = URL_football + "transfers/team/" + str(team_id)
    else:
        return None
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result

#   搜索奖杯
#   get("https://api-football-v1.p.rapidapi.com/v2/trophies/player/276");
#   get("https://api-football-v1.p.rapidapi.com/v2/trophies/coach/2");
#[{'league': 'Championship', 'country': 'England', 'season': '2018/2019', 'place': 'Winner'}]
def search_trophies(player_id = None, coach_id = None):
    type = None
    if (player_id is not None):
        url = URL_football + "trophies/player/" + str(player_id)
        type = "player"
    elif (coach_id is not None):
        url = URL_football + "trophies/coach/" + str(coach_id)
        type = "coach"
    else:
        return None, type
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result, type


#   搜索是否禁赛/受伤
#   get("https://api-football-v1.p.rapidapi.com/v2/sidelined/player/276");
#   get("https://api-football-v1.p.rapidapi.com/v2/sidelined/coach/2");
def search_sideline(player_id = None, coach_id = None):
    type = None
    if(player_id is not None):
        url = URL_football + "sideline/player/" + str(player_id)
        type = "player"
    elif(coach_id  is not None):
        url = URL_football + "sideline/coach/" + str(player_id)
        type = "coach"
    else:
        return None, type
    response = requests.request("GET", url,headers = headers)
    result = response.json()
    return result, type

#   搜索标签（筛选赔率）
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/labels/");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/labels/{label_id}");
def search_labels(label_id = None):
    url = URL_football + "odds/labels/"
    if label_id is not None:
        url = url + str(label_id)
    response = requests.request("GET", url,headers = headers)
    return response.json()

#   搜索赔率商家
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/bookmakers/");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/bookmakers/{bookmaker_id}");
def search_bookmakers(bookmaker_id = None):
    url = URL_football + "odds/bookmakers/"
    if bookmaker_id is not None:
        url = url + str(bookmaker_id)
    response = requests.request("GET", url,headers = headers)
    return response.json()

#   搜索有赔率的fixture的id
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/mapping/");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/mapping?page=2");
def search_mapping(page = None):
    url = URL_football + "odds/mapping"
    if page is not None:
        url = url + "?page=" + str(page)
    else:
        url = url + "/"
    response = requests.request("GET", url,headers = headers)
    return response.json()

#   搜索赔率
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/fixture/{fixture_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/fixture/{fixture_id}/bookmaker/{bookmaker_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/fixture/{fixture_id}/label/{label_id}");
def search_odds_f(fixture_id, bookmaker = None, label = None):
    url = URL_football + "odds/fixture/" + str(fixture_id)
    if bookmaker is not None:
        url = url + "/bookmaker/" + str(bookmaker)
    elif label is not None:
        url = url + "/label/" + str(label)
    response = requests.request("GET", url,headers = headers)
    return response.json()

#   get("https://api-football-v1.p.rapidapi.com/v2/odds/league/{league_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/league/{league_id}?page=2");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/league/{league_id}/bookmaker/{bookmaker_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/league/{league_id}/label/{label_id}");
def search_odds_l(league_id, page = None, bookmaker = None, label = None):
    url = URL_football + "odds/league/" + str(league_id)
    if page is not None:
        url = url + "?page=" + str(page)
    elif bookmaker is not None:
        url = url + "/bookmaker/" + str(bookmaker)
    elif label is not None:
        url = url + "/label/" + str(label)
    response = requests.request("GET", url,headers = headers)
    return response.json()

#   get("https://api-football-v1.p.rapidapi.com/v2/odds/date/{yyyy-mm-dd}");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/date/{yyyy-mm-dd}?page=2");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/date/{yyyy-mm-dd}?page=2?timezone=europe/london");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/date/{yyyy-mm-dd}/bookmaker/{bookmaker_id}");
#   get("https://api-football-v1.p.rapidapi.com/v2/odds/date/{yyyy-mm-dd}/label/{label_id}");
def search_odds_d(date, bookmaker = None, label = None, timezone = None, page = None):
    url = URL_football + "odds/date/" + date[0] + "-" + date[1] + "-" +date[2]
    if page is not None:
        url = url + "?page=" + str(page)
        if timezone is not None:
            url = url + "?timezone=" + timezone[0] + "/" + timezone[1]
    elif bookmaker is not None:
        url = url + "/bookmaker/" + str(bookmaker)
    elif label is not None:
        url = url + "/label/" + str(label)
    return url
    # response = requests.request("GET", url,headers = headers)
    # return response.json()

#   搜索预测，通过fixtureid
#   get("https://api-football-v1.p.rapidapi.com/v2/predictions/{fixture_id}");
def search_prediction(fixture_id):
    url = URL_football + "predictions/" + str(fixture_id)
    return url
    # response = requests.request("GET", url,headers = headers)
    # return response.json()

#{'league_id': 2, 'name': 'Premier League', 'type': 'League', 'country': 'England',
# 'country_code': 'GB', 'season': 2018, 'season_start': '2018-08-10', 'season_end': '2019-05-12',
# 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg',
# 'standings': 1, 'is_current': 0, 'coverage': {'standings': True, 'fixtures': {'events': True,
# 'lineups': True, 'statistics': True, 'players_statistics': True}, 'players': True,
# 'topScorers': True, 'predictions': True, 'odds': False}}
def explain_league(response):
   # message = {}
    if response is None:
        return "I have found no result", []
    if "error" in response["api"].keys():
        return "I have found no result", []
    leagues = response['api']['leagues']
   # country = leagues[0]["country"]
    result = []
    for league in leagues:
        temp = LEAGUE(id = league["league_id"], name = league["name"], country = league["country"], season = league["season"])
        result.append(temp)
    hint = ""
    if len(result)> 4:
        hint = "I found {} leagues and I will list some.".format(len(result))
        count = 0
        for league in result:
            count += 1
            hint += str(league)
            hint += "\n"
            if count == 4:
                break
    else:
        hint = "Here is the result."
        for league in result:
            hint += str(league)
            hint += "\n"
    return hint, result
#    names = [temp for temp in names]
#    temp = "In {} there are ".format(country)
#    temp += ",".join(names)
#    temp = temp + "."
#    message['name'] = temp



#{'team_id': 10, 'name': 'England', 'code': None,
# 'logo': 'https://media.api-sports.io/football/teams/10.png', 'country': 'England',
# 'founded': 1863, 'venue_name': 'Wembley Stadium', 'venue_surface': 'grass', 'venue_address': 'Stadium Way, Wembley, Brent',
# 'venue_city': 'London', 'venue_capacity': 90000}
def explain_team(response):
    if response is None:
        return "I have found no result", []
    if "error" in response["api"].keys():
        return "I have found no result.",[]
    teams = response["api"]["teams"]
    result = []
    for team in teams:
        temp = TEAM(id = team["team_id"], name = team["name"], logo = team["logo"], country = team["country"], founded = team["founded"],
                    venue_name = team["venue_name"], venue_address = team['venue_address'], venue_city = team["venue_city"], venue_cap = team["venue_capacity"])
        result.append(temp)
    message = ""
    if len(result) > 4:
        count = 0
        message += "I have found {} teams, I will list some.".format(len(result))
        for team in result:
            count += 1
            message += str(team)
            message += "\n"
            if count == 4:
                break
    else:
        message += "Here is the result."
        for team in result:
            message += str(team)
            message += "\n"
    return message, result

##{'player_id': 308, 'player_name': 'D. Sturridge', 'firstname': 'Daniel Andre', 'lastname': 'Sturridge',
# #'number': None, 'position': 'Attacker', 'age': 31, 'birth_date': '01/09/1989', 'birth_place': 'Birmingham',
# #birth_country': 'England', 'nationality': 'England', 'height': '188 cm', 'weight': '76 kg'}
# 适用于搜索阵容和按照人名搜索球员
def explain_squad(response):
    if response is None:
        return "I have found no result", []
    if "error" in response["api"].keys():
        return "I have found no result.",[]
    players = response["api"]["players"]
    result = []
    count = 0
    for player1 in players:
        temp = PLAYER(id = player1["player_id"], name =player1["player_name"], firstname = player1["firstname"], lastname = player1["lastname"],
                      number = player1["number"], age = player1["age"], birth_date = player1["birth_date"], birth_place = player1["birth_place"],
                      birth_country = player1['birth_country'], nationality = player1['nationality'], height = player1["height"], weight = player1["weight"])
        result.append(temp)
        count += 1
        if count > 50:
            break
    message = ""
    print(result)
    if len(result) > 4:
        count = 0
        message += "I have found {} players, I will list some.".format(len(result))
        for player in result:
            count += 1
            message += str(player)
            message += "\n"
            if count == 4:
                break
    else:
        message += "Here is the result."
        for player in result:
            #message += str(player)
            message += str(player)
            message += "\n"
    return message, result


#{'player_id': 304, 'player_name': 'S. Mané', 'firstname': 'Sadio', 'lastname': 'Mané', 'position': 'Attacker',
# 'nationality': 'Senegal', 'team_id': 40, 'team_name': 'Liverpool',
# 'games': {'appearences': 36, 'minutes_played': 3086}, 'goals': {'total': 22, 'assists': 1, 'conceded': None, 'saves': None},
# 'shots': {'total': 87, 'on': 42}, 'penalty': {'won': 1, 'commited': None, 'success': 0, 'missed': 0, 'saved': None},
# 'cards': {'yellow': 2, 'second_yellow': 0, 'red': 0}}
def explain_topscorers(response):
    if response is None:
        return "I have found no result"
    if "error" in response["api"].keys():
        return "I have found no result."
    players = response["api"]["topscorers"]
    result = []
    for player in players:
        temp = PLAYER(id = player["player_id"], name =player["player_name"], team_id = player["team_id"], team_name = player["team_name"],
                      games = player["games"], goals = player["goals"], shots = player["shots"], penalty = player["penalty"],
                      nationality = player["nationality"], cards = player["cards"], position = player["position"],firstname = player["firstname"], lastname = player["lastname"])
        result.append(temp)
    message = ""
    if len(result) > 4:
        count = 0
        message += "I have found {} players, I will list some.".format(len(result))
        for player in result:
            count += 1
            message += str(player)
            message += "\n"
            if count == 4:
                break
    else:
        message += "Here is the result."
        for player in result:
            print(player)
            message += str(player)
            message += "\n"
    return message

#{'id': 1, 'name': 'J. Klopp', 'firstname': 'Jürgen', 'lastname': 'Klopp', 'age': 53, 'birth_date': '16/06/1967',
# 'birth_place': 'Stuttgart', 'birth_country': 'Germany', 'nationality': 'Germany', 'height': '191 cm', 'weight': '83 kg',
# 'team': {'id': 40, 'name': 'Liverpool'}, 'career': [{'team': {'id': 40, 'name': 'Liverpool'},
# 'start': 'October 2015', 'end': None}, {'team': {'id': 165, 'name': 'Borussia Dortmund'},
# 'start': 'July 2008', 'end': 'July 2015'}, {'team': {'id': 164, 'name': 'Mainz 05'}, 'start': 'February 2001', 'end': 'June 2008'}]}
def explain_coach(response):

    if response is None:
        return "I have found no result", []
    if "error" in response["api"].keys():
        return "I have found no result."
    coachs = response["api"]["coachs"]
    result = []
    for coach in coachs:
        temp = COACH(id = coach["id"], name =coach["name"], career = coach["career"], age = coach["age"],
                     firstname = coach["firstname"], lastname = coach["lastname"], team = coach["team"],
                     birth_date = coach["birth_date"], birth_place = coach["birth_place"], birth_country = coach["birth_country"],
                     height = coach["height"], weight = coach["weight"])
        result.append(temp)
    message = ""
    if len(result) > 4:
        count = 0
        message += "I have found {} coachs, I will list some.".format(len(result))
        for coach in result:
            count += 1
            message += str(coach)
            message += "\n"
            if count == 4:
                break
    else:
        message += "Here is the result."
        for coach in result:
            message += str(coach)
            message += "\n"
    return message, result

#{'player_id': 40, 'player_name': 'Andrés Felipe Solano Dávila', 'firstname': 'Andrés Felipe', 'lastname': 'Solano Dávila',
# 'number': None, 'position': 'Defender', 'age': 22, 'birth_date': '24/02/1998', 'birth_place': 'Santa Marta',
# 'birth_country': 'Colombia', 'nationality': 'Colombia', 'height': '176 cm', 'weight': '69 kg', 'injured': None, 'rating': None,
# 'team_id': 9570, 'team_name': 'Atlético Madrid II', 'league': 'Segunda B', 'season': '2019-2020', 'captain': 0,
# 'shots': {'total': 0, 'on': 0}, 'goals': {'total': 1, 'conceded': 0, 'assists': 0, 'saves': 0},
# 'passes': {'total': 0, 'key': 0, 'accuracy': 0}, 'tackles': {'total': 0, 'blocks': 0, 'interceptions': 0},
# 'duels': {'total': 0, 'won': 0}, 'dribbles': {'attempts': 0, 'success': 0}, 'fouls': {'drawn': 0, 'committed': 0},
# 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 0, 'commited': 0, 'success': 0, 'missed': 0, 'saved': 0},
# 'games': {'appearences': 16, 'minutes_played': 1274, 'lineups': 14}, 'substitutes': {'in': 2, 'out': 2, 'bench': 2}}
def explain_player_statistics(response):
    if response is None:
        return "I have found no result"
    if "error" in response["api"].keys():
        return "I have found no result."
    players = response["api"]["players"]
    result = []
    for player in players:
        temp = PLAYER(id = player["player_id"], name = player["player_name"], firstname = player["player_firstname"], lastname = player["lastname"], number = player["number"],
                      position = player["position"], age = player["age"], birth_date = player["birth_date"], birth_place = player["birth_place"],
                      birth_country = player["birth_country"], nationality = player["nationality"], height = player["height"], weight = player["weight"],
                      team_id = player["team_id"], team_name = player["team_name"], games = player["player_id"], rating = player["rating"],
                      goals = player["goals"], penalty = player["penalty"], cards = player["cards"], shots = player["shots"], passes = player["passes"],
                      tackles = player["tackles"], fouls = player["fouls"], duels = player["duels"], dribbles = player["dribbles"], substitues = player["substitues"])
        result.append(temp)
    message = ""
    if len(result) > 4:
        count = 0
        message += "I have found {} players, I will list some.".format(len(result))
        for player in result:
            count += 1
            message += str(player)
            message += "\n"
            if count == 4:
                break
    else:
        message += "Here is the result."
        for player in result:
            message += str(player)
            message += "\n"
    return message, result

#194205
def explain_fixture(response):
    if response is None:
        return "I have found no result", []
    if "error" in response["api"].keys():
        return "I have found no result."
    fixtures = response["api"]["fixtures"]
    result = []
    for fixture in fixtures:
        temp = FIXTURE( id = fixture["id"], league_id = fixture["league_id"], league_ = fixture["league"], event_date = fixture["event_date"],
                       firstHalfStart = fixture["firstHalfStart"], secondHalfStart = fixture["secondHalfStart"], round = fixture["round"],
                       status = fixture["status"], statusShort = fixture["statusShort"], elapsed = fixture["elapsed"],
                       venue = fixture["venue"], referee = fixture["referee"], hometeam = fixture["hometeam"], awayteam = fixture["awayteam"],
                       goalsHomeTeam = fixture["goalsHomeTeam"], goalsAwayTeam = fixture["goalsAwayTeam"], score = fixture["score"])
        result.append(temp)
    message = ""
    if len(result) > 4:
        count = 0
        message += "I have found {} coachs, I will list some.".format(len(result))
        for fixture in result:
            count += 1
            message += str(fixture)
            message += "\n"
            if count == 4:
                break
    else:
        message += "Here is the result."
        for fixture in result:
            message += str(fixture)
            message += "\n"
    return message, result

def explain_trophies(response, type):
    if response is None:
        return "I have found no result"
    if "error" in response["api"].keys():
        return "I have found no result."
    trophies = response["api"]["trophies"]
    message = ""
    if type == "player":
        hint = "The player"
    elif type == "coach":
        hint = "The coach"
    else:
        hint = ""
    for trophie in trophies:
        message += "{} is the {} 0f the {} in {} in the season {} ".format(hint, trophie["place"], trophie["league"], trophie["country"],trophie["season"])

    return message
#   {'type': 'Suspended', 'start': '26/02/20', 'end': '01/03/20'}
#   dict_keys(['results', 'sidelined'])
def explain_sidelined(response, type, limit = 4):
    if response is None:
        return "I have found no result"
    if "error" in response["api"].keys():
        return "I have found no result."
    sidelined = response["api"]["sidelined"]
    message = ""
    if type == "player":
        hint = "The player"
    elif type == "coach":
        hint = "The coach"
    else:
        hint = ""
    count = 0
    for sideline in sidelined:
        if sideline["type"] == "suspended":
            message += "{} was suspended from {} to {}".format(hint, sideline["start"], sideline["end"])
        else:
            message += "{} has {} from {} to {}.".format(hint, sideline["type"],sideline["start"], sideline["end"])
        count += 1
        if count > limit:
            break
    return message

#{'player_id': 384, 'player_name': 'M. Loum', 'transfer_date': '2019-07-01', 'type': '€ 7.5M',
#  'team_in': {'team_id': 212, 'team_name': 'FC Porto'}, 'team_out': {'team_id': 217, 'team_name': 'SC Braga'},
# 'lastUpdate': 1598414641}
def explain_transfer(response, limit = 4):
    if response is None:
        return "I have found no result"
    if "error" in response["api"].keys():
        return "I have found no result."
    transfers = response["api"]["transfers"]
    message = ""
    count = 0
    for transfer in transfers:
        message += "{} transfered from {} to {} on {}, with {}.".format(transfer["player_name"], transfer["team_out"]["team_name"],
                                                                        transfer["team_in"]["team_name"], transfer["transfer_date"], transfer["type"])
        count += 1
        if count > limit:
            break
    return message