from controller.ui import Console
from domain.validare.validare_notare import ValidatorNotare
from domain.validare.validare_problema import ValidatorProblema
from domain.validare.validare_student import ValidatorStudent
from repository.repo_notare import NotareRepo, NotareFileRepo
from repository.repo_problema import ProblemaRepo, ProblemaFileRepo
from repository.repo_student import StudentRepo, StudentFileRepo
from service.service_notare import NotareService
from service.service_problema import ProblemaService
from service.service_student import StudentService
from teste.all_tests import Test_All

Test_All()

repo_stud = StudentFileRepo('data/studenti.txt')
val_stud = ValidatorStudent(repo_stud)
srv_student = StudentService(repo_stud, val_stud)

repo_pb = ProblemaFileRepo('data/probleme.txt')
val_pb = ValidatorProblema(repo_pb)
srv_pb = ProblemaService(repo_pb, val_pb)

repo_not = NotareFileRepo('data/otuput.txt', 'data/output.txt')
val_not = ValidatorNotare(repo_not, repo_stud, repo_pb)
srv_not = NotareService(repo_not, val_not, repo_stud, repo_pb)

ui = Console(srv_student, srv_pb, srv_not)
ui.run()