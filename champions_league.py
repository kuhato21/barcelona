champions_league_teams = [
    "Real Madrid",
    "Manchester City",
    "Bayern Munich",
    "Paris Saint-Germain",
    "Inter Milan",
    "Arsenal",
    "Barcelona",
    "Atlético Madrid",
    "Juventus",
    "Liverpool",
    "RB Leipzig",
    "Borussia Dortmund",
    "Bayer Leverkusen",
    "AC Milan",
    "Napoli",
    "Benfica",
    "Porto",
    "Sporting CP",
    "Feyenoord",
    "Ajax",
    "PSV Eindhoven",
    "Celtic",
    "Galatasaray",
    "Shakhtar Donetsk",
    "Red Bull Salzburg",
    "Club Brugge",
    "Rangers",
    "Lazio",
    "Union Berlin",
    "Lens",
    "Real Sociedad",
    "Copenhagen"
]
import random
a = (random.choice(champions_league_teams))
b = (random.choice(champions_league_teams))
#adam = input(f"who win {a} or {b}")
best_team=[]

def round(champ_league_team):
	round_result=[]
	for i in range(0,len(champ_league_team),2):
		x=input(f"did {champ_league_team[i]} win against {champ_league_team[i+1]}")
		if x== "yes":
			round_result.append(champ_league_team[i])
		elif x=="no":
			round_result.append(champ_league_team[i+1])
	return round_result
winners=champions_league_teams
while len(winners)!=1:
	winners=round(winners)
	print("Round Over. Starting next round.....")
	if "Barcelona" in winners:
		print("Barcelona is still winning lets go!")
	else:
		print(" HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH ")
print(winners)
