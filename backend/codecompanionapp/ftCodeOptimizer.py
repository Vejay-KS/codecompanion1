from django import forms
from codecompanionapp import BaseLLM

class CodeOptimizerForm(forms.Form, BaseLLM.BaseLLM1):
    
    input_code = forms.CharField(widget=forms.Textarea(), required=True)
    base_fields = [input_code]
    
    def create_message_CodeOptimizer(self, input_code):
        message = "Optimize and give suggestions for this code. \n" + input_code
        return message
    
    def generate_chat_completion(self, input_message, max_tokens=100):

        headers = CodeOptimizerForm._get_headers(self)
        message = CodeOptimizerForm.create_message_CodeOptimizer(self, input_message)
        data = CodeOptimizerForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = CodeOptimizerForm._get_response(self, headers, data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
