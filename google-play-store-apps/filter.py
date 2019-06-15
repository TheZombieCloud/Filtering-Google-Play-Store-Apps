import csv

class Game:
    def __init__(self, name, category, rating, reviews, size, installs, type2, price, content, genre, update2, cversion, aversion):
        self._name = name
        self._category = category
        self._rating = rating
        self._reviews = reviews
        self._size = size
        self._installs = installs
        self._type = type2
        self._price = price
        self._content = content
        self._genre = genre
        self._update = update2
        self._cversion = cversion
        self._aversion = aversion
    def __str__(self):
        return str("Reviews: " + self._reviews)



Objects = []

Ratings = {}

with open("googleplaystore.csv", encoding = "Latin-1") as filein:
    reader = csv.DictReader(filein)
    counter = 0
    for line in reader:
        counter += 1
        if counter == 10473:
            continue
        AppObject = Game(line["App"], line["Category"], line["Rating"], line["Reviews"], line["Size"], line["Installs"], line["Type"], line["Price"], line["Content Rating"], line["Genres"], line["Last Updated"], line["Current Ver"], line["Android Ver"])
        Objects.append(AppObject)
        Ratings.setdefault(line["Rating"], [])
        Ratings[line["Rating"]].append(AppObject)

for i in Ratings.keys():
    Ratings[i].sort(key = lambda x: int(x._reviews))
    for _ in Ratings[i]:
        print (_)
    print("\n")
        
        
        
        
