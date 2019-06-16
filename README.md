# Filtering Google Play Store Apps

A basic filtering program that filters Google Play Store Apps in multiple ways.

## Data Overview

My data is sourced from a CSV file from Kaggle.com. It contains over 10 000+ apps with information about each one of them. This information includes the App Name, Category, Rating, Number of Reviews, Size, Number of Installs, Type, Price, Content Rating, Genres, Last Update Date, Current Version, and Minimum Android Version.

App Name - Name of the Application (eg. Arrow Switch)  
Category - Category the App Belongs to (eg. Game)  
Rating - User Rating of the App (eg. 4.1)  
Number of Reviews - The number of Reviews the App has received (eg. 7)  
Size - The download size of the app (eg. 39M)  
Number of Installs - The number of installs the App has received (eg. 100,000+)  
Type - Paid or Free (eg. Free)  
Price - The price of the app in USD (eg. $0.99)  
Content Rating - Rating based on the app's target demographic (eg. Everyone)  
Genres - More specific than the Category attribute. Acts like tags. (eg. Art & Design)  
Last Update Date - The date of which the app was last updated (eg. August 1st, 2018)  
Current Version - Current Version of the App (eg. 1.2.4)  
Minimum Android Version - The minimum required Android OS version needed to be able to run the application (eg. 4.1 and up)  

More info can be found on Kaggle.com: https://www.kaggle.com/lava18/google-play-store-apps

## Data Structures

The data structures I used include a dictionary of dictionaries of lists of objects, and two dictionaries of lists. Let's call the first data structure I used "Data A" and the second data structure I used "Data B" for simplicity. I used Data B to store objects for use if the user were to choose the 1st filtering option. The first Data B data structure is used to store the objects, with the second used to store the number of reviews. The first data structure is created to print the objects to console when filtered, with the second data structure used so Python's built-in binary search actually works. I used Data A to store objects for the second filtering option. The nested dictionaries are used for ease of convenience and lower time complexity. The lists in the dictionaries stores the objects that will be printed to console depending on what the user wants to filter for the second filtering option.
