import random

us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
    "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

print("Original list of US states:")
print(us_states)

random.shuffle(us_states)

print("\nFirst 5 shuffled states with index:")
for i, state in enumerate(us_states[:5]):
    print(f"{i}. {state}")

print("\n--------------------------------------------")
print("All shuffled states:")
for state in us_states:
    print(state)

print("\n--------------------------------------------")
print("5 random states:")
for state in random.sample(us_states, 5):
    print(state)

print("\n--------------------------------------------")
list_length = []
for state in sorted(us_states):
    list_length.append(len(state))

new_list = sorted(list_length)

print("Lengths of state names in sorted order:")
for length in new_list:
    print(length)
