# #empty Dict
# contacts = {}

# while True:
#     print("\nContact Book app")
#     print("1. Create Contact")
#     print("2. View Contact")
#     print("3. UpdateContact")
#     print("4. Delete Contact")
#     print("5. Search Contact")
#     print("6. Count Contact")
#     print("7. Exit")

#     choice = input("Enter Your choise = ")

#     if choice == "1":
#         name = input("Enter Name = ")
#         if name in contacts:
#             print("Already Exist", {name})
#         else:
#             age = input("Enter age = ")    
#             number = input("Enter Phone Number = ")    
#             email = input("Enter Email = ")
#             contacts[name] = {"age" : int(age), "Phone Number" : int(number), "Email Address" : email }
#             print(f'Contact name {name} has been created successfully')

# # View Contact
#     elif choice == "2":
#         name = input("Enter Name view contact = ")
#         if name in contacts:
#             contact = contacts[name]
#             print(f" Name = {name} Age = {age} Phone Number = {number} Email Address = {email}")
#         else:
#             print('Contact not found')
# #Update Conatct
#     elif choice == "3":
#         name = input("Enter Name update contact = ")
#         if name in contacts:
#             age = input("Enter age = ")    
#             number = input("Enter Phone Number = ")    
#             email = input("Enter Email = ")
#             contacts[name] = {"age" : int(age), "Phone Number" : int(number), "Email Address" : email }
#             print(f"Update Your Contact = Name = {name} Age = {age} Phone Number = {number} Email Address = {email}")
#         else:
#             print("Contact Not Found")

# # Delet Contact
#     elif choice == "4":
#         name = input("Enter Your Contact Name")
#         if name in contacts:
#             del contacts[name]
#             print(f'Contact name {name} has been deleted successfully')
#         else:
#             print("Contact Not Found")

# # Search Contact
#     elif choice == "5":
#         name = input("Enter Your Contact Name")
#         if name in contacts:
#             print(f"This is Your Contact {name}")
#         else:
#             print("Contact Not Found")

# #Count contact
#     elif choice == '6':
#         print(f"Total Contact = {len(contacts)}")

#     elif choice == '7':
#         print('Close Your Programmme.....')
#         break
#     else:
#         print('Invalid choice')
             
name : str = "Awais khan"
rollno :  str = "PIAICC221042"
distance  : str = "No"
city : str = "Karachi"
center : str = "Baharia Auditorium"
campus : str = "Karsaz"
Day_time : str = "Sunday-09:00 AM to 01:00 PM"
batch : str = "61"

print(f"""ID CARD
Name : {name}
Roll no : {rollno}
Distance learning {distance}
City : {city}
Center : {center}
Campus : {campus}
Day \ Time : {Day_time}
Batch : {batch}""")
