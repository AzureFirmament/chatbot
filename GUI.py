from tkinter import *
import tkinter.font as tf
import spacy
import random
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import content
import re
#   训练
trainer = Trainer(config.load("config_spacy.yml"))
training_data = load_data('train.json')
interpreter = trainer.train(training_data)
nlp = spacy.load("en_core_web_md")

#   缓存设置
player_result = [content.PLAYER()]
team_result = [content.TEAM()]
league_result = [content.LEAGUE()]
coach_result = [content.COACH()]
fixture_result = [content.FIXTURE()]


#   状态参数
INIT = 0
SEARCH_PLAYER = 1
SEARCH_LEAGUE = 2
SEARCH_TEAM = 3
SEARCH_COACH = 4
SEARCH_FIXTURE = 5
SEARCH_TRANSFER = 6
SEARCH_STATISTICS = 7
SEARCH_SIDELINE = 8
SEARCH_TROPHIE = 9
SEARCH_TOPSCORER = 10
status = INIT

policy ={
    (INIT, "search_player"):(SEARCH_PLAYER, "Who do you want to search?"),
    (INIT, "search_league"):(SEARCH_LEAGUE, "Which league do you want to search?"),
    (INIT, "search_coach"):(SEARCH_COACH, "Who do you want to know about?"),
    (INIT, "search_team"):(SEARCH_TEAM, "Which team do you want to search?"),
    (INIT, "None"):(INIT, "What can I do for you?"),
    (SEARCH_PLAYER, "search_trophie"):(SEARCH_TROPHIE, "whose trophies do you want to search?"),
    (SEARCH_PLAYER, "search_sideline"):(SEARCH_SIDELINE, "Whose sideline do you want to search?"),
    (SEARCH_PLAYER, "search_statistics"):(SEARCH_STATISTICS, "Whose statistics do you want to learn?"),
    (SEARCH_PLAYER, "search_transfer"):(SEARCH_TRANSFER, "Whose transfer do you want to search?"),
    (SEARCH_PLAYER, "None"):(INIT, "How can I help you?"),
    (SEARCH_COACH, "search_trophie"):(SEARCH_TROPHIE, "Whose trophies do you want to search?"),
    (SEARCH_COACH, "search_sideline"):(SEARCH_SIDELINE, "Whose sideline do you want to search?"),
    (SEARCH_COACH, "None"):(INIT, "How can I help you?"),
    (SEARCH_LEAGUE, "search_team"):(SEARCH_TEAM, "Which league do you want to search?"),
    (SEARCH_LEAGUE, "search_topscorer"):(SEARCH_TOPSCORER, "Which league do you want to search?"),
    (SEARCH_LEAGUE, "None"):(INIT, "What can I do for you?"),
    (SEARCH_TEAM, "search_squad"):(SEARCH_PLAYER, "Which team and season do you want to search?"),
    (SEARCH_TEAM, "search_coach"):(SEARCH_COACH, "Which team do you want to search?"),
    (SEARCH_TEAM, "search_fixture"):(SEARCH_FIXTURE, "which match do you want to search?"),
    (SEARCH_TEAM, "search_league"):(SEARCH_LEAGUE, "which league do you want to search?"),
    (SEARCH_TEAM, "search_statistics"):(SEARCH_STATISTICS, "which team do you want to search?"),
    (SEARCH_TEAM, "search_transfer"):(SEARCH_TRANSFER, "which team do you want to search?"),
    (SEARCH_TEAM, "None"):(INIT, "How can I help you?"),
    (SEARCH_FIXTURE, "None"):(INIT, "How can I help you?"),
    (SEARCH_TRANSFER, "None"):(INIT, "How can I help you?"),
    (SEARCH_STATISTICS, "None"):(INIT, "What can I do for you?"),
    (SEARCH_SIDELINE, "None"):(INIT, "What can I do for you?"),
    (SEARCH_TROPHIE, "None"):(INIT, "What can I do for you?"),
    (SEARCH_TOPSCORER, "None"):(INIT, "What can I do for you?")
}

normal = {
    'greet':['hello bro!','nice to see you, my friends.', 'glad to meet you!'],
    'goodbye':['good bye', 'ByeBye', 'see you next time']
}

application = {
    'search_league': [content.search_league, content.explain_league],
    'search_team': [content.search_team, content.explain_team],
    'search_player':[content.search_player, content.explain_squad],
    'search_squad':[content.search_squad, content.explain_squad],
    'search_transfer':[content.search_transfer, content.explain_transfer],
    'search_coach':[content.search_coach, content.explain_coach],
    'search_trophy':[content.search_trophies, content.explain_trophies],
    'search_statistics':[content.search_player_statistics, content.explain_player_statistics],
    'search_sideline':[content.search_sideline, content.explain_sidelined],
    'search_topscorer':[content.search_topscorer, content.explain_topscorers],
    'search_fixture':[content.search_fixture, content.explain_fixture]
}


def get_intent(message):
    entities = interpreter.parse(message)
    intent = entities['intent']['name']
    if "transfer" in message.lower():
        intent = "search_transfer"
    if "trophy" in message.lower() or "trophies" in message.lower():
        intent = "search_trophy"
    if "statistics" in message.lower():
        intent = "search_stastistics"
    if "sideline" in message.lower():
        intent = "search_sideline"
    if "squad" in message.lower():
        intent = "search_squad"
    if "topscorer" in message.lower():
        intent = "search_topscorer"
    if "matches" in message.lower():
        intent = "search_fixture"
    if "coach" in message.lower():
        intent = "search_coach"
    return intent

def search_league(message):
    global league_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'GPE'or ent.label_ == 'ORG'or ent.label_ == "DATE":
            params[ent.label_] = ent.text.lower()
    temp = None
    if "DATE" in params.keys():
        if "GPE" in params.keys():
            temp = application["search_league"][0](country=params["GPE"], season = params["DATE"])
        elif "ORG" in params.keys():
            temp = application["search_league"][0](country=params["ORG"], season=params["DATE"])
    else:
        if "GPE" in params.keys():
            temp = application["search_league"][0](country=params["GPE"])
        elif "ORG" in params.keys():
            temp = application["search_league"][0](country=params["ORG"])
    hint,league_result = application["search_league"][1](temp)
    return hint

def search_player(message):
    global player_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        print(ent, ent.label_)
        if ent.label_ == 'PERSON':
            params[ent.label_] = ent.text.lower()
    temp = None
    if "PERSON" in params.keys():
        temp = application["search_player"][0](lastname = params["PERSON"])
    hint, player_result = application["search_player"][1](temp)
    return hint

def search_squad(message):
    global team_result,player_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'ORG' or ent.label_ == "DATE":
            params[ent.label_] = ent.text.lower()
    temp = None
    if "ORG" in params.keys():
        name = params["ORG"]
        id = None
        name =re.compile(name)
        for team in team_result:
            if re.search(name,team.name) :
                id = team.id
                break
        if "DATE" in params.keys():
            temp =  application["search_squad"][0](team_id = id, season = params["DATE"])
        else:
            temp = application["search_squad"][0](team_id = id)
    hint, player_result = application["search_squad"][1](temp)
    return hint

#   false指联赛id搜索
def search_team(message, type = True):
    global team_result,league_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'ORG' or ent.label_ == "GPE":
            params[ent.label_] = ent.text.lower()
    temp = None
    if not type:
        id = None
        if "ORG" in params.keys():
            name = params["ORG"]
            name = re.compile(name)
            for league in league_result:
                if re.search(name,league.name):
                    id = league.id
                    break
        temp = application["search_team"][0](league_id = id)

    else:
        if "ORG" in params.keys():
            temp = application["search_team"][0](name = params["ORG"])
        elif "GPE" in params.keys():
            temp = application["search_team"][0](country = params["GPE"])
    hint, team_result = application["search_team"][1](temp)
    return hint

#   True指球员
def search_transfer(message, type = True):
    global player_result, coach_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            params[ent.label_] = ent.text.lower()
    temp = None
    if type:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            name = re.compile(name)
            for player in player_result:
                if re.search(name,player.name) or re.search(name,player.firstname) or re.search(name,player.lastname):
                    id = player.name
                    break
            temp = application["search_transfer"][0](player_id = id)
    else:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            for coach in coach_result:
                if re.search(name,coach.name):
                    id = coach.name
                    break
            temp = application["search_transfer"][0](coach_id = id)
    hint = application["search_transfer"][1](temp)
    return hint

def search_coach(message):
    global coach_result, team_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'ORG'or ent.label_ == "PERSON" or ent.label_ == "PRODUCT":
            params[ent.label_] = ent.text.lower()
    temp = None
    print(params)
    if "PERSON" in params.keys():
        name = params["PERSON"]
        temp = application["search_coach"][0](coach_name = name)
    elif "PRODUCT" in params.keys():
        name = params["PRODUCT"]
        temp = application["search_coach"][0](coach_name = name)
    elif "ORG" in params.keys():
        name = params["ORG"]
        id = None
        name = re.compile(name)
        for team in team_result:
            if re.search(name,team.name):
                id = team.id
                break
        temp = application["search_coach"][0](team_id = id)
    hint, coach_result = application["search_coach"][1](temp)
    return hint
# TRUE指球员
def search_trophy(message, type = True):
    global player_result, coach_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            params[ent.label_] = ent.text.lower()
    temp = None
    if type:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            name = re.compile(name)
            for player in player_result:
                if re.search(name,player.name) or re.search(name,player.firstname) or re.search(name,player.lastname):
                    id = player.name
                    break
            temp = application["search_trophy"][0](player_id=id)
    else:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            name = re.compile(name)
            for coach in coach_result:
                if re.search(name,coach.name):
                    id = coach.name
                    break
            temp = application["search_trophy"][0](coach_id=id)
    hint = application["search_trophy"][1](temp)
    return hint

#   True指球员, false 指队伍
def search_statistics(message, type = True):
    global player_result, coach_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'PERSON' or ent.label_ == "DATE" or ent.label_ == "ORG":
            params[ent.label_] = ent.text.lower()
    temp = None
    if type:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            name = re.compile(name)
            for player in player_result:
                if re.search(name,player.name) or re.search(name,player.firstname) or re.search(name,player.lastname):
                    id = player.id
                    break
            if "DATE" in params.keys():
                temp = application["search_statistics"][0](player_id=id, season=params["DATE"])
            else:
                temp = application["search_statistics"][0](player_id=id)
    else:
        if "ORG" in params.keys():
            name = params["ORG"]
            id = None
            name = re.compile(name)
            for team in team_result:
                if re.search(name,team.name):
                    id = team.id
                    break
            if "DATE" in params.keys():
                temp = application["search_statistics"][0](team_id=id, season=params["DATE"])
            else:
                temp = application["search_statistics"][0](team_id=id)
    hint, player_result = application["search_statistics"][1](temp)
    return hint
#   true指球员
def search_sideline(message, type = True):
    global player_result, coach_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            params[ent.label_] = ent.text.lower()
    temp = None
    if type:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            name = re.compile(name)
            for player in player_result:
                if re.search(name, player.name) or re.search(name, player.firstname) or re.search(name,player.lastname):
                    id = player.name
                    break
            temp = application["search_sideline"][0](player_id=id)

    else:
        if "PERSON" in params.keys():
            name = params["PERSON"]
            id = None
            name = re.compile(name)
            for coach in coach_result:
                if re.search(name, coach.name):
                    id = coach.name
                    break
            temp = application["search_sideline"][0](coach_id=id)
    hint = application["search_sideline"][1](temp)
    return hint

def search_topscorers(message):
    global league_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'ORG' or ent.label_ == "DATE":
            params[ent.label_] = ent.text.lower()
    temp = None
    id = None
    if "ORG" in params.keys():
        name = params["ORG"]
        name = re.compile(name)
        for league in league_result:
            if re.search(name, league.name):
                id = league.id
                break
        temp = application["search_topscorer"][0](league_id = id)
    hint = application["search_topscorer"][1](temp)
    return hint

def search_fixture(message):
    global team_result, fixture_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    params = {}
    for ent in doc.ents:
        if ent.label_ == 'ORG' :
            params[ent.label_] = ent.text.lower()
    temp = None
    if "ORG" in params.keys():
        name = params["ORG"]
        name = re.compile(name)
        for team in team_result:
            if re.search(name, team.name):
                id = team.id
                break
        temp = application["search_fixture"][0](team_id = id)
    hint, fixture_result = application["search_fixture"][1](temp)
    return hint

part = {
    'search_league': search_league,
    'search_team': search_team,
    'search_player':search_player,
    'search_squad':search_squad,
    'search_transfer':search_transfer,
    'search_coach':search_coach,
    'search_trophy':search_trophy,
    'search_statistics':search_statistics,
    'search_sideline':search_sideline,
    'search_topscorer':search_topscorers,
    'search_fixture':search_fixture,
    'None':None,
    'affirm': None,
    'greet':random.choice(normal['greet']),
    'goodbye':random.choice(normal['goodbye'])
}
def respond(message):
    global status, player_result, league_result, team_result,coach_result, fixture_result
    entities = interpreter.parse(message)
    doc = nlp(message)
    intent = get_intent(message)
    #status, hint = policy[(status, intent)]
    if part[intent] is not None:
        output = part[intent](message)
        User_txt.delete(1.0, END)
        Bot_txt.insert(END, output)
    else:
        User_txt.delete(1.0, END)
        Bot_txt.insert(END, "How can I help You?")

    return entities["intent"], entities, doc.ents

def  debug(event):
    global status, player_result, league_result, team_result, coach_result, fixture_result
    message = User_txt.get(1.0, END)
    entities = interpreter.parse(message)
    doc = nlp(message)
    #intent = 'league_search'
   # print(entities['intent']['name'])
    #for ent in doc.ents:
    #    print(ent.label_)
    #    print(ent.text)
    #print(doc.ents)
   # print(entities["entities"])
    intent = get_intent(message)
    print(status, intent)
    if intent == "greet" or intent == "goodbye":
        bot_message = random.choice(normal[entities['intent']['name']])
        Bot_txt.insert(END, bot_message)
        User_txt.delete(1.0, END)
        return
    if (status, intent) not in policy.keys() :
        status = INIT
        if entities['intent']['name'] != "affirm":
            hint = "I cannot understand what you are saying. Please repeat or try other sayings."
            Bot_txt.insert(END, hint)
        else:
            hint = "so you need any other help?"
            Bot_txt.insert(END, hint)
    else:
        #print("check")
        status, hint = policy[(status, intent)]
        hint = part[intent](message)
        Bot_txt.insert(END, hint)
    #Bot_txt.insert(END, "status: {}".format(status))
    #if intent in application:
    #    for ent in doc.ents:
    #        if ent.label_ == 'GPE':
    #            print('check!')
    #            temp = application[intent][0](country=ent.text.lower())
    #            message = application[intent][1](temp)
    #            Bot_txt.insert(END, message)
    #            Bot_txt.insert(END, '\n')

    #    return

    User_txt.delete(1.0, END)

def send(event):
    message = User_txt.get(1.0, END)
    #Bot_txt.insert(END, message)
    intent, entities,doc = respond(message)
    #print(intent["name"])
    if entities['intent']['name'] in normal.keys():
        bot_message = random.choice(normal[entities['intent']['name']])
        Bot_txt.insert(END, bot_message)
        Bot_txt.insert(END, '\n')
        return
    Bot_txt.insert(END, str(intent["name"]))
    Bot_txt.insert(END,'\n')
    Bot_txt.insert(END,str(intent["confidence"]))
    Bot_txt.insert(END,'\n')
    Bot_txt.insert(END,entities)
    Bot_txt.insert(END,'\n')
    for ent in doc:
        Bot_txt.insert(END, "{} : {}".format(ent.label_, ent.text))
        Bot_txt.insert(END, '\n')
    #Bot_txt.insert(END, doc)
    #Bot_txt.insert(END, '\n')

    #Bot_txt.insert(END,str(entities['entity']))
    #User_txt.delete(1.0, END)

def delete(event):
    Bot_txt.delete(1.0, END)

root = Tk()
root.geometry('1000x800')
root.title("聊天机器人")
label1 = Label(root, text = "user message")
label1.place(relx=0.1, rely=0, relwidth=0.1, relheight=0.1)
Label2 = Label(root, text = "robot message")
Label2.place(relx=0.1, rely=0.5, relwidth=0.1, relheight=0.1)
User_txt = Text(root)
User_txt.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.3)
Bot_txt = Text(root)
Bot_txt.place(relx = 0.1, rely = 0.6, relwidth = 0.8, relheight = 0.3)
bn1 = Button(root, text = "send")
bn1.place(relx = 0.5, rely = 0.025, relwidth = 0.1, relheight = 0.05)
bn1.bind("<Button-1>", debug)
bn2 = Button(root, text = "delete bot message")
bn2.place(relx = 0.4, rely = 0.525, relwidth = 0.2, relheight = 0.05)
bn2.bind("<Button-1>", delete)

root.mainloop()