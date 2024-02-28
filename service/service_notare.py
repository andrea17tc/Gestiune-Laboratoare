from domain.dto import StudentProblemaNotare
from domain.notare import Notare


class NotareService:
    def __init__(self, repo_notare, validator, repo_student, repo_problema):
        self.__repo_notare = repo_notare
        self.__validator_notare = validator
        self.__repo_student = repo_student
        self.__repo_problema = repo_problema

    def notare_student(self, studentID, nrlab_nrpb, nota):
        '''
        Adauga notarea la lista de notari
        :param studentID: id student notat
        type:int
        :param nrlab_nrpb: nr problema la care se face notarea
        type:string
        :param nota:
        :return:
        '''
        notare = Notare(studentID, nrlab_nrpb, nota)
        self.__validator_notare.validare(notare)
        self.__repo_notare.stocare(notare)
        return notare

    def get_all(self):
        '''
        Returneaza lista de notari
        :return: lista de notari
        type: list
        '''
        return self.__repo_notare.get_all()

    def get_all_for_id(self, id):
        '''
        Returneaza toate notarile studentului cu id dat
        :param id: ID-ul studentului
        type: int
        :return: notari_id - lista de notari a studentului de id dat
        type: list
        '''
        notari = self.get_all()
        notari_id = []
        for notare in notari:
            if notare.get_studentID() == id:
                notari_id.append(notare)
        return notari_id

    def get_all_for_nr(self, nr):
        '''
        Returneaza toate notarile problemei cu nr dat
        :param nr: nr problemei
        type: string
        :return: notari_nr - lista de notari
        type: list
        '''
        notari = self.get_all()
        notari_nr = []
        for notare in notari:
            if notare.get_nrlab_nrpb() == nr:
                notare_crt = StudentProblemaNotare(notare.get_studentID(), notare.get_nrlab_nrpb(), notare.get_nota())
                notari_nr.append(notare_crt)
        return notari_nr

    def set_nume_lista(self, nr):
        '''
        Seteaza nume obiectelor de tip StudentProblemaNotare din lista data
        :param nr: nr problemei
        :return: notari
        '''
        notari = self.get_all_for_nr(nr)
        for notare in notari:
            student = self.__repo_student.find(notare.get_studentID())
            notare.set_nume_student(student.get_nume())

        return notari

    def ordonare(self, notari):
        '''
        Ordoneaza lista dupa nota si nume
        :param notari:
        :return:
        '''
        notari.sort(key=lambda x: (x.get_nota(), x.get_nume_student()))

        return notari

    def key1(self, x):
        return x.get_nota()

    def key2(self, x):
        return x.get_nume_student()

    def compare(self, first, second, key1, key2, reverse):
        '''
        comparator
        :param first: primul element de comparat
        :param second: al doilea element de comparat
        :param reverse: True pentru sir sortat crescator
                        False pentru sir sortat descrescator
        :return:
        '''
        if key1 is None:
            key1 = lambda x:x
        if key2 is None:
            key2 = lambda x:x
        if reverse is True:
            if key1(first) < key1(second):
                return 1
            elif key1(first) == key1(second):
                if key2(first) < key2(second):
                    return 1
                elif key2(first) == key2(second):
                    return 1
            return 0
        elif reverse is False:
            if key1(first) < key1(second):
                return 0
            elif key1(first) == key1(second):
                if key2(first) < key2(second):
                    return 0
                elif key2(first) == key2(second):
                    return 0
            return 1

    def partition(self, notari, left, right, key1, key2, reverse):
        """
        Split the values:
        smaller pivot greater
        return pivot position
        post: left we have < pivot
        right we have > pivot
        """
        pivot = notari[left]
        i = left
        j = right
        while i != j:
            while self.compare(notari[j], pivot,key1, key2, reverse) == 1 and i < j:
                j = j - 1
            notari[i] = notari[j]
            while self.compare(notari[j], pivot,key1, key2, reverse) == 0 and i < j:
                i = i + 1
            notari[j] = notari[i]
        notari[i] = pivot
        return i

    def quickSortRec(self, notari, left, right, key1=None, key2=None, reverse=False):
        # partition the list
        pos = self.partition(notari, left, right, key1, key2, reverse)
        # order the left part
        if left < pos - 1:
            self.quickSortRec(notari, left, pos - 1, key1, key2, reverse)
        # order the right part
        if pos + 1 < right:
            self.quickSortRec(notari, pos + 1, right, key1, key2, reverse)

    def quick_sort(self, notari):
        '''
        Sorteaza lista de notari, metoda Quick Sort
        :param notari:
        :return: lista ordonata

        Complexitate:

        best case - O(n*log(n)) , elementele sunt ordonate deja
        worst case -  O(n^2) , elementele sunt ordonate invers
        average cas - O(n*log(n)), elementele se gasesc aleatoriu in sir

        '''
        size = len(notari)
        self.quickSortRec(notari, 0, size - 1, key1=self.key1, key2=self.key2, reverse=False)
        return notari

    def gnome_sort_alg(self, notari, n, key1=None, key2=None, reverse=False):
        '''
        Sorteaza lista de notari cu metoda Gnome sort
        :param notari:
        :param n:
        :param key1:
        :param key2:
        :param reverse:
        :return:
        '''
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if self.compare(notari[index], notari[index-1], key1, key2, reverse) == 1:
                index = index + 1
            else:
                notari[index], notari[index - 1] = notari[index - 1], notari[index]
                index = index - 1

        return notari

    def GnomeSort(self, notari):
        '''
        Returneaza lista de notari ordonata, metoda Gnome Sort
        :param notari:
        :return: lista ordonata
        '''
        size = len(notari)
        self.gnome_sort_alg(notari, size-1, key1=self.key1, key2=self.key2, reverse=False)
        return notari

    def notari_ordonate_problema(self, nr):
        '''
        Returneaza lista ordonata cu numele setate
        :param nr:
        :return:
        '''
        notari = self.set_nume_lista(nr)
        notari_ord = self.quick_sort(notari)
        return notari_ord

    def sterge_student_si_notari(self, id):
        '''
        Sterge notarile studentului de id dat
        :param id: id student
        type: int
        :return: -
        '''
        notari = self.get_all()
        index = self.__repo_notare.find_index_by_id(id)
        while index != -1:
            self.__repo_notare.delete(index)
            index = self.__repo_notare.find_index_by_id(id)

    def sterge_student_si_notari_rec(self, id):
        '''
        Sterge notarile studentului de id dat RECURSIV
        :param id: id student
        type: int
        :return: -
        '''
        notari = self.get_all()
        index = self.__repo_notare.find_index_by_id(id)
        if index != -1:
            self.__repo_notare.delete(index)
            self.sterge_student_si_notari_rec(id)

    def sterge_problema_si_notari(self, nr):
        '''
        Sterge notarile la problema de nr dat
        :param nr:
        :return:
        '''
        notari = self.get_all()
        index = self.__repo_notare.find_index_by_nr(nr)
        while index != -1:
            self.__repo_notare.delete(index)
            index = self.__repo_notare.find_index_by_nr(nr)

    def sterge_problema_si_notari_rec(self, nr):
        '''
        Sterge notarile la problema de nr dat RECURSIV
        :param nr:
        :return:
        '''
        notari = self.get_all()
        index = self.__repo_notare.find_index_by_nr(nr)
        if index != -1:
            self.__repo_notare.delete(index)
            self.sterge_problema_si_notari_rec(nr)

    def medie_laboratoare_student(self, studentID):
        '''
        Calculeaza media
        :param studentID:id
        :return: avg - media
        '''
        notari = self.get_all_for_id(studentID)
        medie = 0

        for notare in notari:
            medie += notare.get_nota()

        l = len(notari)
        avg = medie/l
        return avg

    def studenti_medie_sub_5(self):
        '''
        Returneaza studenti cu media sub 5
        :return: lista
        '''
        nr_studenti = self.__repo_student.size()

        studenti_picati = []
        for i in range(1,nr_studenti+1):
            medie = self.medie_laboratoare_student(i)
            if medie < 5:
                student = self.__repo_student.find(i)
                studenti_picati.append([student.get_nume(), medie])

        return studenti_picati

    def studenti_medie_peste_7(self):
        '''
        Returneaza studenti cu media sub 7
        :return: lista
        '''
        nr_studenti = self.__repo_student.size()

        studenti_buni = []
        for i in range(1, nr_studenti + 1):
            medie = self.medie_laboratoare_student(i)
            if medie > 7:
                student = self.__repo_student.find(i)
                studenti_buni.append([student.get_nume(), medie])
        self.__repo_notare.salveaza_in_fisier(studenti_buni)
        return studenti_buni