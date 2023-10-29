from django import forms
from codecompanionapp import BaseLLM, FilesHandler

class ResumeFiltererForm(forms.Form, BaseLLM.BaseLLM1):
    __INPUT_FILE_HELP_TEXT = 'maximum 5MB'

    input_file1 = forms.FileField(
        label='Upload File 1',
        help_text=__INPUT_FILE_HELP_TEXT
    )
    input_file2 = forms.FileField(
        label='Upload File 2',
        help_text=__INPUT_FILE_HELP_TEXT
    )
    input_file3 = forms.FileField(
        label='Upload File 3',
        help_text=__INPUT_FILE_HELP_TEXT,
        required=False
    )
    input_job_role = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_job_role, input_file1, input_file2]
    
    def __create_message_ResumeFilterer(self, input_file, input_data):
        message = "Filter and Select one resume from the given below 3 resumes for the role of" +  input_data + ". The resumes are separated by \"=====\". \n" + input_file
        return message
    
    def generate_chat_completion(self, input_file, input_message, max_tokens=100):
        if type(input_file) == type(""):
            file_lines = len(input_file)
        else:
            file_lines = FilesHandler.FileHandler.number_of_lines(input_file)
        if(file_lines > 10):
            if type(input_file) == type(""):
                file_data = input_file
            else:
                file_data = FilesHandler.FileHandler.read_file(input_file)
            headers = ResumeFiltererForm._get_headers(self)
            message = ResumeFiltererForm.__create_message_ResumeFilterer(self, file_data, input_message)
            data = ResumeFiltererForm._get_data(self, messages=message)

            if max_tokens is not None:
                data["max_tokens"] = max_tokens

            response = ResumeFiltererForm._get_response(self, headers, data)
        else:
            file_data = "NO DATA"
            response = file_data
            return response
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")