print("hello world!")

# cree les variables

nom = "Tony"
age = "32"
taille = 1.80

# afficher variables

print("Mon nom est :", nom)
print("Mon age est :", age)
print("Ma taille est :", taille)

# operation arithmetique

a = 15
b = 5

add = a+b
sous = a-b
div = a/b
multi = a*b

print("add result : ",add)
print("sous result : ",sous)
print("div result : ",div)
print("multi result : ",multi)

# les boucles

for i in range(5):
    print("repetition", i)

# les conditions

age = 32

if age >= 18:
    print("Tu es majeur!!!")
else:
    print("Tu est mineur!!!")

nombre = 31

if nombre %2:
    print("nombre impair")
else:
    print("nombre pair")

# les fonctions

def multi(a,b):
    return a * b

resultat = multi(5,9)

print(resultat)

# les collections

jours = "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"

i = 0
for jour in jours:
    print(i, jour)
    i += 1

#or

for i in range(len(jours)):
    print(i, jours[i])

#or

for i, jour in enumerate(jours,start = 1):
    print(i, jour)
