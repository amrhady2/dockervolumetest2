import requests

def send_sms(message):
    service_plan_id = "dd72595c5b61402f8044c6875a21a47d"
    url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"

    payload = {
      "from": "+12066578183",
      "to": [
        "+14752369160" , "+16035685274"
      ],
      "body": message
    }

    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer 5977208d4b744f9e859fcfc8188ffdf3"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    print(data)
    
    #"+14752369160", "+16035685274", "+16034937425"