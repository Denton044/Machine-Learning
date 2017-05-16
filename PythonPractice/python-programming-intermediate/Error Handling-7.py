## 2. Sets ##

gender = []
for i in legislators:
    gender.append(i[3])
gender = set(gender)
print (gender)

## 3. Exploring the Dataset ##

party = []
for i in legislators:
    party.append(i[6])
party = set(party)
print (party)
print (legislators)

## 4. Missing Values ##

for i in legislators:
    if i[3] == "":
        i[3] = "M"

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    parts = row[2].split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float('hello')
except Exception:
    print ("Error converting to float.")

## 7. Exception Instances ##

try:
    int('')
except Exception as e:
    print(type(e))
    print(str(e))

## 8. The Pass Keyword ##

converted_years = []
for i in birth_years:
    year = i
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##

for row in legislators:
    parts = row[2].split("-")
    try:
        birth_year = int(parts[0])
    except Exception:
        birth_year = 0
    row.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]