import urllib3
import json

http = urllib3.PoolManager()


def lambda_handler(event, context):
    url = ""  #we can either hardcode or take it from env or anywhere it is required
    MessageObj = json.loads(event["Records"][0]["Sns"]["Message"])
    # print(type(MessageObj))
    # print(MessageObj)

    msg = {
        "Alarm Name" : MessageObj["AlarmName"],   #this payload is for a custom webhook , feel free to change it for your needs
        "Alarm Description" : MessageObj["AlarmDescription"],
        "Time" : MessageObj["StateChangeTime"],
        "Notification Reason" : MessageObj["NewStateReason"]
    }
    headers = {'Content-Type': 'application/json'}
    
    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg, headers = headers)
    print(resp)
    print(
        {
            "message": event["Records"][0],
            "status_code": resp.status,
            "response": resp.data,
        }
    )