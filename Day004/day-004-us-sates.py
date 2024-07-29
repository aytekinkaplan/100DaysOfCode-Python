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

# Örneğin, listenin tamamını yazdırmak için
print(us_states)

# Listenin ilk 5 elemanını yazdırmak için
print(us_states[:5])

# Listenin son 5 elemanını yazdırmak için
print(us_states[-5:])

# Listeyi tersten yazdırmak için
print(us_states[::-1])

# Listeyi alfabetik olarak sıralamak için
print(sorted(us_states))

state_to_find = "California"
if state_to_find in us_states:
    print(f"{state_to_find} is in the list.")
else:
    print(f"{state_to_find} is not in the list.")

state_to_find = "Texas"
index = us_states.index(state_to_find) if state_to_find in us_states else -1
print(f"{state_to_find} is at index {index}.")


print(f"Liste uzunluğu: {len(us_states)}")



