def calc_average(scores):
    return sum(scores)/len(scores)

def determine_grade(average):
    if average>=90 or average<=100:
        return 'A'
    if average>=80 or average<=89:
        return 'B'
    if average>=70 or average<=79:
        return 'C'
    if average>=60 or average<=69:
        return 'D'
    if average<60:
        return 'F'

scores=input("enter 5 scores by using space").split()
scores=list(map(int,scores))
print (scores)
average=calc_average(scores)
grade=determine_grade(average)
print(f"the average of numbers is {average}")
print(f"the grade of your is{grade}")