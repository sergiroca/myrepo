import twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC45b086d199eacad131475cbdff89f556"
# Your Auth Token from twilio.com/console
auth_token  = "90a411c563d82bb65d7fb1fc38e01eb1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+34663091516", 
    from_="+34932204270",
    body="Hola Teresa")

print(message.sid)
