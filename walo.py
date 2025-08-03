import random 
from barcelona import barcelona_players
a = (random.choice(barcelona_players))
b = (random.choice(barcelona_players))
adam = input(f"is better {a} than {b}?")
best_player=[]
if(adam=="yes"):
	best_player.append(a)
else:
	best_player.append(b)
print(best_player)
