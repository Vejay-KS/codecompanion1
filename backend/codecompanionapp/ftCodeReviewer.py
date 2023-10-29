from django import forms
from codecompanionapp import BaseLLM

class CodeReviewerForm(forms.Form, BaseLLM.BaseLLM1):
    
    input_code = forms.CharField(widget=forms.Textarea(), required=True)
    base_fields = [input_code]
    
    def create_message_CodeReviewer(self, input_code):
        message = "Review this code and give suggestions if any, based on better coding principles. \n" + input_code
        return message
    
    def generate_chat_completion(self, input_message, max_tokens=100):

        headers = CodeReviewerForm._get_headers(self)
        message = CodeReviewerForm.create_message_CodeReviewer(self, input_message)
        data = CodeReviewerForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = CodeReviewerForm._get_response(self, headers, data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")