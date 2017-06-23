####################################
# 	@codeauthor: Abhishek M
# 	Reach out to me @github/warlock1437
# 	Email me at nateriver210@gmail.com
####################################

from subprocess import call

print '\nSENTO by Abhishek(@warlock1437)\n\nOnce dependencies are installed, you can run the code by typing \'python mainPY.pyc\'\n\n[+] Verifying and installing dependencies\n'
try:
	import tweepy
except ImportError:
	print '[!] Tweepy not found, installing tweepy via pip'
	call(['pip','install','tweepy'])
try:
	import textblob
except ImportError:
	print '[!] TextBlob not found, installing textblob via pip'
	call(['pip','install','textblob'])

print '[+] All dependencies and data corpus successfully injected'

while True:
	choice = raw_input('Start program? (y or n)').lower()[0]
	if choice=='y':
		call(['python','mainPY.pyc'])
		break
	elif choice=='n':
		exit()
