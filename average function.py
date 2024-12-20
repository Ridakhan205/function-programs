def calc_average(scores):
    return sum(scores) / len(scores)

def determine_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

scores = []
input_scores = input("Enter 5 scores separated by spaces: ").split()

for score in input_scores:
    scores.append(int(score))  

average = calc_average(scores)
grade = determine_grade(average)

print(f"The average of the numbers is {average:.2f}")
print(f"The grade for your average is {grade}")