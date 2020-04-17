##
##Code Tester - Get From File and Make Dictionary
##

file1 = open('People.txt', 'r') 
Lines = file1.readlines()

dict = {}

for line in Lines:
    words = line.split(',')
    name = words[0]
    place = words.index(' service')
    languages = words[2:place]
    place2 = words.index(' location')
    services = words[place+1:place2]
    location = words[place2+1]
    place3 = words.index(' availability')
    availability = words[place3+1]
    dict1 = {'language':languages, 'service':services, 'location':location, 'availability':availability}
    dict.update({name:dict1})

print(dict)
