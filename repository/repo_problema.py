from domain.problema import Problema


class ProblemaRepo:
    def __init__(self):
        self.__probleme = []

    def stocare(self, problema):
        '''
        Stocheaza in lista de probleme prooblema data
        :param problema: problema data
        type:Problema
        :return: -
        '''
        self.__probleme.append(problema)

    def get_all(self):
        '''
        Returneaza lista de probleme
        :return: lista de probleme
        type: list
        '''
        return self.__probleme

    def delete(self,index):
        '''
        Sterge elementul de pe pozitia index
        :param index: pozitia elementului
        type: int
        :return: problema stearsa
        type: Problema
        '''
        if index == -1:
            raise ValueError('Nu exista problema cu acest nr')
        problema = self.__probleme[index]
        self.__probleme.pop(index)
        return problema

    def size(self):
        '''
        Returneaza lungimea listei de probleme
        :return:
        '''
        return len(self.__probleme)

    def find_index(self, id):
        '''
        Gaseste indexul problemei de id dat
        :param id: numarul problemei
        type: string
        :return: index
        type: int
        '''
        index = -1
        for i in range(self.size()):
            if self.__probleme[i].get_nrlab_nrpb() == id:
                index = i
        return index

    def find(self, id):
        '''
        Gaseste problema dupa numar
        :param id: numarul problemei
        type: string
        :return:
        '''
        index = self.find_index(id)
        if index == -1:
            raise ValueError('Nu exista problema cu acest numar.')
        return self.__probleme[index]

    def update(self, nr, modified_pb):
        '''
        Modifica problema dupa numar
        :param nr: numarul problemei
        type:string
        :param modified_pb: problema modificata
        :return: old_pb - problema inainte de modificare
        '''
        index = self.find_index(nr)
        if index == -1:
            raise ValueError('Nu exista problema cu acest numar.')
        old_pb = self.__probleme[index]
        self.__probleme[index] = modified_pb
        return old_pb

class ProblemaFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        '''
        Incarca din fisier datele
        :return: lista
        '''
        try:
            f = open(self.__filename, 'r')
        except IOError:
            print('Fisier inexistent')

        probleme = []
        lines = f.readlines()
        for line in lines:
            nr, descriere, deadline = [token.strip() for token in line.split(';')]
            problema = Problema(nr, descriere, int(deadline))
            probleme.append(problema)
        f.close()
        return probleme

    def __save_to_file(self, probleme):
        '''
        Salveaza in fisier
        :param probleme: lista
        :return: -
        '''
        with open(self.__filename, 'w') as f:
            for problema in probleme:
                problema_string = problema.get_nrlab_nrpb() + ';' + problema.get_descriere() + ';' + str(
                   problema.get_deadline()) + '\n'
                f.write(problema_string)

    def stocare(self, problema):
        '''
        Stocheaza in lista de probleme prooblema data
        :param problema: problema data
        type:Problema
        :return: -
        '''
        probleme = self.__load_from_file()
        probleme.append(problema)
        self.__save_to_file(probleme)

    def delete(self,index):
        '''
        Sterge o problema
        :param index:
        :return: pb stearsa
        '''
        probleme = self.__load_from_file()
        problema = probleme[index]
        probleme.pop(index)
        self.__save_to_file(probleme)
        return problema

    def size(self):
        '''
        Returneaza lungimea listei
        :return:
        '''
        probleme = self.__load_from_file()
        return len(probleme)

    def find_index(self, id):
        '''
        Gaseste indexul dupa nr
        :param id:
        :return:
        '''
        probleme = self.__load_from_file()
        index = -1
        for i in range(self.size()):
            if probleme[i].get_nrlab_nrpb() == id:
                index = i
        return index

    def find(self, id):
        '''
        gaseste problema de id dat
        :param id:
        :return:
        '''
        probleme = self.__load_from_file()
        index = self.find_index(id)
        if index == -1:
            raise ValueError('Nu exista problema cu acest numar.')
        return probleme[index]

    def update(self, nr, modified_pb):
        '''
        Modifica problema de nr dat
        :param nr:
        :param modified_pb:
        :return:
        '''
        probleme = self.__load_from_file()
        index = self.find_index(nr)
        if index == -1:
            raise ValueError('Nu exista problema cu acest numar.')
        old_pb = probleme[index]
        probleme[index] = modified_pb
        self.__save_to_file(probleme)
        return old_pb

    def get_all(self):
        '''
        Returneaza toata lista de pb
        :return:
        '''
        probleme = self.__load_from_file()
        return probleme