from django import forms
from codecompanionapp import BaseLLM

class TechnicalTrendsForm(forms.Form, BaseLLM.BaseLLM1):
    
    input_domain = forms.CharField(widget=forms.Textarea(), required=True)
    base_fields = [input_domain]
    
    def create_message_TechnicalTrends(self, input_domain):
        message = "What are the current and future trends of " + input_domain + " ? \n"
        return message
    
    def generate_chat_completion(self, input_message, max_tokens=100):

        headers = TechnicalTrendsForm._get_headers(self)
        message = TechnicalTrendsForm.create_message_TechnicalTrends(self, input_message)
        data = TechnicalTrendsForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = TechnicalTrendsForm._get_response(self, headers, data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
