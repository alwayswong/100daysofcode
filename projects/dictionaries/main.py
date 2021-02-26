# # retrieve items from a dictionary by calling the string
#
# # add to dictionary by defining the key and item, similar to how pandas works
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
#
# student_grades = {}
#
# for key in student_scores:
#     if 91 <= student_scores[key] <= 100:
#         student_grades[key] = 'Outstanding'
#     elif 81 <= student_scores[key] <= 90:
#         student_grades[key] = 'Exceeds Expectations'
#     elif 71 <= student_scores[key] <= 80:
#         student_grades[key] = 'Acceptable'
#     else:
#         student_grades[key] = 'Fail'
#
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#
# #to be added to the travel_log. 👇
#
# def add_new_country(country_name, times_visited, cities):
#     # adding the new info to the travel log
#     new_dict = {"country": country_name, "visits": times_visited, "cities": cities}
#     travel_log.append(new_dict)
#
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)



from art import logo

print(logo)
bids = {}

while True:
    name = input("What is your name?").lower().strip()
    bid = int(input("What is your highest bid?"))
    bids[name] = bid
    while True:
        bidders = input("Are there more bidders?").lower().strip()
        if bidders in ("no","yes"):
            break
        else:
            print("Yes or no?")

    if bidders == "no":
        break

high_bid = 0
high_bidder = ''
for bid in bids:
    if bids[bid] > high_bid:
        high_bid = bids[bid]
        high_bidder = bid
print(f'The high bid is {high_bid} from {high_bidder}')




