class FileHandler():

    def number_of_lines(self, input_file):
        li = input_file.readlines()
        total_lines = len(li)
        return total_lines
        
    def read_file(input_file):
        file_data = ""
        for line in input_file:
            file_data = file_data + line.decode("utf-8")
        return file_data
    
    def read_files(list_of_files):
        file_data = ""
        for input_file in list_of_files:
            for line in input_file:
                file_data = file_data + line.decode("utf-8")
            file_data = file_data + "====="
        return file_data
    
    def get_file_type(self):
        pass