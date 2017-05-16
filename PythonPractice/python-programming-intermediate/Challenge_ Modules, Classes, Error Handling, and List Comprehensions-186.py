## 2. Introduction to the Data ##

import csv

f = open("nfl_suspensions_data.csv", 'r')
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:]

years ={}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] += 1
    else: 
        years[row_year] = 1

print (years)

## 3. Unique Values ##

team =[]
for row in nfl_suspensions:
    team.append(row[1])

unique_teams = set(team)

games =[]
for row in nfl_suspensions:
    games.append(row[2])

unique_games = set(games)

print (unique_teams)
print (unique_games)

## 4. Suspension Class ##

import csv

class Suspension():
    #reads the data from nfl_suspensions_data.csv, stores it in the new property via init method
    def __init__(self):
        self.nfl = list(nfl_suspensions)
        
    def name(self):
        for row in self.nfl:
            name = row[0]
        return name
    
    def team(self):
        for row in self.nfl:
            team = row[1]
        return team
    
    def year(self):
        for row in self.nfl:
            year = row[5]
            
third_suspension = Suspension()        
# correct solution

'''class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2] 
        self.year = row[5]
third_suspension =Suspension(nfl_suspensions[2]) '''

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
           self.year = int(row[5])
        except Exception:
               self.year = 0
     
    def get_year(self):
        return self.year

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()       


        