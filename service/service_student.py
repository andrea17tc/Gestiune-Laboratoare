from domain.student import Student


class StudentService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def adauga_student(self, id, nume, grupa):
        '''
        Adauga student la lista de studenti
        :param id: ID-ul studentului
        type: int
        :param nume: numele studentului
        type: string
        :param grupa: grupa studentului
        type: int
        :return: s - studentul
        type: Student
        '''
        s = Student(id, nume, grupa)
        self.__validator.validare(s)
        self.__validator.validare_adaugare(id)
        self.__repo.stocare(s)
        return s

    def get_all(self):
        '''
        Returneaza lista de studenti
        :return:
        '''
        return self.__repo.get_all()

    def delete_by_id(self, id):
        '''
        Sterge studentul de id dat
        :param id:
        :return:
        '''
        self.__validator.validare_ID(id)
        index = self.__repo.find_index(id)
        student = self.__repo.delete(index)
        return student

    def modifica_student(self, id, nume, grupa):
        '''
        Modifica studentul de id dat in studentul dat
        :param id: id ul studentului de modificat
        type: int
        :param student: studentul modificat
        type: Student
        :return: old_stud - studentul inainte de modificare
        '''
        student = Student(id, nume, grupa)
        self.__validator.validare(student)
        self.__validator.validare_modificare(id)
        old_stud = self.__repo.update(id, student)
        return old_stud

    def cauta_student(self, id):
        '''
        Cauta studentul de id dat
        :param id: id ul studentului cautat
        :return: studentul cautat
        '''
        self.__validator.validare_cautare(id)
        return self.__repo.find(id)