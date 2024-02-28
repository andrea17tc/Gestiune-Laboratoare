class ValidatorStudent:
    def __init__(self, repo):
        self.__repo = repo
    def validare_ID(self, id):
        if id < 1:
            raise ValueError("ID invalid")
    def validare_nume(self,nume):
        if len(nume) < 3 or len(nume) > 50:
            raise ValueError("Nume invalid")
    def validare_grupa(self,grupa):
        if grupa < 210 or grupa > 917:
            raise ValueError("Grupa invalida")
    def validare(self,stud):
        self.validare_ID(stud.get_studentID())
        self.validare_nume(stud.get_nume())
        self.validare_grupa(stud.get_grupa())

    def validare_adaugare(self, id):
        index = self.__repo.find_index(id)
        if index != -1:
            raise ValueError("Studentul este inregistrat deja")

    def validare_modificare(self, id):
        self.validare_ID(id)
        index = self.__repo.find_index(id)
        if index == -1:
            raise ValueError("Studentul nu exista")

    def validare_cautare(self, id):
        self.validare_ID(id)
        index = self.__repo.find_index(id)
        if index == -1:
            raise ValueError("Studentul nu exista")