from controller.generate import generate_studenti, generate_probleme


class Console:
    def __init__(self, srv_student, srv_problema, srv_notare):
        self.__srv_student = srv_student
        self.__srv_problema = srv_problema
        self.__srv_notare = srv_notare

    def __adauga_student(self):
        ID = int(input("ID-ul studentului:"))
        nume = input("Numele studentului:")
        grupa = int(input("Grupa studentului:"))
        try:
            stud = self.__srv_student.adauga_student(ID, nume, grupa)
            print('Studentul ' + str(stud.get_studentID()) + '. ' + str(stud.get_nume()) + ' (' + str(
                stud.get_grupa()) + ') a fost adaugat cu succes.')
        except ValueError as ve:
            print(str(ve))

    def __adauga_problema(self):
        nrlab_nrpb = input("Numarul problemei")
        descriere = input("Descrierea problemei")
        deadline = int(input("Deadline"))
        try:
            pb = self.__srv_problema.adauga_problema(nrlab_nrpb, descriere, deadline)
            print('Problema ' + pb.get_nrlab_nrpb() + pb.get_descriere() + ' (' + str(
                pb.get_deadline()) + ') a fost adaugata cu succes.')
        except ValueError as ve:
            print(str(ve))

    def __print_toti_studentii(self):
        lista_studenti = self.__srv_student.get_all()
        if len(lista_studenti) == 0:
            print('Nu exista studenti in lista.')
        else:
            print('Lista de studenti este:')
            for stud in lista_studenti:
                print(stud)

    def __print_toate_problemele(self):
        lista_probleme = self.__srv_problema.get_all()
        if len(lista_probleme) == 0:
            print('Nu exista probleme in lista.')
        else:
            print('Lista de probleme este:')
            for pb in lista_probleme:
                print(pb)

    def __sterge_student(self):
        id = int(input('Identificatorul studentului de sters:'))
        try:
            deleted_stud = self.__srv_student.delete_by_id(id)
            deleted_notari = self.__srv_notare.sterge_student_si_notari(id)
            print('Succes')
        except ValueError as ve:
            print(str(ve))

    def __sterge_problema(self):
        nrlab_nrpb = input('Numarul problemei de sters:')
        try:
            deleted_pb = self.__srv_problema.delete_by_nr(nrlab_nrpb)
            deleted_notare = self.__srv_notare.sterge_problema_si_notari(nrlab_nrpb)
            print('Succes')
        except ValueError as ve:
            print(str(ve))

    def __modifica_student(self):
        id = int(input('Identificator student:'))
        nume = input("Nume student:")
        grupa = int(input("Numarul grupei:"))
        try:
            modified_stud = self.__srv_student.modifica_student(id, nume, grupa)
            print('Studentul ' + str(modified_stud.get_studentID()) + '. ' + str(modified_stud.get_nume()) + ' (' + str(
                modified_stud.get_grupa()) + ') a fost modificat cu succes in Studentul ' + str(id) +
                  '.' + nume + '(' + str(grupa) + ')')
        except ValueError as ve:
            print(str(ve))

    def __modifica_problema(self):
        nrlab_nrpb = input('Numar problema:')
        descriere = input("Descriere problema:")
        deadline = int(input("Deadline:"))
        try:
            modified_pb= self.__srv_problema.modifica_problema(nrlab_nrpb, descriere, deadline)
            print('Problema ' + modified_pb.get_nrlab_nrpb() + modified_pb.get_descriere() + ' ('  + str(modified_pb.get_deadline()) +
                  ') a fost modificata cu succes in Problema '  + nrlab_nrpb + descriere + '('+ str(deadline)+')')
        except ValueError as ve:
            print(str(ve))

    def generate_studenti(self,x):
        generate_studenti(x,self.__srv_student)

    def generate_probleme(self,x,):
        generate_probleme(x,self.__srv_problema)

    def cauta_student(self):
        id = int(input('Identificatorul studentului cautat:'))
        try:
            found_stud = self.__srv_student.cauta_student(id)
            print('Studentul ' + str(found_stud.get_studentID()) + '. ' + str(found_stud.get_nume()) + ' (' + str(
                found_stud.get_grupa()) + ') este studentul cautat')
        except ValueError as ve:
            print(str(ve))

    def cauta_problema(self):
        nrlab_nrpb = input('Numarul problemei cautate:')
        try:
            found_pb = self.__srv_problema.cauta_problema(nrlab_nrpb)
            print('Problema ' + found_pb.get_nrlab_nrpb() + found_pb.get_descriere() + ' (' + str(
                found_pb.get_deadline()) +
                  ') este problema cautata')
        except ValueError as ve:
            print(str(ve))

    def notare_student(self):
        studentID = int(input('ID-ul studentului:'))
        nrlab_nrpb = input('Numar problema:')
        nota = float(input('Nota:'))
        try:
            notare = self.__srv_notare.notare_student(studentID, nrlab_nrpb, nota)
            print('Studentul ' + str(notare.get_studentID()) +' a fost notat pe problema ' + notare.get_nrlab_nrpb() +
                  ' cu nota '  + str(notare.get_nota()) )
        except ValueError as ve:
            print(str(ve))

    def __print_toate_notarile(self):
        lista_notari = self.__srv_notare.get_all()
        if len(lista_notari) == 0:
            print('Nu exista notari in lista.')
        else:
            print('Lista de notari este:')
            for notare in lista_notari:
                print(notare)

    def __notari_ordonate_problema(self):
        nrlab_nrpb = input("Numar problema: ")
        try:
            notari = self.__srv_notare.notari_ordonate_problema(nrlab_nrpb)
            if len(notari) == 0:
                print('Nu exista notari pentru problema ' + nrlab_nrpb)
            else:
                print('Lista de notari pentru problema ' + nrlab_nrpb)
                for notare in notari:
                    print(notare)
        except ValueError as ve:
            print(str(ve))

    def studenti_medie_sub_5(self):
        try:
            lista_studenti = self.__srv_notare.studenti_medie_sub_5()
            if len(lista_studenti) == 0:
                print('Nu exista studenti cu media sub 5')
            else:
                print('Lista de studenti este:')
                for stud in lista_studenti:
                    print(stud[0] + ', media: ' + str(stud[1]))
        except ValueError as ve:
            print(str(ve))

    def studenti_medie_peste_7(self):
        try:
            lista_studenti = self.__srv_notare.studenti_medie_peste_7()
            if len(lista_studenti) == 0:
                print('Nu exista studenti cu media peste 7')
            else:
                print('Lista de studenti este:')
                for stud in lista_studenti:
                    print(stud[0] + ', media: ' + str(stud[1]))
        except ValueError as ve:
            print(str(ve))

    def run(self):
        print("1.Adauga student")
        print("2.Adauga problema de laborator")
        print("3.Afiseaza studentii")
        print("4.Afiseaza problemele")
        print("5.Sterge student")
        print("6.Sterge problema")
        print("7.Modifica student")
        print("8.Modifica problema")
        print("9.Genereaza studenti si probleme")
        print("10.Cauta student")
        print("11.Cauta problema")
        print("12.Noteaza student")
        print("13.Afiseaza notari")
        print("14.Afiseaza notari pentru o problema data, ordonate")
        print("15.Afiseaza studentii cu media sub 5")
        print("16.*Afiseaza studenti cu media peste 7")
        while True:
            opt = input("Optiunea este: ")
            if opt == '1':
                self.__adauga_student()
            elif opt == '2':
                self.__adauga_problema()
            elif opt == '3':
                self.__print_toti_studentii()
            elif opt == '4':
                self.__print_toate_problemele()
            elif opt == '5':
                self.__sterge_student()
            elif opt == '6':
                self.__sterge_problema()
            elif opt == '7':
                self.__modifica_student()
            elif opt == '8':
                self.__modifica_problema()
            elif opt == '9':
                x = int(input('Introdu numarul de studenti si probleme generate:'))
                self.generate_studenti(x)
                self.generate_probleme(x)
            elif opt == '10':
                self.cauta_student()
            elif opt == '11':
                self.cauta_problema()
            elif opt == '12':
                self.notare_student()
            elif opt == '13':
                self.__print_toate_notarile()
            elif opt == '14':
                self.__notari_ordonate_problema()
            elif opt == '15':
                self.studenti_medie_sub_5()
            elif opt == '16':
                self.studenti_medie_peste_7()
            else:
                break
