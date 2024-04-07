import csv


def read_books(file_books):
    books = []
    reader = csv.reader(file_books)
    header = next(reader)
    for row in reader:
        books.append(dict(zip(header, row)))
    return books
