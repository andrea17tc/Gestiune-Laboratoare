class Notare:

    def __init__(self, studentID, nrlab_nrpb, nota):
        self.__studentID = studentID
        self.__nrlab_nrpb = nrlab_nrpb
        self.__nota = nota

    def get_studentID(self):
        return self.__studentID

    def get_nrlab_nrpb(self):
        return self.__nrlab_nrpb

    def get_nota(self):
        return self.__nota

    def set_nota(self, value):
        self.__nota = value

    def __eq__(self, other):
        if self.__studentID == other.get_studentID() and self.__nrlab_nrpb == other.get_nrlab_nrpb():
            return True
        return False

    def __str__(self):
        return "ID student: " + str(self.__studentID) + '; Numar problema: ' + self.__nrlab_nrpb + '; Nota:' + str(self.__nota)
