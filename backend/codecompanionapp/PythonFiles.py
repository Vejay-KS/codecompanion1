from codecompanionapp.FilesHandler import FileHandler

class PythonFile(FileHandler):

    __file_type = ".py"

    def get_file_type():
        return PythonFile.__file_type