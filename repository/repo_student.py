from domain.student import Student


class StudentRepo:
    def __init__(self):
        self.__studenti = []

    def stocare(self, student):
        '''
        Stocheaza in lista de studenti studentul dat
        :param student: studentul dat
        type: Student
        :return: -
        '''
        self.__studenti.append(student)

    def get_all(self):
        '''
        Returneaza lista de studenti
        :return: lista de studenti
        type:list
        '''
        return self.__studenti

    def delete(self,index):
        '''
        Sterge elementul de pe pozitia index
        :param index: pozitia
        type:int
        :return:student - studentul sters
        '''
        if index == -1:
            raise ValueError('Nu exista student cu acest id')
        student = self.__studenti[index]
        self.__studenti.pop(index)
        return student

    def size(self):
        '''
        Returneaza lungimea listei de studenti
        :return:
        '''
        return len(self.__studenti)

    def find_index(self, id):
        '''
        Gaseste indexul studentului de id dat
        :param id: ID-ul studentului
        type:int
        :return: index
        type: int
        '''
        index = -1
        for i in range(self.size()):
            if self.__studenti[i].get_studentID() == id:
                index = i
        return index

    def find(self, id):
        '''
        Gaseste studentul de id dat
        :param id: ID-ul studentului
        type: int
        :return: studentul - daca exista student cu ID dat
                 None - daca nu exista student cu ID dat
        '''
        index = self.find_index(id)
        if index == -1:
            raise ValueError('Nu exista student cu acest id.')
        return self.__studenti[index]

    def update(self, id, modified_stud):
        '''
        Modifica studentul dupa id.
        :param id: ID-ul studentului
        type:int
        :param modified_stud: Studentul modificat
        type:Student
        :return: old-stud - Studentul inainte de modificare
        type:Student
        '''
        index = self.find_index(id)
        if index == -1:
            raise ValueError('Nu exista student cu acest id.')
        old_stud = self.__studenti[index]
        self.__studenti[index] = modified_stud
        return old_stud

class StudentFileRepo:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            print('Fisier inexistent')

        studenti = []
        lines = f.readlines()
        for line in lines:
            id, nume, grupa = [token.strip() for token in line.split(';')]
            student = Student(int(id), nume, int(grupa))
            studenti.append(student)
        f.close()
        return studenti

    def __save_to_file(self,studenti):
        with open(self.__filename, 'w') as f:
            for student in studenti:
                student_string = str(student.get_studentID()) + ';' + student.get_nume() + ';' + str(
                    student.get_grupa()) + '\n'
                f.write(student_string)

    def stocare(self, problema):
        '''
        Stocheaza in lista de studenti studentul dat
        :param studentul dat
        type:Student
        :return: -
        '''
        studenti = self.__load_from_file()
        studenti.append(problema)
        self.__save_to_file(studenti)

    def delete(self, index):
        studenti = self.__load_from_file()
        if index == -1:
            raise ValueError('Nu exista student cu acest id')
        student = studenti[index]
        studenti.pop(index)
        self.__save_to_file(studenti)
        return student

    def size(self):
        studenti = self.__load_from_file()
        return len(studenti)

    def find_index(self, id):
        studenti = self.__load_from_file()
        index = -1
        for i in range(self.size()):
            if studenti[i].get_studentID() == id:
                index = i
        return index

    def find(self, id):
        studenti = self.__load_from_file()
        index = self.find_index(id)
        if index == -1:
            raise ValueError('Nu exista student cu acest id.')
        return studenti[index]

    def update(self, id, modified_stud):
        studenti = self.__load_from_file()
        index = self.find_index(id)
        if index == -1:
            raise ValueError('Nu exista student cu acest id.')
        old_stud = studenti[index]
        studenti[index] = modified_stud
        self.__save_to_file(studenti)
        return old_stud

    def get_all(self):
        studenti = self.__load_from_file()
        return studenti
