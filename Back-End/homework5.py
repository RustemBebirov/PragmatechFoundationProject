# # home work 3
# class User():

#     def __init__ (self,first_name,last_name,username,age,country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.age = age
#         self.country = country

#     def describe_user(self):
#         print("AD:" +self.first_name + ' Soyad:' + self.last_name + " Olke: " + self.country + ' age:' + str(self.age))

#     def greet_user(self):
#         print('Salam :' + self.first_name + ' ' +self.last_name)



# user1=User('Rustem','Bebirov','rustembebirov',25,'Azerbaijan')
# user1.describe_user()
# user1.describe_user()


# user2=User('Subhan',"Atakisiyev",'subhanatakisiyev',24,'Azerbaijan')
# user2.describe_user()
# user2.greet_user()

# home work 1

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print('Restaurant name : '+self.restaurant_name)
        print('Metbex: '+ self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name +' Restaurant is open')

    
res1=Restaurant('Adana','kabab')
print(res1.restaurant_name)
print(res1.cuisine_type)

res1.describe_restaurant()

res1.open_restaurant()

res2=Restaurant('Nusret','burger')
res2.describe_restaurant()
res2.open_restaurant()

res3=Restaurant('Dominos','Pizza')
res2.describe_restaurant()
res2.open_restaurant()







