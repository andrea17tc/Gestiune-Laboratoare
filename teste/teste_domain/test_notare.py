from domain.notare import Notare


def test_get_studentID(notare):
    id = notare.get_studentID()
    assert(id == 1)


def test_get_nrlab_nrpb(notare):
    nrlab_nrpb = notare.get_nrlab_nrpb()
    assert(nrlab_nrpb == '1_1')


def test_get_nota(notare):
    nota = notare.get_nota()
    assert(nota == 7)


def test_set_nota(notare):
    notare.set_nota(10)
    nota = notare.get_nota()
    assert (nota == 10)


def Test_Notare():
    notare = Notare(1,'1_1',7)
    test_get_studentID(notare)
    test_get_nrlab_nrpb(notare)
    test_get_nota(notare)
    test_set_nota(notare)