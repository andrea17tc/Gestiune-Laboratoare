import unittest

from domain.student import Student


class TestCaseStudentDomain(unittest.TestCase):

    def test_get_studentID(self):
        student = Student(1, 'Andrei Macelaru', 213)
        id = student.get_studentID()
        self.assertEqual(id, 1)

    def test_get_nume(self):
        student = Student(1, 'Andrei Macelaru', 213)
        nume = student.get_nume()
        self.assertEqual(nume, 'Andrei Macelaru')

    def test_get_grupa(self):
        student = Student(1, 'Andrei Macelaru', 213)
        grupa = student.get_grupa()
        self.assertEqual (grupa, 213)

    def test_set_nume(self):
        student = Student(1, 'Andrei Macelaru', 213)
        student.set_nume('Marcel')
        nume = student.get_nume()
        self.assertEqual (nume, 'Marcel')

    def test_set_grupa(self):
        student = Student(1, 'Andrei Macelaru', 213)
        student.set_grupa(214)
        grupa = student.get_grupa()
        self.assertEqual(grupa, 214)

    def test_eq(self):
        student = Student('1', 'Andrei', 213)
        other = Student('1','Alex', 214)
        self.assertEqual(student,other)
        other2 = Student('2','Alex', 214)
        self.assertNotEqual(student,other2)

if __name__ == '__main__':
    unittest.main()
