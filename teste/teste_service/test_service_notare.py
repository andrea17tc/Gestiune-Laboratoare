from domain.dto import StudentProblemaNotare
from domain.problema import Problema
from domain.student import Student
from domain.validare.validare_notare import ValidatorNotare
from repository.repo_notare import NotareRepo
from repository.repo_problema import ProblemaRepo
from repository.repo_student import StudentRepo
from service.service_notare import NotareService


def test_notare_student():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    repo_student.stocare(stud1)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    repo_problema.stocare(pb1)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    try:
        notare1 = srv.notare_student(1, '1_1', 5)
        assert True
    except ValueError:
        assert False

    try:
        notare2 = srv.notare_student(2, '1_2', 3)
        assert False
    except ValueError:
        assert True


def test_get_all_for_id():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    stud2 = Student(2, 'Alex', 216)
    repo_student.stocare(stud1)
    repo_student.stocare(stud2)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    pb2 = Problema('1_2', 'Ana are caise', 2)
    repo_problema.stocare(pb1)
    repo_problema.stocare(pb2)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    notare1 = srv.notare_student(1, '1_1', 5)
    notare2 = srv.notare_student(1, '1_2', 7)
    notare3 = srv.notare_student(2, '1_2', 8)
    notari = srv.get_all_for_id(1)
    assert(len(notari) == 2)
    assert(notari == [notare1, notare2])


def test_get_all_for_nr():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    stud2 = Student(2, 'Alex', 216)
    repo_student.stocare(stud1)
    repo_student.stocare(stud2)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    pb2 = Problema('1_2', 'Ana are caise', 2)
    repo_problema.stocare(pb1)
    repo_problema.stocare(pb2)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    notare1 = srv.notare_student(1, '1_1', 5)
    notare2 = srv.notare_student(1, '1_2', 7)
    notare3 = srv.notare_student(2, '1_2', 8)
    notari = srv.get_all_for_nr('1_2')
    assert (len(notari) == 2)
    assert (notari == [notare2, notare3])


def test_sterge_student_si_notari():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    stud2 = Student(2, 'Alex', 216)
    repo_student.stocare(stud1)
    repo_student.stocare(stud2)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    pb2 = Problema('1_2', 'Ana are caise', 2)
    repo_problema.stocare(pb1)
    repo_problema.stocare(pb2)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    notare1 = srv.notare_student(1, '1_1', 5)
    notare2 = srv.notare_student(1, '1_2', 7)
    notare3 = srv.notare_student(2, '1_2', 8)
    srv.sterge_student_si_notari(1)
    notari = srv.get_all()
    assert(len(notari) == 1)
    assert(notari == [notare3])


def test_sterge_problema_si_notari():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    stud2 = Student(2, 'Alex', 216)
    repo_student.stocare(stud1)
    repo_student.stocare(stud2)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    pb2 = Problema('1_2', 'Ana are caise', 2)
    repo_problema.stocare(pb1)
    repo_problema.stocare(pb2)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    notare1 = srv.notare_student(1, '1_1', 5)
    notare2 = srv.notare_student(1, '1_2', 7)
    notare3 = srv.notare_student(2, '1_2', 8)
    srv.sterge_problema_si_notari('1_2')
    notari = srv.get_all()
    assert (len(notari) == 1)
    assert (notari == [notare1])


def test_set_nume_lista():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    stud2 = Student(2, 'Alex', 216)
    repo_student.stocare(stud1)
    repo_student.stocare(stud2)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    pb2 = Problema('1_2', 'Ana are caise', 2)
    repo_problema.stocare(pb1)
    repo_problema.stocare(pb2)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    notare1 = srv.notare_student(1, '1_1', 5)
    notare2 = srv.notare_student(1, '1_2', 7)
    notare3 = srv.notare_student(2, '1_2', 8)
    notari = srv.set_nume_lista('1_2')
    assert(len(notari) == 2)
    notare4 = StudentProblemaNotare(1, '1_2', 7)
    notare4.set_nume_student('Andrei')
    notare5 = StudentProblemaNotare(2, '1_2', 8)
    notare5.set_nume_student('Alex')
    assert(notari == [notare2, notare3])


def test_ordonare():
    repo_notare = NotareRepo()
    repo_student = StudentRepo()
    stud1 = Student(1, 'Andrei', 215)
    stud2 = Student(2, 'Alex', 216)
    repo_student.stocare(stud1)
    repo_student.stocare(stud2)
    repo_problema = ProblemaRepo()
    pb1 = Problema('1_1', 'Ana are mere', 23)
    pb2 = Problema('1_2', 'Ana are caise', 2)
    repo_problema.stocare(pb1)
    repo_problema.stocare(pb2)
    val = ValidatorNotare(repo_notare, repo_student, repo_problema)
    srv = NotareService(repo_notare, val, repo_student, repo_problema)
    notari = []
    notare4 = StudentProblemaNotare(1, '1_2', 7)
    notare4.set_nume_student('Andrei')
    notare5 = StudentProblemaNotare(2, '1_2', 8)
    notare5.set_nume_student('Alex')
    notari.append(notare5)
    notari.append(notare4)
    notari_ord = srv.ordonare(notari)
    assert(notari_ord == [notare4, notare5])


def Test_Service_Notare():
    test_notare_student()
    test_get_all_for_id()
    test_get_all_for_nr()
    test_sterge_student_si_notari()
    test_sterge_problema_si_notari()
    test_set_nume_lista()
    test_ordonare()