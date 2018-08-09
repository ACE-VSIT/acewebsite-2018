from django.core.mail import EmailMessage
import csv
import re


def send_mail(student_name, email_id):
	msg = EmailMessage('Reminder:ACE-Online Round 2017', """Hello %s,<br><br>
		
		You have registered for the ACE Selection Process on our online portal. 
		Gear up for the challenge.The problem statements are out. 
		You can access them at <a href="http://vipsace.org/portal">http://vipsace.org/portal</a> <br><br>

		Every Category of task has been divided into 3 levels : Easy, Medium and Hard.<br><br>

		General Guidelines:<br>
		
		1. There is no limit to the number of tasks you can attempt.<br>
		2. You are allowed to submit a task just once and subsequent submissions will not be recorded.<br>
		3. Plagiarism and use of unfair means to complete the task are strictly prohibited.<br>
		4. We recommend you to attempt as many tasks as you can however we believe in quality over quantity.<br>
		5. Kindly submit the URL of your code/solution before the submission deadline.<br><br>

		For any queries/doubts at any stage of the selection process, Please don't hesitate to <a href="https://www.facebook.com/vipsace">contact us</a>.<br><br>

		All the Best<br>
		Team ACE""" % (student_name), 'csi-sb-ace@vips.edu',[email_id])

	msg.content_subtype="html"
	response = msg.send()
	return response


def load_data():
	my_file = 'data.csv'
	fp = open(my_file,'r')
	data = []

	for line in fp:
		data.append(tuple(line.strip().split(',')))
	return data


data = load_data()

#data = [('SameerKumar','01629802015','BCA','sameer18051998@gmail.com'),('AshishPahwa','01629802015','BCA','ashishpahwa7@gmail.com')]
counter = 0
for record in data:
	try:
		name = re.findall('[A-Z][^A-Z]*', record[0])
		name = ' '.join(name)
		print name, record[3]
		response = send_mail(name,record[3])
		counter = counter + 1
	except:
		print name, record[3]
		print "Error"
	


print(counter)