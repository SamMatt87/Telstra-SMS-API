import requests
import json

def sendSMS():
    print ("Please enter your Consumer key:")
    CONSUMER_KEY = input()
    print ("Please enter your consumer secret:")
    CONSUMER_SECRET = input()
    another_one = "y"
    while another_one != "n":
        print ("Enter the recipients number:")
        contact = input()
        print ("Enter your message:")
        message = input()

        URL = 'https://beta-sapi.telstra.com/v1/oauth/token'
        data = 'client_id='+CONSUMER_KEY+'&client_secret='+CONSUMER_SECRET+'&grant_type=client_credentials&scope=NSMS'
        response = requests.post(URL,data=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
        print(response)
        print(response.text)
        authResp = json.loads(response.text)
        smsURL='https://beta-sapi.telstra.com/v2/messages/sms'
        #sms = "{\"to\":\""+contact+"\", \"body\":\""+message+"\"}"
        sms2 = {"to":contact,"from":"0400000000","body":message}
        response = requests.post(smsURL,data=json.dumps(sms2).encode('utf-8'),headers={'Content-Type':'application/json','Authorization': 'Bearer '+authResp["access_token"]})
        print(response.text)
        print ("Would you like to send another? y/n:")
        another_one = input().lower()
sendSMS()