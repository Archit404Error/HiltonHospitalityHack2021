from speech_text_methods import *
import requests
import json

class IntentRecognizer:
    def __init__(self, text):
        self.text = text
        self.headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Authorization": "Bearer ya29.a0ARrdaM9SbrM0tlcLeYpm1WcU2UYK2HHCKM3ZrAk6l8MCQMjrYRW0H6pFQ2k8A2nLwMEWHhdw5whQLca_Qn7wKDCp2VtbIZ6QwPR67ltd0LiROZvNZheCUBOo6uMrnP7S6jUSLh-VaXh9fmlFKC9atIi9oah4hosdB7dhHMvzkWqIPWzyqMeqO64MHI_cUEv1ABV0D5IKiMXCphnHhSMQbQqyaH0AcrUPnhYVh_l_UYHCSro"
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
        self.url = "https://dialogflow.googleapis.com/v2/projects/ava-wtvw/agent/sessions/842b397f-f75c-e156-4ba0-03dcfcb8d49d:detectIntent"

    def call_model(self):
        res = requests.post(
            url=self.url,
            data = json.dumps(self.data),
            headers=self.headers
        )
        return json.loads(res.text)

    def parse_output(self):
        speak("Hang on one second")
        res = self.call_model()
        try:
            classification = res["queryResult"]["action"]
            if classification == "venues.eating_out.search":
                speak("Here are some restaurants close to you")
        except:
            speak("Sorry, I couldn\'t understand")
            print(res)

    def exec(self):
        self.parse_output()

while True:
    print("Listening for input go ahead...")
    IR = IntentRecognizer(listen())
    IR.exec()
