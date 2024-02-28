class ValidatorProblema:
    def __init__(self, repo):
        self.__repo = repo
    def validare_nrlab_nrpb(self,nrlab_nrpb):
        if len(nrlab_nrpb.split("_")) != 2:
            raise ValueError("Numar problema invalid")
    def validare_descriere(self,descriere):
        if len(descriere)>50:
            raise ValueError("Descriere invalida")
    def validare_deadline(self,deadline):
        if deadline < 1 or deadline > 31:
            raise ValueError("Deadline invalid")
    def validare(self,pb):
        self.validare_nrlab_nrpb(pb.get_nrlab_nrpb())
        self.validare_deadline(pb.get_deadline())
        self.validare_descriere(pb.get_descriere())

    def validare_adaugare(self, nr):
        index = self.__repo.find_index(nr)
        if index != -1:
            raise ValueError("Problema este inregistrata deja")

    def validare_modificare(self, nr):
        index = self.__repo.find_index(nr)
        if index == -1:
            raise ValueError("Nu exista problema cu acest numar")

    def validare_cautare(self, nr):
        self.validare_nrlab_nrpb(nr)
        index = self.__repo.find_index(nr)
        if index == -1:
            raise ValueError("Problema nu exista")