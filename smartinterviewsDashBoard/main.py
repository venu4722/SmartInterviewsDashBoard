import csv
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
database = json.load(open('database.json'))
marks = json.load(open('marks.json'))
DashBoard = {}

def create_excel():
    pass



def calculate_score(d,platform):
    score = 0
    for i in d:
        score += marks[platform][i] * int(d[i])
    return score

DashBoard  ={}

a = time.time()
for i in database:
    username = i
    DashBoard[i] ={}
    score = {}
    total_score = 0
    for profile in database[username]:
        if database[username][profile]=="":
            DashBoard[username][profile] = 0
            continue
        req = requests.get(database[username][profile])
        soup = BeautifulSoup(req.content, 'html.parser')
        problems = {}
        score = 0
        if profile =='leetcode':
            key = True
            for item in soup.find_all('div', {'w-[53px] text-label-3 dark:text-dark-label-3','flex flex-1 items-center'}):
                if key:
                    temp = item.text.lower()
                    if temp in marks['leetcode']:
                        problems[temp] = 0
                        key = False
                else:
                    key = True
                    problems[temp] = item.text.split('/')[0]

        elif profile=='gfg':
            for i in soup.find_all(class_='tab'):
                temp = i.text
                problems[temp.split('(')[0].lower()[:-1]] = temp.split('(')[1].split(')')[0]

        temp = calculate_score(problems,profile)
        #print(username,problems,temp)
        DashBoard[username][profile] = temp
        total_score += temp
    DashBoard[username]['Total_Score'] = total_score

#print(time.time()-a)
#print(DashBoard)
data = DashBoard.values()
df = pd.DataFrame(data, index=DashBoard.keys())
#print(df.head())

df.sort_values(by = 'Total_Score',inplace = True,ascending=False)
#print(df.head())
df.to_csv('smartinterviewsscore.csv')
