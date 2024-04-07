from files_processing.PathProvider import get_path
from files_processing.UsersProcessor import read_users, write_users
from files_processing.BooksProcessor import read_books

PATH_BOOKS = get_path("books.csv")
PATH_USERS = get_path("users.json")
PATH_RESULT = get_path("result.json")


class FileMerger:
    def __init__(self):
        pass

    def give_books_to_users(self):
        with open(PATH_USERS, "r") as f:
            self.users_list = read_users(f)

        with open(PATH_BOOKS, newline='') as f:
            self.books_list = read_books(f)

        self.books_list.reverse()

        give_iterations = len(self.books_list) / len(self.users_list)
        while (give_iterations > 0):
            for user in self.users_list:
                if self.books_list:
                    user["books"].append(self.books_list.pop())
            give_iterations = give_iterations - 1

    def return_merged_files(self):
        with open(PATH_RESULT, "a") as f:
            write_users(f, self.users_list)
