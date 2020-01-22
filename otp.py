import os
from twilio.rest import Client

account_sid="AC208fd81769b08cd5c4489033f6726d4b"
auth_token="19e4aa4bcfde166ff5317e925f4bfa81"

client=Client(account_sid,auth_token)

client.messages.create(
    to="+919872143204",
    from_="+13143264810",
    body="Testing"
)
