from files_processing.PathProvider import get_path
from files_processing.UsersProcessor import read_users
from files_processing.BooksProcessor import read_books
from files_processing.File import File

PATH_BOOKS = get_path("books.csv")
PATH_USERS = get_path("users.json")



class FileMerger:
    def __init__(self):
        self.file_users = File(PATH_USERS)
        self.file_books = open(PATH_BOOKS, newline='')
        # self.file_result = File(PATH_RESULT)

    def get_users(self):
        return read_users(self.file_users)

    def get_books(self):
        return read_books(self.file_books)

    def end_work(self):
        self.file_users.close_file()
        self.file_books.close()
        # self.file_result.close()
