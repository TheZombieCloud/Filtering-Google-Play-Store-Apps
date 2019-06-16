import csv
from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1

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
        return str(self._name)

class Interface:
    def __init__(self):
        pass
    def choice1(self):
        print ("|                                              |")
        print ("|   Chooose a Rating and No. of Reviews        |")
        print ("|                                              |")
        print ("|   Rating (0-5)(Up to 1 Decimal Place ex. 4.1)|")
        print ("|   No. of Reviews (Integer)                   |")
        print ("|                                              |")
        print ("|                                              |")
    def choice2(self):
        print ("|                                              |")
        print ("|      Choose a Content Rating and Price       |")
        print ("|                                              |")
        print ("|      Content Rating: Everyone, Teen,         |")
        print ("|      Mature 17+, Adults only 18+             |")
        print ("|                                              |")
        print ("|      Price: Paid, Free                       |")
        return("|                                              |")
    def __str__(self):
        print ("|          Google Play Apps Filtering          |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|    1. Filter by Rating and No. of Reviews    |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|    2. Filter by Content Rating and Price     |")
        print ("|       (Paid or Free)                         |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|    Enter the Number of the Option you wish   |")
        print ("|              to choose (1 or 2).             |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|                                              |")
        print ("|                                              |")
        return("|                                              |")
    

Ratings = {}
Ratingss = {}
ContentandPrice = {}

with open("googleplaystore.csv", encoding = "Latin-1") as filein:
    reader = csv.DictReader(filein)
    counter = 0
    for line in reader:
        counter += 1
        if counter == 10473:
            continue
        AppObject = Game(line["App"], line["Category"], line["Rating"], line["Reviews"], line["Size"], line["Installs"], line["Type"], line["Price"], line["Content Rating"], line["Genres"], line["Last Updated"], line["Current Ver"], line["Android Ver"])
        Ratings.setdefault(line["Rating"], [])
        Ratings[line["Rating"]].append(AppObject)
        Ratingss.setdefault(line["Rating"], [])
        Ratingss[line["Rating"]].append(int(line["Reviews"]))
        ContentandPrice.setdefault(line["Content Rating"], {})
        ContentandPrice[line["Content Rating"]].setdefault(line["Type"], [])
        ContentandPrice[line["Content Rating"]][line ["Type"]].append(AppObject)

for i in Ratings.keys():
    Ratings[i].sort(key = lambda x: int(x._reviews))
    Ratingss[i].sort(key = lambda x: int(x))

interface = Interface()
print(interface)
choice = int(input("Your choice: "))
if choice == 2:
    interface.choice2()
    rating = input("Content Rating: ")
    typep = input("Price: ")
    print("-"*30)
    ContentandPrice[rating][typep].sort(key = lambda x: x._name.upper())
    for i in ContentandPrice[rating][typep]:
        print(i)
elif choice == 1:
    interface.choice1()
    Rating = float(input("Rating: "))
    start = int(input("Starting No. of Reviews: "))
    end = int(input("Ending No. of Reviews: "))
    print("-"*30)
    arr2 = Ratings[str(Rating)]
    arr = Ratingss[str(Rating)]
    if not arr:
        print ("No apps exist with that rating")
    else:
        index = BinarySearch(arr, start)
        index += 1
        arr3 = []
        for i in range (index, len(arr)):
            if arr[i] > end:
                break
            arr3.append(arr2[i])
        arr3.sort(key = lambda x: x._name.upper())
        for i in arr3:
            print(i)
        
    
    

        
        
        
        
