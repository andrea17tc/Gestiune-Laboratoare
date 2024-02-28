import unittest

from domain.problema import Problema
from domain.validare.validare_problema import ValidatorProblema
from repository.repo_problema import ProblemaRepo
from service.service_problema import ProblemaService


class TestCaseProblemaService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ProblemaRepo()
        self.__val = ValidatorProblema(self.__repo)
        self.__srv = ProblemaService(self.__repo, self.__val)

        problema1 = Problema('1_1', 'Ana are mere', 3)
        problema2 = Problema('1_2', 'Ana are pere', 5)
        self.__repo.stocare(problema1)
        self.__repo.stocare(problema2)

    def test_adauga_problema(self):
        self.assertTrue(self.__srv.adauga_problema('1_3', 'Ana are mere', 3))
        self.assertRaises(ValueError, self.__srv.adauga_problema,'1','Ana are pere', 50 )

    def test_modifica_problema(self):
        problema = self.__srv.modifica_problema('1_1', 'Ana are caise', 4)
        self.assertEqual(problema, Problema('1_1', 'Ana are caise', 4))
        self.assertRaises(ValueError, self.__srv.modifica_problema, '1_3','Ana are caise', 4)

    def test_cauta_problema(self):
        problema2 = Problema('1_2', 'Ana are pere', 5)
        problema = self.__srv.cauta_problema('1_2')
        self.assertEqual(problema, problema2)
        self.assertRaises(ValueError, self.__srv.cauta_problema, '1')

    def test_delete_by_nr(self):
        problema1 = Problema('1_1', 'Ana are mere', 3)
        problema = self.__srv.delete_by_nr('1_1')
        self.assertEqual(problema, problema1)
        probleme = self.__srv.get_all()
        self.assertEqual(len(probleme), 1)
        self.assertRaises(ValueError, self.__srv.delete_by_nr, '1')
        self.assertRaises(ValueError, self.__srv.delete_by_nr, '1_5')

if __name__ == '__main__':
    unittest.main()
