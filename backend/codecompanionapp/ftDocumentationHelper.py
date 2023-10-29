from django import forms
from codecompanionapp import BaseLLM, FilesHandler

class DocumentationHelperForm(forms.Form, BaseLLM.BaseLLM1):

    __INPUT_FILE_HELP_TEXT = 'maximum 5MB'
    input_code = forms.CharField(widget=forms.Textarea(), required=False)

    input_file = forms.FileField(
        label='Upload File',
        help_text=__INPUT_FILE_HELP_TEXT,
        required=False
    )

    base_fields = [input_code, input_file]

    def create_message_DocumentationHelper(self, input_file, input_code):
        message = "Provide documentation (only purpose of code) for this piece of code. \n" + input_code + input_file
        return message
    
    def generate_chat_completion(self, input_file, input_document, max_tokens=100):

        print(type(input_file))
        if type(input_file) == type(""):
            file_lines = len(input_file)
        else:
            file_lines = FilesHandler.FileHandler.number_of_lines(input_file)
        print(file_lines)
        if(file_lines > 10):
            if type(input_file) == type(""):
                file_data = input_file
            else:
                file_data = FilesHandler.FileHandler.read_file(input_file)
            print(file_data)
        else:
            file_data = ""
        headers = DocumentationHelperForm._get_headers(self)
        message = DocumentationHelperForm.create_message_DocumentationHelper(self, input_file, input_document)
        data = DocumentationHelperForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = DocumentationHelperForm._get_response(self, headers, data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
