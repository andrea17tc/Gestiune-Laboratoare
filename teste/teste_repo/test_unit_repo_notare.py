import unittest

from domain.notare import Notare
from repository.repo_notare import NotareRepo


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = NotareRepo()

        notare1 = Notare(1, '1_1', 7)
        notare2 = Notare(2, '1_2', 9)
        notare3 = Notare(3, '1_3', 12)
        self.__repo.stocare(notare1)
        self.__repo.stocare(notare2)
        self.__repo.stocare(notare3)

    def test_stocare(self):
        notari = self.__repo.get_all()
        self.assertEqual(len(notari), 3)

    def test_size(self):
        size = self.__repo.size()
        self.assertEqual(size, 3)

    def test_delete(self):
        notare1 = Notare(1, '1_1', 7)
        notare = self.__repo.delete(0)
        notari = self.__repo.get_all()
        self.assertEqual(len(notari), 2)
        self.assertEqual(notare, notare1)

    def test_find_index_by_id(self):
        index = self.__repo.find_index_by_id(1)
        self.assertEqual(index, 0)
        index2 = self.__repo.find_index_by_id(4)
        self.assertEqual(index2, -1)

    def test_find_index_by_nr(self):
        index = self.__repo.find_index_by_nr('1_1')
        self.assertEqual(index, 0)
        index2 = self.__repo.find_index_by_nr('1_4')
        self.assertEqual(index2, -1)

    def test_find(self):
        notare4 = self.__repo.find(1, '1_1')
        self.assertEqual(notare4, 0)
        notare5 = self.__repo.find(1, '2_2')
        self.assertEqual(notare5, -1)

if __name__ == '__main__':
    unittest.main()
