import unittest

from domain.student import Student
from domain.validare.validare_student import ValidatorStudent
from repository.repo_student import StudentRepo


class TestCaseStudentRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = StudentRepo()

        student1 = Student(1, 'Alex', 213)
        student2 = Student(2, 'Andrei', 214)
        student3 = Student(3, 'Ana', 215)
        student4 = Student(4, 'Maria', 216)
        self.__repo.stocare(student1)
        self.__repo.stocare(student2)
        self.__repo.stocare(student3)
        self.__repo.stocare(student4)

    def test_stocare(self):
        studenti = self.__repo.get_all()
        self.assertEqual (len(studenti), 4)

    def test_delete(self):
        student1 = Student(1, 'Alex', 213)
        student2 = Student(2, 'Andrei', 214)
        student3 = Student(3, 'Ana', 215)
        student4 = Student(4, 'Maria', 216)
        student = self.__repo.delete(2)
        studenti = self.__repo.get_all()
        self.assertEqual(len(studenti), 3)
        self.assertEqual (studenti, [student1, student2, student4])
        assert (student == student3)

    def test_size(self):
        size = self.__repo.size()
        self.assertEqual(size, 4)

    def test_find_index(self):
        index = self.__repo.find_index(1)
        index2 = self.__repo.find_index(5)
        self.assertEqual(index, 0)
        self.assertEqual(index2, -1)

    def test_update(self):
        student5 = Student(1, 'Alexandru', 214)
        student = self.__repo.update(1, student5)
        studenti = self.__repo.get_all()
        self.assertEqual(len(studenti), 4)
        self.assertEqual(studenti[0],Student(1, 'Alexandru', 214))
        self.assertEqual(student, Student(1, 'Alexandru', 214))


if __name__ == '__main__':
    unittest.main()
