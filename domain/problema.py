class Problema:
    '''
    Clasa Problema cu atributele :
    nrlab_nrpb - numarul problemei dintr-un laborator
    type:string
    descriere -descrierea problemei
    type: string
    deadline - data limita
    type:int
    '''
    no_instances = 0

    def __init__(self, nrlab_nrpb, descriere, deadline):
        self.__nrlab_nrpb = nrlab_nrpb
        self.__descriere = descriere
        self.__deadline = deadline
        Problema.no_instances += 1

    def get_nrlab_nrpb(self):
        return self.__nrlab_nrpb

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_descriere(self, value):
        self.__descriere = value

    def set_deadline(self, value):
        self.__deadline = value

    def __eq__(self, other):
        if self.__nrlab_nrpb == other.get_nrlab_nrpb():
            return True
        return False

    def __str__(self):
        return "Numarul laboratorului si numarul problemei " + self.__nrlab_nrpb + \
               '; Descriere: ' + str(self.__descriere) + '; Deadline: ' + str(self.__deadline)

    @staticmethod
    def getNrProbleme():
        return Problema.no_instances
