x = 0
while x <= 5:
    print(x)
    x = x + 1


counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)


for num in range(2):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#print county
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

#print voters
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#print Key-Value Pairs
#for key, value in dictionary_name.items():
 #   print(key,value)

for county, voters in counties_dict.items():
    print(county,"county has ", voters, " registerd voters.") 

#print Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#print Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#print a specific key-value
for county_dict in voting_data:
    print(county_dict['registered_voters'])


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
