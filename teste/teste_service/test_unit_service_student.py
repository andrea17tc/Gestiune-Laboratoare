import unittest

from domain.student import Student
from domain.validare.validare_student import ValidatorStudent
from repository.repo_student import StudentRepo
from service.service_student import StudentService


class TestCaseStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = StudentRepo()
        self.__val = ValidatorStudent(self.__repo)
        self.__srv = StudentService(self.__repo, self.__val)

        student1 = Student(1, 'Alex', 213)
        student2 = Student(2, 'Andrei', 214)
        student3 = Student(3, 'Ana', 215)
        student4 = Student(4, 'Maria', 216)
        self.__repo.stocare(student1)
        self.__repo.stocare(student2)
        self.__repo.stocare(student3)
        self.__repo.stocare(student4)

    def test_adauga_student(self):
        self.assertTrue(self.__srv.adauga_student(5,'Adrian', 216))
        self.assertRaises(ValueError, self.__srv.adauga_student,1,'Alex', 213 )

    def test_get_all(self):
        studenti = self.__repo.get_all()
        self.assertEqual(len(studenti), 4)

    def test_delete_by_id(self):
        student = self.__srv.delete_by_id(1)
        studenti = self.__srv.get_all()
        self.assertEqual(len(studenti), 3)
        self.assertRaises(ValueError, self.__srv.delete_by_id, 6)

    def test_delete_by_id_black(self):
        student = self.__srv.delete_by_id(1)
        studenti = self.__srv.get_all()
        self.assertEqual(len(studenti), 3)


    def test_modifica_student(self):
        self.assertTrue(self.__srv.modifica_student(1, 'Alexandru', 214))
        student = self.__srv.modifica_student(1, 'Alexandru', 214)
        self.assertEqual(student, Student(1, 'Alexandru', 214))
        self.assertRaises(ValueError, self.__srv.modifica_student,5,'Alexandru', 214)

    def test_cauta_student(self):
        student = self.__srv.cauta_student(2)
        self.assertEqual(student, Student(2, 'Andrei', 214))
        self.assertRaises(ValueError, self.__srv.cauta_student, 5)

if __name__ == '__main__':
    unittest.main()
