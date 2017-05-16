## 1. The Data Set ##

# Weather has been loaded in.
print (weather[0])
print (weather[-1])

## 3. Practice Populating a Dictionary ##

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]

## 4. Practice Indexing a Dictionary ##

random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)
animals ={
    7: "raven", 
    8: "goose",
    9: "duck"
}

times ={
    "morning": 9,
    "afternoon": 14,
    "evening": 19,
    "night": 23
}

## 5. Defining a Dictionary with Values ##

students = {
    "Tom": 60,
    "Jim": 70
}

students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5

## 6. Modifying Dictionary Values ##

students = {
    "Tom": 60,
    "Jim": 70
}

students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5

## 7. The In Statement and Dictionaries ##

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers

## 9. Practicing with the Else Statement ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for item in planet_names:
    x = len(item)
    if x > 5:
        long_names.append(item)
    else:
        short_names.append(item)

## 10. Counting with Dictionaries ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for item in planet_names:
    x = len(item)
    if x > 5:
        long_names.append(item)
    else:
        short_names.append(item)

## 11. Counting the Weather ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for item in planet_names:
    x = len(item)
    if x > 5:
        long_names.append(item)
    else:
        short_names.append(item)