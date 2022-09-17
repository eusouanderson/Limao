import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ"xxxxxxxxx"
auth_token = os.environ['xxxxxxxxx1']
client = Client(account_sid, auth_token)

message = client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch()

print(message.body)
