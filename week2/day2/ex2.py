#ex1
# my_fav_numbers = {7, 10, 23}
# my_fav_numbers.add(3)
# my_fav_numbers.add(8)
# last_number = my_fav_numbers.pop()
# print(my_fav_numbers)
# friend_fav_numbers = {2, 15, 29}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#ex2
# first_tuple = (1, 3, 5)
# new_integers = (7, 9, 11)
# mix_tuple = first_tuple + new_integers
# print(mix_tuple)
# it's not possible to add more integers to a single tuple

#ex3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# apple_count = basket.count("Apples")
# basket.clear()
# print(basket)

#ex4
#float is the numbers with decimals
# start = 1.5
# end = 5
# sequence_list = [start + 0.5 * i for i in range(int((end - start) / 0.5) + 1)]
# print(sequence_list)

# #ex5
# print("All numbers from 1 to 20:")
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

#ex6
# my_name = "John"
# user_name = ""
# while user_name != my_name:
#     user_name = input("Please enter your name: ")
#     if user_name != my_name:
#         print("That's not my name. Please try again.")

# print("Welcome,", my_name + "!")

#ex7
# favorite_fruits_str = input("Please enter your favorite fruit(s), separated by a single space: ")
# favorite_fruits_list = favorite_fruits_str.split()
# chosen_fruit = input("Please enter a fruit: ")
# if chosen_fruit in favorite_fruits_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy.")

#ex8
# toppings = []
# base_price = 10
# while True:
#     topping = input("Enter a pizza topping (enter 'quit' to finish): ")
#     if topping.lower() == 'quit':
#         break
#     toppings.append(topping)
#     print("Adding", topping, "to your pizza.")
# total_price = base_price + len(toppings) * 2.5
# print("\nYour pizza toppings:")
# for topping in toppings:
#     print("-", topping)
# print("\nTotal price:", total_price)

#ex9
# def calculate_ticket_price(age):
#     if age < 3:
#         return 0
#     elif 3 <= age <= 12:
#         return 10
#     else:
#         return 15

# family_members = int(input("Enter the number of family members: "))
# total_cost = 0
# for i in range(family_members):
#     age = int(input(f"Enter the age of family member {i + 1}: "))
#     total_cost += calculate_ticket_price(age)

# print("Total cost of all the family's tickets:", total_cost)

# teenagers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# for teenager in teenagers[:]:
#     age = int(input(f"Enter the age of {teenager}: "))
#     if not 16 <= age <= 21:
#         teenagers.remove(teenager)
# print("Final list of teenagers permitted to watch the movie:", teenagers)

#ex10
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")
# finished_sandwiches = []
# # Prepare the orders of the clients
# while sandwich_orders:
#     sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(sandwich)
#     print(f"Finished making {sandwich}.")

# print("\nList of finished sandwiches:")
# for sandwich in finished_sandwiches:
#     print("- " + sandwich)










