from speech_text_methods import *
import requests
import json

class IntentRecognizer:
    def __init__(self, text):
        self.text = text
        self.headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Authorization": "Bearer ya29.a0ARrdaM9ukBl9U_jVV0zcNUg9SnY_lCQu1Rmdr25R8KFNyY9T2uHSUxoHIdI6NU1n25Gq2JRdw8SUTvBir558VZthziETFhile4q2Y_A2Jzeu9zVbYgAiMoMef8bZbFmZHAgNzKVSA6G2Hy59FGZCG2AGjrfpv37M-5m5UKKkes7KdMhmBCAR-MAZRBlZAXdoIEJ0KJ1HteXp7jpJTgYMpw-nEfUptBunpcKDr190HRu8lak"
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
                        "resetContexts":"true",
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
            params = res["queryResult"]["parameters"]
            if classification == "venues.eating_out.search":
                speak("Here are some restaurants close to you")
                res = requests.get("http://localhost:5000/getRestaurants")
                restaurant_list = res.json()
                speak(", ".join(restaurant_list))
            elif classification == "events.search.implicit":
                speak("Here are some events near you")
                res = requests.get("http://localhost:5000/getActivities")
                restaurant_list = res.json()
                speak(", ".join(restaurant_list))
            elif classification == "events.tickets.book":
                speak("Booking your ticket now")
                event = params['event-type']
                try:
                    time = params["date-time"]['date_time']
                except:
                    time = params["date-time"]
                requests.get(f"http://localhost:5000/createRequest?Archit&{event}&{time}&activity&none")
                speak("Booking confirmed")
            elif classification == "delivery.product.add":
                speak("Ordering your food via room service")
            elif classification == "hotel.book":
                speak("Booking your cleaning")
                try:
                    time = params["checkin-date"]['date-time']
                except:
                    time = params["checkin-date"]
                if type(time) == list:
                    time = time[0]
                res = requests.get(f"http://localhost:5000/createRequest?Archit&cleaning&{time}&roomCleaning&none")
                print(res.text)
                speak("Cleaning has been scheduled")
            elif classification == "restaurant.book":
                speak("Booking your seat")
                restaurant = params["location"]["business-name"]
                try:
                    time = params["date-time"]["date_time"]
                except:
                    time = params["date-time"]
                res = requests.get(f"http://localhost:5000/createRequest?Archit&{restaurant}&{time}&restaurant&none")
                speak("Seat booked")
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            speak("Sorry, I couldn\'t understand")

    def exec(self):
        self.parse_output()

while True:
    print("Listening for input go ahead...")
    IR = IntentRecognizer(listen())
    IR.exec()
