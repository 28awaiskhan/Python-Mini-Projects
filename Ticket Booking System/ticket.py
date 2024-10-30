days = {
    "Monday": "Monday",
    "Tuesday": "Tuesday",
    "Wednesday": "Wednesday",
    "Thursday": "Thursday",
    "Friday": "Friday"
}

ticket_amount = {
    "Monday": 1000,
    "Tuesday": 2000,
    "Wednesday": 3000,
    "Thursday": 4000,
    "Friday": 5000,
}

amount = 0

print("Hello Welcome to the \033[1mTECH-AIRLINES\033[0m")

print("""
    FROM Location

     Los Angeles
     Chicago
     San Francisco
     Miami
     Seattle
     Boston
     Houston
     Dallas
     Atlanta
     Philadelphia

""")

from_location = input("Enter Your Location: ")

print("""
    To Location

    Pakistan
    America
    UAE
    India
    Bangladesh
    Quwait
    Saudia Arab
    Malaysia
    Iran
    Phalestine

""")

to_location = input("Please Enter Your Destination Location: ")

print("""
    Monday    : 1
    Tuesday   : 2
    Wednesday : 3
    Thursday  : 4
    Friday    : 5
""")

select_days = input("Enter day: ")

if select_days in days:
    day_name = days[select_days]

    if day_name in ticket_amount:
      
        amount += ticket_amount[day_name]
        print("You have selected", day_name)
else:
    print("Invalid day")

print(f"""
Congratulations! Your plane ticket has been successfully booked. Safe travels!
From Location : {from_location}
To Location : {to_location}
Days : {day_name}
Amount : {amount}
""")
