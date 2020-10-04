import csv
with open("ClassMarks.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get index number and value of each item in the header_row list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Get first name, surname, class, and marks from this CSV file
    first_name, surname, class_name, marks = [], [], [], []
    for row in reader:
        try:
            new_first_name = str(row[0])
            new_surname = str(row[1])
            new_class_name = str(row[2])
            new_marks = int(row[3])
        except ValueError:
            print(f"Missing data.")
        else:
            first_name.append(new_first_name)
            surname.append(new_surname)
            class_name.append(new_class_name)
            marks.append(new_marks)


class Student:
    """
    A class containing the name of a student and their classmarks
    """
    def __init__(self, firstName, surName):
        self.firstName = firstName
        self.surName = surName
        self.classMarks = []

    def totalMark(self):
        """
        Return the total mark given to the student from all classes
        """
        total = 0
        for classMark in self.classMarks:
            total += classMark.marksGiven
        return total

    def averageMark(self):
        total = 0
        numberOfClasses = 0

        for classMark in self.classMarks:
            total += classMark.marksGiven
            numberOfClasses += 1

        return float(total) / numberOfClasses

class ClassMark:

    def __init__(self, classTaken, marksGiven):
        self.classTaken = classTaken
        self.marksGiven = marksGiven

studentList = []
if __name__ == "__main__":

    getSurname = 0
    getClass = 0
    getClassMark = 0

    for name in first_name:

        name = Student(name, surname[getSurname])
        studentList.append(name)

        getSurname += 1

        name.classMarks.append(ClassMark(class_name[getClass], marks[getClassMark]))

        getClass += 1
        getClassMark += 1

    for name in studentList:
        print(f"Average mark for {name.firstName} = {str(name.averageMark())}")
        print(f"Total mark for {name.firstName} = {str(name.totalMark())}")

