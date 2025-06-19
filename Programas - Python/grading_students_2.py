def roundGrade(grade):
    if (grade - 3) % 5 == 0:
        grade += 2
    elif (grade + 1) % 5 == 0:
        grade += 1
    return grade

def checkGrade(grade):
    if grade > 37 and grade % 5 != 0:
        return roundGrade(grade)
    return grade

def gradingStudents(grade):
    return list(map(checkGrade, grade))
    
if __name__ == '__main__':
    print(gradingStudents([73, 67, 38, 33]))
