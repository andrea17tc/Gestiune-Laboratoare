from domain.student import Student


def test_get_studentID(student):
    id = student.get_studentID()
    assert(id == 1)

def test_get_nume(student):
    nume = student.get_nume()
    assert(nume == 'Andrei Macelaru')


def test_get_grupa(student):
    grupa = student.get_grupa()
    assert(grupa == 213)


def test_set_nume(student):
    student.set_nume('Marcel')
    nume = student.get_nume()
    assert(nume == 'Marcel')

def test_set_grupa(student):
    student.set_grupa(214)
    grupa = student.get_grupa()
    assert(grupa == 214)

def Test_Student():
    student = Student(1,'Andrei Macelaru', 213)
    test_get_studentID(student)
    test_get_nume(student)
    test_get_grupa(student)
    test_set_nume(student)
    test_set_grupa(student)