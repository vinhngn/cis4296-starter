import math

def calculation(days):
    rate = 1.2
    totalInfected = 7
    latestInfected = totalInfected
    earlyDropStudents = totalInfected 
    
    for i in range(1, days):
        latestInfected = math.trunc(latestInfected * rate)
        totalInfected += latestInfected
        if totalInfected > 2440:
            totalInfected = 2440
        if i < 14:  
            earlyDropStudents += latestInfected

    lostTuition = earlyDropStudents * 9972
    discount = (2440 - earlyDropStudents) * (9972 * 0.05)
    percentage = (totalInfected / 2440) * 100
    
    return totalInfected, round(percentage, 3), lostTuition, 2440 - earlyDropStudents, discount


#Testing
print("""
    - Currently, we have 7 infected students.
    - The infection rate is 1.2 times the current infected students daily.
    
    Instructions:
    - Please enter the number of days you wish to calculate the total number of infected students.
    - This tool will also calculate the tuition lost for students who drop within the first 14 days 
      (full refund) and the discount for students who remain uninfected.
    - Note: The number of days should start from 1. Please enter a numerical value.
    """)

result = calculation(int(input("Enter the days: ")))

print("Total students infected: ", result[0])
print("Percentage of infected students: ", result[1], "%")
print("Tuition lost for early drop students: $", result[2])
print("Total uninfected students by add/drop: ", result[3])
print("Tuition discount for uninfected students: $", result[4])

input("Press enter to exit!")
