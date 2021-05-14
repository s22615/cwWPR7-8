import random

# 1
names = ("Franek", "Marek", "Zbyszek", "Asia", "Basia", "Kasia")
print(names)
# 2
surnames = ("Banach", "Currie", "Kowalski", "Studencki")
print(surnames)

# 3
for x in names:
    if x[-1] == 'a':
        print(x)


# 4
def llps(s):
    polski_suffix = ("ski", "cki")
    for each in polski_suffix:
        if s.endswith(each):
            return True
    return False


# 5
for each in surnames:
    if llps(each):
        print(each)


# 6
def filtracjaPolaczkow(zestNazw):
    listaPolaczkow = []
    for each in surnames:
        if llps(each):
            listaPolaczkow.append(each)
    return listaPolaczkow


print(filtracjaPolaczkow(surnames))

# 7
people = []

for n in names:
    for s in surnames:
        people.append((n, s,))

for each in people:
    print(each)

#
print("================================")
# 8
for n in names:
    for s in surnames:
        if n[-1] == 'a' and llps(s):
            s = s[:-1] + 'a'
            people.append((n, s,))
            print(n, s)

#
print("================================")


# 9
def create_a_person(names, surnames):
    x = random.randint(0, len(names) - 1)
    random_name = names[x]
    y = random.randint(0, len(surnames) - 1)
    random_surnames = surnames[y]
    if random_name[-1] == 'a' and llps(random_surnames):
        random_surnames - random_surnames[:-1] + 'a'
    return f"{random_name} {random_surnames}"


print(create_a_person(names, surnames))

#
print("================================")


# 10
