# blind-auction
import art

print(art.logo)


def auction():
    auction_data = {}
    while True:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        auction_data[name] = bid
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue.lower() == "no":
            break
    return auction_data


auction_data = auction()

for key in auction_data:
    print(f"{key} bid ${auction_data[key]}")

winner = max(auction_data, key=auction_data.get)
print(f"The winner is {winner} with a bid of ${auction_data[winner]}")

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))