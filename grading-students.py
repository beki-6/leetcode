def gradingStudents(grades):
    # Write your code here
    newGrades = []
    for i in grades:
        diff = (i+5 - (i%5))
        if i >= 38 and diff - i < 3:
            newGrades.append(diff)
        else:
            newGrades.append(i)    
    return newGrades