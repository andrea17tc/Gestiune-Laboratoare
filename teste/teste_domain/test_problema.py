from domain.problema import Problema


def test_get_nrlab_nrpb(problema):
    nrlab_nrpb = problema.get_nrlab_nrpb()
    assert (nrlab_nrpb == '1_1')


def test_get_descriere(problema):
    descriere = problema.get_descriere()
    assert(descriere == 'Ana are mere')


def test_get_deadline(problema):
    deadline = problema.get_deadline()
    assert(deadline == 23)


def test_set_descriere(problema):
    problema.set_descriere('Ana are pere')
    descriere = problema.get_descriere()
    assert (descriere == 'Ana are pere')


def test_set_deadline(problema):
    problema.set_deadline(25)
    deadline = problema.get_deadline()
    assert(deadline == 25)


def Test_Problema():
    problema = Problema('1_1', 'Ana are mere', 23)
    test_get_nrlab_nrpb(problema)
    test_get_descriere(problema)
    test_get_deadline(problema)
    test_set_descriere(problema)
    test_set_deadline(problema)