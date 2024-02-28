from teste.teste_service.test_service_notare import Test_Service_Notare
from teste.teste_service.test_service_problema import Test_Service_Problema
from teste.teste_service.test_service_student import Test_Service_Student


def Test_Service():
    Test_Service_Student()
    Test_Service_Problema()
    Test_Service_Notare()