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
a = PLAYER(name = '123', id= '123')
temp = []
temp.append(a)
print(str(a))
b = PLAYER(name='234', lastname='234')
temp.append(b)
message = ""
for c in temp:
    message += str(c)
print(message)
print(str(a)+str(b))