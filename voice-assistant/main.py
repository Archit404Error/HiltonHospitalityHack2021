from speech_text_methods import *
import requests
import json

class IntentRecognizer:
    def __init__(self, text):
        self.text = text
        self.headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Authorization": "Bearer ya29.a0ARrdaM8EQ1uADEdULXgvII5S6AwEjzEAWTENYs0Go0pncmgkuSTizjm1bFKU_yYumSbxmh7SXnUrWtmAF9wCv_PXibRvv_5P986JsB9NJ_x9YCw6zNfIR3l4FyJLOvyddxRkx0WmTYf57k4Eb9bQ9u3C3i2lqNHNywsAXhlK7PVnC4ycqiQjXEsQ8Ild-yHGpqAOPs5sIOZTeKbl5PQaSbjJCyAzvyx3BJdYH_jqxiKWtq0"
         }
        self.data = {
            "queryInput":{
                    "text":{
                        "text":
                            f"{self.text}",
                            "languageCode":"en"
                            }
                },"queryParams":{
                        "source":"DIALOGFLOW_CONSOLE",
                        "timeZone":"America/New_York",
                        "sentimentAnalysisRequestConfig":{
                            "analyzeQueryTextSentiment":True
                            }
                        }
                }
        self.url = "https://dialogflow.googleapis.com/v2/projects/megaagent-borp/agent/sessions/92ab73d7-dd71-9347-f491-5b4260961214:detectIntent"

    def call_model(self):
        res = requests.post(
            url=self.url,
            data = json.dumps(self.data),
            headers=self.headers
        )
        return json.loads(res.text)

    def parse_output(self):
        res = self.call_model()
        print(res)

    def exec(self):
        self.parse_output()

while True:
    print("Listening for input go ahead...")
    IR = IntentRecognizer(listen())
    IR.exec()
