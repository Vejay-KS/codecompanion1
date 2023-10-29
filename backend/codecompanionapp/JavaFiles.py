from codecompanionapp.FilesHandler import FileHandler


class JavaFile(FileHandler):

    __file_type = ".java"

    def get_file_type():
        return JavaFile.__file_type