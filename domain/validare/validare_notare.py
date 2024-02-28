class ValidatorNotare:
    def __init__(self, repo_notare, repo_student, repo_problema):
        self.__repo_notare = repo_notare
        self.__repo_student = repo_student
        self.__repo_problema = repo_problema

    def validare_nota(self,nota):
        if nota < 1 or nota > 10:
            raise ValueError("Nota invalida")
    def validare_id(self, id):
        index = self.__repo_student.find_index(id)
        if index == -1:
            raise ValueError('Nu exista student cu acest id')
    def validare_nr(self, nr):
        index = self.__repo_problema.find_index(nr)
        if index == -1:
            raise ValueError('Nu exista problema cu acest numar')
    def validare(self, notare):
        self.validare_id(notare.get_studentID())
        self.validare_nr(notare.get_nrlab_nrpb())
        index = self.__repo_notare.find(notare.get_studentID(), notare.get_nrlab_nrpb())
        if index != -1:
            raise ValueError('Notarea exista deja')
        self.validare_nota(notare.get_nota())