#dc1-day3

# user_word = input("Give me a word: ")
# dict_word = {}
# for i,letter in enumerate(user_word):
#     if letter not in dict_word: 
#         dict_word[letter]= []
#     dict_word[letter].append(i)
 
# print(dict_word)


#dc2-day3
# def afford_items(items_purchase ,wallet):
#   wallet_amount = int(wallet.replace('$', '').replace(',', ''))
#   affordable_items =[]
#   for item, price in items_purchase.items():
#       item_price = int(price.replace('$','').replace(',', ''))
#       if wallet_amount >= item_price:
#        affordable_items.append(item)
     
#   affordable_items.sort()
#   if affordable_items:
#         return affordable_items
#   else:
#         return "Nothing"
      
# items_purchase_1 = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
# wallet_1 = "$300"
    
# print(afford_items(items_purchase_1,wallet_1))

# items_purchase_2 = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }
# wallet_2 = "$100"

# print(afford_items(items_purchase_2,wallet_2))

# items_purchase_3 = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }
# wallet_3 = "$1"

# print(afford_items(items_purchase_3,wallet_3))

