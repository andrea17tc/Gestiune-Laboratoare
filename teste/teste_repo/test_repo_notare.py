from domain.notare import Notare
from repository.repo_notare import NotareRepo


def test_stocare():
    repo = NotareRepo()
    notare1 = Notare(1,'1_1',7)
    notare2 = Notare(2,'1_2',9)
    notare3 = Notare(3,'1_3', 12)
    repo.stocare(notare1)
    repo.stocare(notare2)
    repo.stocare(notare3)
    notari = repo.get_all()
    assert(len(notari) == 3)


def test_size():
    repo = NotareRepo()
    notare1 = Notare(1, '1_1', 7)
    notare2 = Notare(2, '1_2', 9)
    notare3 = Notare(3, '1_3', 12)
    repo.stocare(notare1)
    repo.stocare(notare2)
    repo.stocare(notare3)
    size = repo.size()
    assert(size == 3)


def test_delete():
    repo = NotareRepo()
    notare1 = Notare(1, '1_1', 7)
    notare2 = Notare(2, '1_2', 9)
    notare3 = Notare(3, '1_3', 12)
    repo.stocare(notare1)
    repo.stocare(notare2)
    repo.stocare(notare3)
    notare = repo.delete(0)
    notari = repo.get_all()
    assert (len(notari) == 2)
    assert(notare == notare1)


def test_find_index_by_id():
    repo = NotareRepo()
    notare1 = Notare(1, '1_1', 7)
    notare2 = Notare(2, '1_2', 9)
    notare3 = Notare(3, '1_3', 12)
    repo.stocare(notare1)
    repo.stocare(notare2)
    repo.stocare(notare3)
    index = repo.find_index_by_id(1)
    assert(index == 0)
    index2 = repo.find_index_by_id(4)
    assert(index2 == -1)


def test_find_index_by_no():
    repo = NotareRepo()
    notare1 = Notare(1, '1_1', 7)
    notare2 = Notare(2, '1_2', 9)
    notare3 = Notare(3, '1_3', 12)
    repo.stocare(notare1)
    repo.stocare(notare2)
    repo.stocare(notare3)
    index = repo.find_index_by_nr('1_1')
    assert (index == 0)
    index2 = repo.find_index_by_nr('1_4')
    assert (index2 == -1)


def test_find():
    repo = NotareRepo()
    notare1 = Notare(1, '1_1', 7)
    notare2 = Notare(2, '1_2', 9)
    notare3 = Notare(3, '1_3', 12)
    repo.stocare(notare1)
    repo.stocare(notare2)
    repo.stocare(notare3)
    notare4 = repo.find(1, '1_1')
    assert(notare4 == 0)
    notare5 = repo.find(1,'2_2')
    assert(notare5 == -1)


def Test_Repo_Notare():
    test_stocare()
    test_size()
    test_delete()
    test_find()
