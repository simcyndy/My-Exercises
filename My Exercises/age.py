from datetime import date
name = raw_input("Enter your Name: ")
age = int(raw_input("Enter your Age: "))

today = date.today()
year = today.year
in_100_years = (int(100) - age) + year
print("Hi {0} ,You will turn 100 years old in the year {1}").format(name, in_100_years)
