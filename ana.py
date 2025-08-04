participite = []
x= int(input("enter a random number"))
print(x)
for i in range (1, x+1):
    g= input("give team n¹")
    participite.append(g)

import random
a = (random.choice(participite))
b = (random.choice(participite))
#adam = input(f"who win {a} or {b}")
best_team=[]

def round(champ_league_team):
        round_result=[]
        for i in range(0,len(champ_league_team),2):
                x=input(f"did {champ_league_team[i]} win against {champ_league_team[i+1]}")
                if x== "yes":
                        round_result.append(champ_league_team[i])
                elif x=="no":
                        round_result.append(champ_league_team[i])
        return round_result
winners=participite
while len(winners)!=1:
        winners=round(winners)
        print("Round Over. Starting next round.....")
print(winners)
