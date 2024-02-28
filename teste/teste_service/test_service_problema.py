from domain.problema import Problema
from domain.validare.validare_problema import ValidatorProblema
from repository.repo_problema import ProblemaRepo
from service.service_problema import ProblemaService


def test_adauga_problema():
    repo = ProblemaRepo()
    val = ValidatorProblema(repo)
    srv = ProblemaService(repo, val)
    try:
        problema1 = srv.adauga_problema('1_1', 'Ana are mere', 3)
        assert True
    except ValueError:
        assert False

    try:
        problema2 = srv.adauga_problema('1','Ana are pere', 50)
        assert False
    except ValueError:
        assert True


def test_modifica_problema():
    repo = ProblemaRepo()
    val = ValidatorProblema(repo)
    srv = ProblemaService(repo, val)
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    repo.stocare(problema1)
    repo.stocare(problema2)
    problema_noua = Problema('1_1','Ana are caise', 4)
    problema = srv.modifica_problema('1_1','Ana are caise', 4)
    assert(problema == Problema('1_1','Ana are caise', 4))
    try:
        problema3 = srv.modifica_problema('1_3','Ana are caise', 4)
        assert False
    except ValueError:
        assert True


def test_cauta_problema():
    repo = ProblemaRepo()
    val = ValidatorProblema(repo)
    srv = ProblemaService(repo, val)
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    repo.stocare(problema1)
    repo.stocare(problema2)
    problema = srv.cauta_problema('1_2')
    assert(problema == problema2)
    try:
        problema3 = srv.cauta_problema('1')
        assert False
    except ValueError:
        assert True

    try:
        problema4 = srv.cauta_problema('1_3')
        assert False
    except ValueError:
        assert True


def test_delete_by_nr():
    repo = ProblemaRepo()
    val = ValidatorProblema(repo)
    srv = ProblemaService(repo, val)
    problema1 = Problema('1_1', 'Ana are mere', 3)
    problema2 = Problema('1_2', 'Ana are pere', 5)
    repo.stocare(problema1)
    repo.stocare(problema2)
    problema = srv.delete_by_nr('1_1')
    assert(problema == problema1)
    probleme = srv.get_all()
    assert(len(probleme) == 1)


def Test_Service_Problema():
    test_adauga_problema()
    test_modifica_problema()
    test_delete_by_nr()
    test_cauta_problema()
