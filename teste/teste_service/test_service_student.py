from domain.student import Student
from domain.validare.validare_student import ValidatorStudent
from repository.repo_student import StudentRepo
from service.service_student import StudentService


def test_adauga_student():
    repo = StudentRepo()
    val = ValidatorStudent(repo)
    srv = StudentService(repo, val)
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    try:
        student = srv.adauga_student(1,'Alex', 213)
        assert False
    except ValueError:
        assert True
    try:
        student5 = srv.adauga_student(5,'Adrian', 216)
        assert True
    except ValueError:
        assert False


def test_delete_by_id():
    repo = StudentRepo()
    val = ValidatorStudent(repo)
    srv = StudentService(repo, val)
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    student = srv.delete_by_id(1)
    studenti = srv.get_all()
    assert(len(studenti) == 3)
    assert(student == student1)
    try:
        student5 = srv.delete_by_id(6)
        assert False
    except ValueError:
        assert True


def test_modifica_student():
    repo = StudentRepo()
    val = ValidatorStudent(repo)
    srv = StudentService(repo, val)
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    student = srv.modifica_student(1,'Alexandru', 214)
    assert(student == Student(1,'Alexandru', 214))
    try:
        student6 = srv.modifica_student(5,'Alexandru', 214)
        assert False
    except ValueError:
        assert True


def test_cauta_student():
    repo = StudentRepo()
    val = ValidatorStudent(repo)
    srv = StudentService(repo, val)
    student1 = Student(1, 'Alex', 213)
    student2 = Student(2, 'Andrei', 214)
    student3 = Student(3, 'Ana', 215)
    student4 = Student(4, 'Maria', 216)
    repo.stocare(student1)
    repo.stocare(student2)
    repo.stocare(student3)
    repo.stocare(student4)
    student = srv.cauta_student(2)
    assert(student == Student(2, 'Andrei', 214))
    try:
        student5 = srv.cauta_student(5)
        assert False
    except ValueError:
        assert True


def Test_Service_Student():
    test_adauga_student()
    test_delete_by_id()
    test_modifica_student()
    test_cauta_student()