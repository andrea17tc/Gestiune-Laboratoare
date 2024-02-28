from repository.repo_student import StudentFileRepo


def test_save_from_file():
    repo = StudentFileRepo('data/teste/input_student.txt')
    studenti = repo.get_all()
    assert(len(studenti) == 5)
    

def Test_File_Repo_Student():
    test_save_from_file()
