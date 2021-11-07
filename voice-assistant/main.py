from speech_text_methods import *
import requests
import json

class IntentRecognizer:
    def __init__(self, text):
        self.text = text
        self.headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Authorization": "Bearer ya29.a0ARrdaM8mgchwFOTyHsjUiYZ3Zh2dWY7J0G61yJcJZVnm2uSm3kuBw_gn5hpo5OBv8Lz9VGLP-8awN4eN7F5LYRFv57eO1XreLUXVcSKLEpFSo6Bq8QaB08u-rb4HXSobboWPS4EtM1Wr31T4NkX-bROiZLWEiQLxk7l2J0ymcEu4KcqhYSACDtVX74hLDHh7wQNYKMh5g5LlNa1xmhL3y6UVjVoGxX-4Uf93lCjwpHxcOtU"
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
        if self.text != "Sorry, I didn\'t understand":
            speak("Hang on one second")
        else:
            speak("Sorry, I couldn\'t understand")
            return
        res = self.call_model()
        print(res)
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
