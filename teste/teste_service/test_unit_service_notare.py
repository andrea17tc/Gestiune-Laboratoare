import unittest

from domain.dto import StudentProblemaNotare
from domain.problema import Problema
from domain.student import Student
from domain.validare.validare_notare import ValidatorNotare
from repository.repo_notare import NotareRepo
from repository.repo_problema import ProblemaRepo
from repository.repo_student import StudentRepo
from service.service_notare import NotareService


class TestCaseNotareService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_notare = NotareRepo()
        self.__repo_student = StudentRepo()
        self.__repo_problema = ProblemaRepo()
        self.__val = ValidatorNotare(self.__repo_notare,self.__repo_student, self.__repo_problema)
        self.__srv = NotareService(self.__repo_notare, self.__val, self.__repo_student, self.__repo_problema)
        stud1 = Student(1, 'Andrei', 215)
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud1)
        pb1 = Problema('1_1', 'Ana are mere', 23)
        self.__repo_problema.stocare(pb1)
        self.__srv = NotareService(self.__repo_notare, self.__val, self.__repo_student, self.__repo_problema)

    def test_notare_student(self):
        self.assertTrue(self.__srv.notare_student(1, '1_1', 5))
        self.assertRaises(ValueError, self.__srv.notare_student, 2, '1_2', 3)

    def test_get_all(self):
        self.assertEqual(self.__srv.get_all(), [])
        self.__srv.notare_student(1, '1_1', 5)
        self.assertRaises(ValueError, self.__srv.notare_student, 2, '1_1', 7)
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        self.__srv.notare_student(2, '1_1', 8)
        self.assertEqual(len(self.__srv.get_all()), 2)

    def test_get_all_for_id(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        notari = self.__srv.get_all_for_id(1)
        self.assertEqual(len(notari), 2)
        self.assertEqual(notari, [notare1, notare2])
        notari2 = self.__srv.get_all_for_id(3)
        self.assertEqual(notari2, [])

    def test_get_all_for_nr(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        notari = self.__srv.get_all_for_nr('1_1')
        self.assertEqual(len(notari), 1)
        self.assertEqual(notari, [notare1])
        notari2 = self.__srv.get_all_for_id('1_3')
        self.assertEqual(notari2, [])

    def test_sterge_student_si_notari(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        self.__srv.sterge_student_si_notari(1)
        notari = self.__srv.get_all()
        self.assertEqual(len(notari) , 1)
        self.assertEqual(notari, [notare3])

    def test_sterge_problema_si_notari(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        self.__srv.sterge_student_si_notari(2)
        notari = self.__srv.get_all()
        self.assertEqual(len(notari), 2)
        self.assertEqual(notari, [notare1,notare2])

    def test_set_nume_lista(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        notari = self.__srv.set_nume_lista('1_2')
        self.assertEqual(len(notari), 2)
        notare4 = StudentProblemaNotare(1, '1_2', 7)
        notare4.set_nume_student('Andrei')
        notare5 = StudentProblemaNotare(2, '1_2', 8)
        notare5.set_nume_student('Alex')
        self.assertEqual(notari,[notare2, notare3])

    def test_ordonare(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        notari = []
        notare4 = StudentProblemaNotare(1, '1_2', 7)
        notare4.set_nume_student('Andrei')
        notare5 = StudentProblemaNotare(2, '1_2', 8)
        notare5.set_nume_student('Alex')
        notari.append(notare5)
        notari.append(notare4)
        notari_ord = self.__srv.ordonare(notari)
        self.assertEqual(notari_ord, [notare4, notare5])

    def test_sterge_student_si_notari_rec(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        self.__srv.sterge_student_si_notari_rec(1)
        notari = self.__srv.get_all()
        self.assertEqual(len(notari) , 1)
        self.assertEqual(notari, [notare3])

    def test_sterge_problema_si_notari_rec(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        self.__srv.sterge_problema_si_notari_rec('1_1')
        notari = self.__srv.get_all()
        self.assertEqual(len(notari), 2)
        self.assertEqual(notari, [notare2,notare3])

    def test_quick_sort(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        notari = []
        notare4 = StudentProblemaNotare(1, '1_2', 7)
        notare4.set_nume_student('Andrei')
        notare5 = StudentProblemaNotare(2, '1_2', 8)
        notare5.set_nume_student('Alex')
        notari.append(notare5)
        notari.append(notare4)
        notari_ord = self.__srv.quick_sort(notari)
        self.assertEqual(notari_ord, [notare4, notare5])

    def test_gnome_sort(self):
        stud2 = Student(2, 'Alex', 213)
        self.__repo_student.stocare(stud2)
        pb2 = Problema('1_2', 'Ana are caise', 2)
        self.__repo_problema.stocare(pb2)
        notare1 = self.__srv.notare_student(1, '1_1', 5)
        notare2 = self.__srv.notare_student(1, '1_2', 7)
        notare3 = self.__srv.notare_student(2, '1_2', 8)
        notari = []
        notare4 = StudentProblemaNotare(1, '1_2', 7)
        notare4.set_nume_student('Andrei')
        notare5 = StudentProblemaNotare(2, '1_2', 8)
        notare5.set_nume_student('Alex')
        notari.append(notare5)
        notari.append(notare4)
        notari_ord = self.__srv.GnomeSort(notari)
        self.assertEqual(notari_ord, [notare4, notare5])

if __name__ == '__main__':
    unittest.main()
