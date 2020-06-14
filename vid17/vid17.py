# a list of dictionaries is a data structure

allCats = []
allCats.append({'name': 'Alice', 'age': 3, 'color': 'red'})
allCats.append({'name': 'Blake', 'age': 4, 'color': 'blue'})
allCats.append({'name': 'Elliot', 'age': 5, 'color': 'green'})
allCats.append({'name': 'Quintin', 'age': 6, 'color': 'orange'})

print(allCats)
print(allCats[1])
print(allCats[1].get('name'))
print(list(allCats[1].items()))