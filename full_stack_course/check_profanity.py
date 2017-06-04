import urllib
def read_text():

	quotes = open("/home/ubuntu/myrepo/full_stack_course/movies_sample.txt")
	contents  = quotes.read()
	#print (contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(input_text):

	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+input_text)
	output = connection.read()
	print(output)
	connection.close()

	if "true" in output:
		print ("Hay palabrotas")
	else: print("El texto es limpio")

read_text()
