from django import forms
from codecompanionapp import BaseLLM, FilesHandler

class LetterGeneratorForm(forms.Form, BaseLLM.BaseLLM1):
    
    input_name = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    input_type_of_letter = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    input_extra_details = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    input_organisation_details = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    input_designation = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_name, input_type_of_letter, input_extra_details, input_organisation_details, input_designation]
    
    def create_message_LetterGenerator(self, input_name, input_type_of_letter, input_extra_details, input_organisation_details, input_designation):
        message = "Generate a " + input_type_of_letter + " letter for " + input_name + " with " + input_extra_details + " as extra details " + " and organization's details as " + input_organisation_details + " and signed with designation as " + input_designation
        return message
    
    def generate_chat_completion(self, input_name, input_type_of_letter, input_extra_details, input_organisation_details, input_designation, max_tokens=100):

        headers = LetterGeneratorForm._get_headers(self)
        message = LetterGeneratorForm.create_message_LetterGenerator(self, input_name, input_type_of_letter, input_extra_details, input_organisation_details, input_designation)
        data = LetterGeneratorForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = LetterGeneratorForm._get_response(self, headers, data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")