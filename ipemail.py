from urllib.request import urlopen
import re
import smtplib

#setup our login credentials
from_address = '<email>@gmail.com'
to_address = '<email>@gmail.com'
subject = 'Mine@Craft'
username = '<user>'
password = '<passwd>'

#Setup where we will get our IP address
url = 'http://checkip.dyndns.org'
print ("The chosen IP address service is: ", url)

#Open up the url, then read the contents, and tak>
request = urlopen(url).read().decode('utf-8')
#We extract the IP address only
ourIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
ourIP = str(ourIP)
print ("Mine@Craft IP address is: ", ourIP)

def send_email(ourIP):
	# Body of the email
	body_text = ourIP + ' is the Mine@Craft IP address'
	msg = '\r\n'.join(['To: %s' % to_address,
			   'From: %s' % from_address,
			   'Subject: %s' % subject,
			   '', body_text])
	#Actually send the email!
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls() # Our security for transmission of credentials
	server.login(username,password)
	server.sendmail(from_address, to_address, msg)
	server.quit()
	print ("The email has been sent!")

# Open Up last_ip.txt, and extract the contents
with open('/home/mine/ipemail/last_ip.txt', 'rt') as last_ip:
	last_ip = last_ip.read() # Read the text file

# Check to if our IP address has really changed
if last_ip == ourIP:
	print ("Mine@Craft IP address have not changed.")
else:
	print ("Mine@Craft has a new IP address.")
	with open('/home/mine/ipemail/last_ip.txt', 'wt') as last_ip:
		last_ip.write(ourIP)
	print ("Updating the new IP address to the text file.")
	send_email(ourIP)
