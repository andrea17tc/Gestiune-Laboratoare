import random
import string


def generate_studenti(x,srv1):
    random_studs = srv1
    lista_nume = ['Andrei', 'Alex', 'Mihai','Daniel', 'Mircea','Marcel','Cosmin','Ana','Maria','Corina']
    for i in range(1,x+1):
        #stud = Student(i, random.choice(lista_nume), random.randrange(210,918))
        random_studs.adauga_student(i, random.choice(lista_nume), random.randrange(210,918))


def generate_probleme(x,srv2):
    random_pbs = srv2
    for i in range(x):
        nrlab_nrpb = str(random.randrange(1,10)) + '_' + str(random.randrange(1,10))
        descriere = ''.join(random.choices(string.ascii_lowercase, k=5))
        deadline = random.randrange(1,32)
        #pb = Problema(nrlab_nrpb,descriere,deadline)
        random_pbs.adauga_problema(nrlab_nrpb,descriere,deadline)