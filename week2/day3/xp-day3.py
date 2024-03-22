#ex1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# user_data = set(zip(keys,values))
# print(user_data)

#ex2
# ticket_price_under_3 = 0
# ticket_price_3_to_12 = 10
# ticket_price_over_12 = 15

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost =0
# for x,y in family.items():
#     if y < 3:  
#      print(f"the cost for",x,"is",": $",ticket_price_under_3,',00')
#      total_cost += ticket_price_under_3
#     elif y <12:
#      print(f"the cost for",x,"is",": $",ticket_price_3_to_12,',00' )
#      total_cost +=ticket_price_3_to_12
     
#     else:
#      print(f"the cost for",x,"is",": $",ticket_price_over_12,',00' ) 
#      total_cost += ticket_price_over_12
# print(f'the total cost for this family is: ','$',total_cost,',00')
   
   
   
#    #ex3
# brand ={'name': 'Zara', 
# 'creation_date': 1975 ,
# 'creator_name': 'Amancio Ortega Gaona', 
# 'type_of_clothes': ['men', 'women', 'children', 'home'], 
# 'international_competitors':['Gap', 'H&M', 'Benetton'], 
# 'number_stores': 7000 ,
# 'major_color': {
#     'France': 'blue', 
#     'Spain': 'red', 
#     'US': ['pink', 'green']}
# }
        
# brand['number_stores'] = 2
# # print('Zara clients are men, women, children, people that like also Gap, H&M and Benneton from around the world')
# brand['conutry_creation']='Spain'
# brand['international_competitors'].append('Desigual')
# del  brand['creation_date']
# # print(brand['international_competitors'][-1])
# # print(brand['major_color']['US'])
# # print(len(brand))
# # print(brand.keys())

# more_on_zara = {'creation_date': 1975 ,
# 'number_stores': 10000}
# brand.update(more_on_zara)
# # print(brand)
# print(brand['number_stores'])
# The number of stores from the more_on_zara dictionary was replaced by the previous key.
# The number of stores between the 2 dictionaries was not unified


#ex4
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# result =[]
# for puffys in range(len(users)):
#     if puffys %2 == 0:
#         result.append(users[puffys])
        
# print(result)

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# disney_users_A = {}
# for i,user in enumerate(users):
#     disney_users_A[user] = i
# print(disney_users_A)

# disney_users_B ={}
# for i,user in enumerate(users):
#     disney_users_B[i]=user
#     print(disney_users_B)
    
# disney_users_C = {user:i for i,user in enumerate(sorted(users))}
# print(disney_users_C)

# disney_users_i = {}
# for i, user in enumerate(users):
#     if 'i' in user:
#         disney_users_i[user] = i
# print(disney_users_i)

# disney_users_m_p = {}
# for i, user in enumerate(users):
#     if user[0].lower() in ['m', 'p']:
#         disney_users_m_p[user] = i
# print(disney_users_m_p)


 
   




    

