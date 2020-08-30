import sqlite3
import requests
#   "https://api-football-v1.p.rapidapi.com/v2/leagues"
conn = sqlite3.connect('football.db')
c =conn.cursor()
#再create table之前先把之前的table删除
c.execute('drop table league')
c.execute('create table league(id PRIMARY KEY , name, country, season,  starttime , endtime , logolink )')

URL_football = "https://api-football-v1.p.rapidapi.com/"
headers = {
   'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
   'x-rapidapi-key': "c984d7fe6amsh8a35f5e8b7643adp12a5e1jsn991163475fcd"
   }
url = URL_football + "leagues"
response = requests.request("GET", url,headers = headers)
result = response.json()

print(response)
print("-------------------------------------------------------------------------------------------")
print(result)
print("--------------------------------------------------------------------------------------------")

temp = result["api"]["leagues"]
i = 0
for item in temp.keys():
    c.execute('insert into league values(?,?,?,?,?,?,?)',
              (temp[item]["league_id"],temp[item]["name"],temp[item]["country"], temp[item]["season"],
               temp[item]["season_start"], temp[item]["season_end"], temp[item]["logo"] ))


conn.commit()
conn.close()

