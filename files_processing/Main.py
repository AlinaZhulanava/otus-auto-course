from files_processing.FileMerger import FileMerger

file_merger = FileMerger()
print(file_merger.get_users())
print(file_merger.get_books())
file_merger.end_work()