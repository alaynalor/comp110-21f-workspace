"""DEmonstrations of dictionary capabilities."""

# declare type of dictionary
schools: dict[str, int]

# initalize to empty dictionary
schools = dict()

# set a key-value pairing in dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print dictionary literal representation
print(schools)

# access value by its key -- "lookup"
print(f"Unc has {schools['UNC']} students")

# remove key-value pair from dictionary by its key
schools.pop("Duke")

# test for existense of key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# update / reassign key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

invert_schools: dict[int, str] = {}
invert_schools[19400] = "UNC"

# example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

# demonstration of dictionary literals

# empty dictionary literal 

schools = {} 
print(schools)

# alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# access key that does not exist
print(schools["UNCC"])