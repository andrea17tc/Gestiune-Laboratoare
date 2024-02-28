from teste.teste_domain.test_domain import Test_Domain
from teste.teste_file_repo.test_file_repo import Test_File_Repo
from teste.teste_repo.test_repo import Test_Repo
from teste.teste_service.test_service import Test_Service


def Test_All():
    Test_Domain()
    Test_Repo()
    Test_Service()
    Test_File_Repo()