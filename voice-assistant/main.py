import requests
import json
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer ya29.a0ARrdaM-TzuYLuEdDgDZ-hpW8XotgmtMn3wTYEsdawxUYMd4TLNHRyxaLzP6zAtZ5ffvNXdyVA6Nx_GcNcxgraJpSpGKqQTv6bUUBXJJl_LqO_pQKwXw5xgp7Z9dCMecSrRU-ZjgLFGtcmTE0zd3YMq_FMeZJ_RNBRev9fazHSXr4E6A_b5hPHvBYLJ8IW1QhzrG82ul5063LhI3s7Lw_SdgRyNC7cK1tolgGpPX3SyEIBw"
}
data = {
    "queryInput":{
            "text":{
                "text":
                    "where can i get a haircut?",
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

url = "https://dialogflow.googleapis.com/v2/projects/megaagent-borp/agent/sessions/92ab73d7-dd71-9347-f491-5b4260961214:detectIntent"
x = requests.post(url, data = json.dumps(data), headers=headers)
print(x.text)
