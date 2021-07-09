def roundGrade(grade):
    first_number, second_number = list(str(grade))[0], list(str(grade))[1]
    if int(second_number) > 7:
        first_number = str(int(first_number) + 1)
        second_number = '0'
        return int(first_number + second_number)
    elif int(second_number) > 2 and int(second_number) < 5:
        second_number = '5'
        return int(first_number + second_number)
    else:
        return grade

def checkGrade(grade):
    if grade > 37 and grade % 5 != 0:
        return roundGrade(grade)
    return grade

def gradingStudents(grade):
    return list(map(checkGrade, grade))
    
if __name__ == '__main__':
    print(gradingStudents([73, 67, 38, 33]))
