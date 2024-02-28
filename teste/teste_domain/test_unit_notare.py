import unittest

from domain.notare import Notare


class TestCaseNotareDomain(unittest.TestCase):

    def test_get_studentID(self):
        notare = Notare(1, '1_1', 7)
        id = notare.get_studentID()
        self.assertEqual(id, 1)

    def test_get_nrlab_nrpb(self):
        notare = Notare(1, '1_1', 7)
        nrlab_nrpb = notare.get_nrlab_nrpb()
        self.assertEqual(nrlab_nrpb, '1_1')

    def test_get_nota(self):
        notare = Notare(1, '1_1', 7)
        nota = notare.get_nota()
        self.assertEqual(nota, 7)

    def test_set_nota(self):
        notare = Notare(1, '1_1', 7)
        notare.set_nota(10)
        nota = notare.get_nota()
        self.assertEqual(nota, 10)

    def test_eq(self):
        notare = Notare(1, '1_1', 7)
        notare2 = Notare(1, '1_1', 7)
        self.assertEqual(notare, notare2)
        notare3 = Notare(3, '1_1', 7)
        self.assertNotEqual(notare, notare3)

if __name__ == '__main__':
    unittest.main()
