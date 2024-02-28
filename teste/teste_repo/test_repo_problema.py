from domain.problema import Problema
from repository.repo_problema import ProblemaRepo


def test_stocare():
    repo = ProblemaRepo()
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    problema3 = Problema('1_3', 'Ana are caise', 8)
    problema4 = Problema('1_4', 'Ana are prune', 12)
    repo.stocare(problema1)
    repo.stocare(problema2)
    repo.stocare(problema3)
    repo.stocare(problema4)
    probleme = repo.get_all()
    assert(len(probleme) == 4)


def test_delete():
    repo = ProblemaRepo()
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    problema3 = Problema('1_3', 'Ana are caise', 8)
    problema4 = Problema('1_4', 'Ana are prune', 12)
    repo.stocare(problema1)
    repo.stocare(problema2)
    repo.stocare(problema3)
    repo.stocare(problema4)
    problema = repo.delete(1)
    probleme = repo.get_all()
    assert(len(probleme) == 3)
    assert(probleme == [problema1, problema3, problema4])
    assert(problema == problema2)


def test_size():
    repo = ProblemaRepo()
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    problema3 = Problema('1_3', 'Ana are caise', 8)
    problema4 = Problema('1_4', 'Ana are prune', 12)
    repo.stocare(problema1)
    repo.stocare(problema2)
    repo.stocare(problema3)
    repo.stocare(problema4)
    size = repo.size()
    assert(size == 4)


def test_find_index():
    repo = ProblemaRepo()
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    problema3 = Problema('1_3', 'Ana are caise', 8)
    problema4 = Problema('1_4', 'Ana are prune', 12)
    repo.stocare(problema1)
    repo.stocare(problema2)
    repo.stocare(problema3)
    repo.stocare(problema4)
    index = repo.find_index('1_2')
    assert(index == 1)
    index = repo.find_index('2_2')
    assert(index == -1)


def test_find():
    repo = ProblemaRepo()
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    problema3 = Problema('1_3', 'Ana are caise', 8)
    problema4 = Problema('1_4', 'Ana are prune', 12)
    repo.stocare(problema1)
    repo.stocare(problema2)
    repo.stocare(problema3)
    repo.stocare(problema4)
    problema = repo.find('1_1')
    assert(problema == problema1)


def test_update():
    repo = ProblemaRepo()
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    problema3 = Problema('1_3', 'Ana are caise', 8)
    problema4 = Problema('1_4', 'Ana are prune', 12)
    repo.stocare(problema1)
    repo.stocare(problema2)
    repo.stocare(problema3)
    repo.stocare(problema4)
    problema_noua = Problema('2_2', 'Ana are piersici', 20)
    problema = repo.update('1_1', problema_noua)
    probleme = repo.get_all()
    assert(len(probleme) == 4)
    assert(problema == Problema('1_1', 'Ana are mere', 3))
    assert(probleme[0] == problema_noua)


def Test_Repo_Problema():
    test_stocare()
    test_delete()
    test_size()
    test_find_index()
    test_find()
    test_update()