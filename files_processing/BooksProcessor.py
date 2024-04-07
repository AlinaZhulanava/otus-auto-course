import csv


def read_books(file_books):
    books = []
    reader = csv.reader(file_books)
    header = next(reader)
    for row in reader:
        full_book_dict = dict(zip(header, row))
        useful_book_dict = {"title": full_book_dict["Title"],
                            "author": full_book_dict["Author"],
                            "pages": full_book_dict["Pages"],
                            "genre": full_book_dict["Genre"]}
        books.append(useful_book_dict)
    return books
