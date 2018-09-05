from scripts.sendgrid import send_sd_email
def reminder(to_email):
     subject = "Tasks for ACE Selections 2018 are now live!"
     from_email = "vips.ace@gmail.com"
     email_content = {
                 'type': 'text/plain',
                 'content': '''
Hey there!
We really appreciate your interest in ACE and would like to inform you that the tasks for ACE Selections 2018 are now live!
Visit https://vipsace.org/portal to view all the tasks. Please submit the tasks before the submission deadline as mentioned on the website.
All the best!

With Love,
Team ACE
 '''
             }
     try:
         send_sd_email('', from_email, to_email, subject, email_content)

     except Exception as ex:
         print(str(ex))