from speech_text_methods import *
import requests
import json

class IntentRecognizer:
    def __init__(self, text):
        self.text = text
        self.headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Authorization": "Bearer ya29.a0ARrdaM9SvzmaP9v4dNWj9Lsuoomiu9THe3C_2Sn2pq4h_CbRtQBXwyajPZHqBCa_0WIP40qCn1r8Kiz0ebekHCMSxTs7bIoUgvTQousZ8srexTGf0UlETLYKjl6oACwsZbp5KgF_gzeCiRALwO1We422BeG-Gxa5pqYD-5Dn_F3s1As5LzSzazuG2ONthUywPlfAfvRYIgYBLMH_ee2n6yf980oofH6JLtsLIArDNIMiK-o"
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
        self.url = "https://dialogflow.googleapis.com/v2/projects/dining-out-njcy/agent/sessions/1b48378b-2560-23cb-8a3c-1508fa232bf2:detectIntent"

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
        classification = res["queryResult"]["action"]
        if classification == "venues.eating_out.search":
            speak("Here are some restaurants close to you")

    def exec(self):
        self.parse_output()

while True:
    print("Listening for input go ahead...")
    IR = IntentRecognizer(listen())
    IR.exec()
