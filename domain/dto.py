class StudentProblemaNotare:
    def __init__(self, studentID, nrlab_nrpb, nota):
        self.__studentID = studentID
        self.__nrlab_nrpb = nrlab_nrpb
        self.__nume_student = None
        self.__nota = nota

    def get_studentID(self):
        return self.__studentID

    def get_nrlab_nrpb(self):
        return self.__nrlab_nrpb

    def get_nume_student(self):
        return self.__nume_student

    def get_descriere_problema(self):
        return self.__descriere_problema

    def get_nota(self):
        return self.__nota

    def set_nume_student(self, value):
        self.__nume_student = value

    def set_descriere_problema(self, value):
        self.__descriere_problema = value

    def set_nota(self, value):
        self.__nota = value

    def __str__(self):
        return str(self.__studentID) + '.' + str(self.__nume_student) + '; Nota: ' + str(self.__nota)
