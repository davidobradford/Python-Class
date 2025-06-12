salary = 0
while salary <= 0:
    salary = float(input("Enter The Teacher's Starting Salary: "))
    if salary <= 0:
        print("Salary Cannot Be Zero or Less, Try again...")

print(" ")

increase = 0        
while increase <= 0:
    increase = float(input("Enter The Percentage of Increase Each Year: "))
    if increase <= 0:
        print("Percentage Increase Cannot Be Zero or Less, Try again...")

print(" ")

years = 0
while years <= 0:
    years = int(input("Enter The Number of Years In the Schedule: "))
    if years <= 0:
        print("Number Of Schedule Years Cannot Be Zero or Less, Try again...")

for year in range(years):
    salary = salary + (salary * (increase / 100) * year)
    print(year + 1, round(salary,2))
    

