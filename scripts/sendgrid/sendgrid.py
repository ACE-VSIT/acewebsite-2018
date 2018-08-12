import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
import urllib.request as urllib
from ace.settings import SENDGRID_API_KEY


def send_sd_email(name, fromemail, toemail, subject, email_content):
    print(name, fromemail, toemail, subject, email_content)
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(fromemail)
    to_email = Email(toemail)
    content = Content(email_content['type'], email_content['content'])
    mail = Mail(from_email, subject, to_email, content)
    # mail.personalizations[0].add_substitution(Substitution("-name-", name))
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except urllib.HTTPError as e:
        print(e.read())
        exit()
    return response.status_code