#from a list, print every barcelona player
barcelona_players = [
"Lionel Messi",
"Xavi Hernandez",
"Andres Iniesta",
"Ronaldinho",
"Samuel Eto'o",
"Carles Puyol",
"Diego Maradona",
"Gerard Pique",
"Neymar",
"Thierry Henry",
"Frenkie de Jong",
"Pedri",
"Lamine Yamal"
# ... (extend as needed for more historical players)
]
import random
print(random.choices(barcelona_players, weights = [10, 1, 1], k = 14))
