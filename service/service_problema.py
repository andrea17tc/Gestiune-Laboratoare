from domain.problema import Problema


class ProblemaService:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def adauga_problema(self, nrlab_nrpb, descriere, deadline):
        '''
        Adauga problema in lista de probleme
        :param nrlab_nrpb: nr problema
        type:string
        :param descriere: descriere problema
        type: string
        :param deadline: deadline problema
        type: int
        :return: p - problema
        type: Problema
        '''
        p = Problema(nrlab_nrpb, descriere, deadline)
        self.__validator.validare(p)
        self.__validator.validare_adaugare(nrlab_nrpb)
        self.__repo.stocare(p)
        return p

    def get_all(self):
        '''
        Returneaza lista de probleme
        :return: lista de probleme
        type: list
        '''
        return self.__repo.get_all()

    def delete_by_nr(self, nr):
        '''
        Sterge problema de nr dat
        :param nr: nr problema
        :return:
        '''
        self.__validator.validare_nrlab_nrpb(nr)
        index = self.__repo.find_index(nr)
        problema = self.__repo.delete(index)
        return problema

    def modifica_problema(self, nr, descriere, deadline):
        '''
        Modifica problema cu numarul nr in problema data
        :param nr: nr problemei de modificat
        :param problema: problema modificata
        :return: old_pb - problema inainte de modificare
        '''
        problema = Problema(nr, descriere, deadline)
        self.__validator.validare(problema)
        self.__validator.validare_modificare(nr)
        old_pb = self.__repo.update(nr, problema)
        return old_pb

    def cauta_problema(self, nr):
        '''
        Cauta problema dupa numar
        :param nr: nr problema
        type:string
        :return: problema cautata
        '''
        self.__validator.validare_cautare(nr)
        return self.__repo.find(nr)