from files_processing.PathProvider import get_path
from files_processing.UsersProcessor import read_users, write_users
from files_processing.BooksProcessor import read_books
from files_processing.File import File

PATH_BOOKS = get_path("books.csv")
PATH_USERS = get_path("users.json")
PATH_RESULT = get_path("result.json")


class FileMerger:
    def __init__(self):
        self.file_users = File(PATH_USERS)
        self.file_books = open(PATH_BOOKS, newline='')
        self.file_result = File(PATH_RESULT)

    def get_users(self):
        return read_users(self.file_users)

    def get_books(self):
        return read_books(self.file_books)

    def end_work(self):
        self.file_users.close_file()
        self.file_books.close()
        self.file_result.close_file()

    def give_books_to_users(self):
        self.users_list = self.get_users()
        self.books_list = self.get_books()

        give_iterations = len(self.books_list) / len(self.users_list)
        while (give_iterations>0):
            for user in self.users_list:
                if self.books_list:
                    user["books"].append(self.books_list.pop())
            give_iterations = give_iterations -1

    def return_merged_files(self):
        write_users(self.file_result, self.users_list)
