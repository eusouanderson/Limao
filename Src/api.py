import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ"ACbbafaef13a9f3d2eb06a20b2e96c7c15"
auth_token = os.environ['5511954914441']
client = Client(account_sid, auth_token)

message = client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch()

print(message.body)