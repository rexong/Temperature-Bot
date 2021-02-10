from twilio.rest import Client

account_sid = 'AC35b8f3f1e62fab6f34050b6423eebcfd'
auth_token = '03eb52e8fefa9e80704500baf30a591b'
client = Client(account_sid, auth_token)


def send_message(text):
    client.messages.create(from_='whatsapp:+14155238886',
                           body=text,
                           to='whatsapp:+6586994184')
