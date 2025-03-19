# Creating functions
# Author: Andrew Beatty
# Reproduced by: Elaine Cazetta

def readModules():
    return []


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


#test
students = []
doAdd(students)
doAdd(students)
print(students)