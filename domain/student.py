class Student:
    '''
    Clasa Student cu atributele:
    studentID - ID-ul studentului
    type: int
    nume - numele studentului
    type:string
    grupa - grupa studentului
    type: int
    '''
    no_instances = 0

    def __init__(self, studentID, nume, grupa):
        self.__studentID = studentID
        self.__nume = nume
        self.__grupa = grupa
        Student.no_instances +=1

    def get_studentID(self):
        return self.__studentID

    def get_nume(self):
        return self.__nume

    def get_grupa(self):
        return self.__grupa

    def set_nume(self,value):
        self.__nume = value

    def set_grupa(self, value):
        self.__grupa = value

    def __eq__(self, other):
        if self.__studentID == other.get_studentID():
            return True
        return False

    def __str__(self):
        return "ID student: " + str(self.__studentID) + '; Nume: ' + str(self.__nume) + '; Nr. grupa: ' + str(
            self.__grupa)

    @staticmethod
    def getNrStudenti():
        return Student.no_instances
