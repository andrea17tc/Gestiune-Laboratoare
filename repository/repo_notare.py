class NotareRepo:
    def __init__(self):
        self.__notari= []

    def stocare(self, notare):
        '''
        Stocheaza in lista de notari notarea data
        :param notare: notarea
        type:Notare_Laborator
        :return: -
        '''
        self.__notari.append(notare)

    def get_all(self):
        '''
        Returneaza lista de notari
        :return: lista
        type: list
        '''
        return self.__notari

    def size(self):
        '''
        Returneaza lungimea listei de notari
        :return:
        '''
        return len(self.__notari)

    def delete(self, index):
        '''
        Sterge elementul de pe pozitia index
        :param index: pozitia elementului
        type: int
        :return: notare - notarea stearsa
        '''
        notare = self.__notari[index]
        self.__notari.pop(index)
        return notare

    def find_index_by_id(self, studentID):
        '''
        Gaseste indexul notarii studentului de id studentID
        :param studentID: id student
        type:int
        :return: index - indexul notarii cautate
        type:int
        '''
        index = -1
        for i in range(self.size()):
            if self.__notari[i].get_studentID() == studentID:
                index = i
        return index

    def find_index_by_nr(self, nrlab_nrpb):
        '''
        Gaseste indexul notarii la problema nrlab_nrpb
        :param nrlab_nrpb: numarul problemei
        type: string
        :return: index - indexul notarii cautate
        type: int
        '''
        index = -1
        for i in range(self.size()):
            if self.__notari[i].get_nrlab_nrpb() == nrlab_nrpb:
                index = i
        return index

    def find(self, id, nrlab_nrpb):
        '''
        :param id:
        :param nrlab_nrpb:
        :return:
        '''
        index = -1
        for i in range(self.size()):
            if self.__notari[i].get_nrlab_nrpb() == nrlab_nrpb and self.__notari[i].get_studentID() == id:
                index = i
        return index

class NotareFileRepo():
    def __init__(self, filename, filename2):
        self.__notari = []
        self.__filename = filename
        self.__filename2 = filename2

    def __save_to_file(self, file,notari):
        '''
        Salveaza in fisier
        :param notari:
        :return:
        '''
        with open(file, 'w') as f:
            for notare in notari:
                notare_string = str(notare) + '\n'
                f.write(notare_string)

    def stocare(self, notare):
        '''
        Stocheaza in lista de notari notarea data
        :param notare: notarea
        type:Notare_Laborator
        :return: -
        '''
        self.__notari.append(notare)
        notari = self.get_all()
        self.__save_to_file(self.__filename2, notari)


    def salveaza_in_fisier(self, file, lista):
        self.__save_to_file(file, lista)

    def get_all(self):
        '''
        Returneaza lista de notari
        :return: lista
        type: list
        '''
        return self.__notari

    def size(self):
        '''
        Returneaza lungimea listei de notari
        :return:
        '''
        return len(self.__notari)

    def delete(self, index):
        '''
        Sterge elementul de pe pozitia index
        :param index: pozitia elementului
        type: int
        :return: notare - notarea stearsa
        '''
        notare = self.__notari[index]
        self.__notari.pop(index)
        self.__save_to_file(self.__filename2, self.__notari)
        return notare

    def find_index_by_id(self, studentID):
        '''
        Gaseste indexul notarii studentului de id studentID
        :param studentID: id student
        type:int
        :return: index - indexul notarii cautate
        type:int
        '''
        index = -1
        for i in range(self.size()):
            if self.__notari[i].get_studentID() == studentID:
                index = i
        return index

    def find_index_by_nr(self, nrlab_nrpb):
        '''
        Gaseste indexul notarii la problema nrlab_nrpb
        :param nrlab_nrpb: numarul problemei
        type: string
        :return: index - indexul notarii cautate
        type: int
        '''
        index = -1
        for i in range(self.size()):
            if self.__notari[i].get_nrlab_nrpb() == nrlab_nrpb:
                index = i
        return index

    def find(self, id, nrlab_nrpb):
        '''
        :param id:
        :param nrlab_nrpb:
        :return:
        '''
        index = -1
        for i in range(self.size()):
            if self.__notari[i].get_nrlab_nrpb() == nrlab_nrpb and self.__notari[i].get_studentID() == id:
                index = i
        return index