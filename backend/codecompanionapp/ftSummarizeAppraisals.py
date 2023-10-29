from django import forms
from codecompanionapp import BaseLLM, FilesHandler

class SummarizeAppraisalsForm(forms.Form, BaseLLM.BaseLLM1):
    
    __INPUT_FILE_HELP_TEXT = 'maximum 5MB'

    input_file = forms.FileField(
        label='Upload File 1',
        help_text=__INPUT_FILE_HELP_TEXT,
        required=False
    )
    input_appraisal = forms.CharField(widget=forms.Textarea(), required=False)
    base_fields = [input_appraisal, input_file]
    
    def create_message_SummarizeAppraisals(self, input_file, input_appraisal):
        message = "Analyse and give a 2 line summary for this appraisal. \n" + input_appraisal + input_file
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
        else:
            file_data = ""
        headers = SummarizeAppraisalsForm._get_headers(self)
        message = SummarizeAppraisalsForm.create_message_SummarizeAppraisals(self, file_data, input_message)
        data = SummarizeAppraisalsForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = SummarizeAppraisalsForm._get_response(self, headers, data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
