import unittest

from domain.problema import Problema


class TestCaseProblemaDomain(unittest.TestCase):

    def test_get_nrlab_nrpb(self):
        problema = Problema('1_1', 'Ana are mere', 23)
        nrlab_nrpb = problema.get_nrlab_nrpb()
        self.assertEqual (nrlab_nrpb, '1_1')

    def test_get_descriere(self):
        problema = Problema('1_1', 'Ana are mere', 23)
        descriere = problema.get_descriere()
        self.assertEqual(descriere, 'Ana are mere')

    def test_get_deadline(self):
        problema = Problema('1_1', 'Ana are mere', 23)
        deadline = problema.get_deadline()
        self.assertEqual(deadline, 23)

    def test_set_descriere(self):
        problema = Problema('1_1', 'Ana are mere', 23)
        problema.set_descriere('Ana are pere')
        descriere = problema.get_descriere()
        self.assertEqual(descriere, 'Ana are pere')

    def test_set_deadline(self):
        problema = Problema('1_1', 'Ana are mere', 23)
        problema.set_deadline(25)
        deadline = problema.get_deadline()
        self.assertEqual(deadline, 25)

    def test_eq(self):
        problema = Problema('1_1', 'Ana are mere', 23)
        problema2 = Problema('1_1', 'Ana are mere', 23)
        problema3 = Problema('1_2', 'Ana are pere', 2)
        self.assertEqual(problema, problema2)
        self.assertNotEqual(problema,problema3)


if __name__ == '__main__':
    unittest.main()
