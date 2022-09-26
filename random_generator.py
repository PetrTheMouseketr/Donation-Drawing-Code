import random
from collections import defaultdict

#gets the info from the txt file
raw_data = open("sample_donations.txt", "r").readlines()
donator_dict = defaultdict(float)

#figures out the range of values in the list of values
amounts_list = []
for i in raw_data:
    donator_and_amount = i.split(", ")
    donator = donator_and_amount[0]
    amount = float(donator_and_amount[1])
    donator_dict[donator] = amount
    amounts_list.append(amount)

highest = max(amounts_list)
lowest = min(amounts_list)
total = len(amounts_list)

#sets up the tiers for the donation pool based on the range and the total
tier_value = (highest - lowest) / total

#adds name to the hat at least once, then adds more for the amount of times it can be divided by tier_value
#so, the greater the amount contributed, the higher the chance of being picked!
drawing_hat = []
for donator, amount in donator_dict.items():
    drawing_hat.append(donator)
    multiplier = amount // tier_value
    for i in range(1, int(multiplier)):
        drawing_hat.append(donator)

#sets up the total amount of people in the final drawing list
final_list = []
final_list_length = 5
if total < 5:
    final_list_length = total

#picks the names out of the hat (does not pick the same person twice)
while (len(final_list) < final_list_length):
    rand_num = random.randrange(0, len(drawing_hat)-1)
    selected_donator = drawing_hat[rand_num]
    if selected_donator not in final_list:
        final_list.append(selected_donator)

#prints out the results of the drawing!
print("\nCongratulations to:")
for i in final_list:
    print(i)
print("\n")
