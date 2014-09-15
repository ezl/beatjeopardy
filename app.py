from flask import Flask, request
from twilio.rest import TwilioRestClient

client = TwilioRestClient()
my_twilio_number = "+19032006644"

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    output = "Hello World"
    data = request.form
    """
    Sample data
    ImmutableMultiDict([('FromZip', u'77386'),
                        ('From', u'+18322646644'),
                        ('SmsMessageSid', u'SM30517e517a740ca551c3116db5d7b992'),
                        ('FromCity', u'HOUSTON'),
                        ('ApiVersion', u'2010-04-01'), 
                        ('To', u'+19032006644'),
                        ('NumMedia', u'0'),
                        ('AccountSid', u'AC8fc3a46010b77b1d28a38d82d35584c1'),
                        ('SmsSid', u'SM30517e517a740ca551c3116db5d7b992'),
                        ('ToCity', u'COLLINSVILLE'), ('FromState', u'TX'),
                        ('FromCountry', u'US'), ('Body', u'Good'),
                        ('MessageSid', u'SM30517e517a740ca551c3116db5d7b992'), ('SmsStatus', u'received'),
                        ('ToZip', u'76233'),
                        ('ToCountry', u'US'), ('ToState', u'TX')])
    """
    body = data.get("Body")
    original_sender = data.get("From")
    message = client.messages.create(
        to=original_sender,
        from_=my_twilio_number,
        body=body)
    return "foo"

if __name__ == "__main__":
    app.run(host='0.0.0.0',)
