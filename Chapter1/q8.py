#Write a program that asks the user the day number in a year in the range 2 to 365 and asks the first day of the year Sunday or Monday or Tuesdas etc.
#Then the program should display the day on the day-thumber that has been input

week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
n=int(input("enter day number in a year in the range (2-365):"))
if n<2 and n>365:
    print("error")
else:
    print("done")

first_day_of_year = input("Enter the first day of the year (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday): ")
first_day_index = week.index(first_day_of_year)
day_of_week_index=(first_day_index +n-1)%7
week=week[day_of_week_index]
print(f"The day number {n} falls on a {week}.")


