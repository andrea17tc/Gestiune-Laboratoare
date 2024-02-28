import unittest

from domain.problema import Problema
from repository.repo_problema import ProblemaRepo, ProblemaFileRepo


class TestCaseProblemaRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ProblemaRepo()

        problema1 = Problema('1_1', 'Ana are mere', 3)
        problema2 = Problema('1_2', 'Ana are pere', 5)
        problema3 = Problema('1_3', 'Ana are caise', 8)
        problema4 = Problema('1_4', 'Ana are prune', 12)
        self.__repo.stocare(problema1)
        self.__repo.stocare(problema2)
        self.__repo.stocare(problema3)
        self.__repo.stocare(problema4)

    def test_stocare(self):
        probleme = self.__repo.get_all()
        self.assertEqual(len(probleme), 4)

    def test_delete(self):
        problema1 = Problema('1_1', 'Ana are mere', 3)
        problema2 = Problema('1_2', 'Ana are pere', 5)
        problema3 = Problema('1_3', 'Ana are caise', 8)
        problema4 = Problema('1_4', 'Ana are prune', 12)
        problema = self.__repo.delete(1)
        probleme = self.__repo.get_all()
        self.assertEqual (len(probleme), 3)
        self.assertEqual (probleme , [problema1, problema3, problema4])
        self.assertEqual (problema, problema2)

    def test_size(self):
        size = self.__repo.size()
        self.assertEqual(size, 4)

    def test_find_index(self):
        index = self.__repo.find_index('1_2')
        self.assertEqual(index, 1)
        index = self.__repo.find_index('2_2')
        self.assertEqual(index, -1)

    def test_find(self):
        problema1 = Problema('1_1', 'Ana are mere', 3)
        problema = self.__repo.find('1_1')
        self.assertEqual(problema, problema1)
        #problema2 = self.__repo.find('2')
        self.assertRaises(ValueError,self.__repo.find, '2')

    def test_update(self):
        problema_noua = Problema('2_2', 'Ana are piersici', 20)
        problema = self.__repo.update('1_1', problema_noua)
        probleme = self.__repo.get_all()
        self.assertEqual(len(probleme), 4)
        self.assertEqual(problema, Problema('1_1', 'Ana are mere', 3))
        self.assertEqual(probleme[0], problema_noua)
        self.assertRaises(ValueError,self.__repo.update,'2',problema_noua )

if __name__ == '__main__':
    unittest.main()
