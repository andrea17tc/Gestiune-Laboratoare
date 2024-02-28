from domain.student import Student
from repository.repo_student import StudentRepo


def test_stocare():
    repo = StudentRepo()
    student1 = Student(1,'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    studenti = repo.get_all()
    assert(len(studenti) == 4)


def test_delete():
    repo = StudentRepo()
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    student = repo.delete(2)
    studenti = repo.get_all()
    assert(len(studenti) == 3)
    assert(studenti == [student1,student2, student4])
    assert(student == student3)


def test_size():
    repo = StudentRepo()
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    size = repo.size()
    assert(size == 4)


def test_find_index():
    repo = StudentRepo()
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    index = repo.find_index(1)
    index2 = repo.find_index(5)
    assert(index == 0)
    assert(index2 == -1)


def test_find():
    repo = StudentRepo()
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    student_nou = repo.find(2)
    assert(student_nou == student2)


def test_update():
    repo = StudentRepo()
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)

    student5 = Student(1, 'Alexandru', 214)
    student = repo.update(1, student5)
    studenti = repo.get_all()
    assert(len(studenti) == 4)
    assert(studenti[0] == Student(1, 'Alexandru', 214))
    assert(student == Student(1, 'Alexandru', 214))


def Test_Repo_Student():
    test_stocare()
    test_delete()
    test_size()
    test_find_index()
    test_find()
    test_update()