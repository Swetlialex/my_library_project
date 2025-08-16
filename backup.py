import shutil


# Архив на библиотеката
def backup_library():
    shutil.copy("./data/library.json", "./data/library_backup.json")
