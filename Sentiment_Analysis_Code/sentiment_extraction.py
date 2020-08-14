import boto3
import json
import ast 

ACCESS_KEY = 'ASIAXPZJUBM2GO7LRAHK'
SECRET_KEY = 'sY5Kn8CO88jxCMHrkLWOqv2xAG8UCUXAR3GhcsTM'
SESSION_TOKEN = 'FwoGZXIvYXdzEAQaDPYv/r4WaJzK0n9HJCLEAc4BuQB3ROL0Wbb9gTl95TYdCFx6GbLSDT68igD9Hk6EM7WxlLby8syqlMgD/Zbt8ikUTFGDYZ5BcRTYBS/gqBfejn+qRUAvKL0b1aZEl7niPJ8OI4+1eqjD4YniX9bB9ndFfPEDrwSokezTLbbSAl0MxKDJqdJ2L3JoTDSCAofLLI41zqkXr8oyRmeknGjzE3sYw0rK4Tbzw267ZdjkfYopB+SLVW81/hTeKXGE3GbW6+qvODWKlGl5EfTZhyfnrsIfyHEo4/3x+AUyLbkGgP54/XjctCrkAR3rgIYGLmmt8YJKSROym6lM0stIyuaS1PZ8d/QWNnkJAQ=='

comprehend_client = boto3.client('comprehend', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY, region_name='us-east-1',aws_session_token=SESSION_TOKEN)


for j in range(13):
	path = "./Chats/"+str(j)+".txt"
	F = open(path,"r")
	data = F.read()
	data = data.split("\n")
	F.close()
	Sentiments = {}
	i=0
	L = []
	temp = {}
	for line in data:

		sentiments=json.dumps(comprehend_client.detect_sentiment(Text=line,LanguageCode='en'), sort_keys=True, indent=4)
		sentiments = json.loads(sentiments)
		Sentiment = sentiments["Sentiment"]
		temp[line] = Sentiment


	path = "./Sentiments/"+str(j)+"_sentiments.txt"
	F = open(path,"w")

	for line in temp:
		F.write(line + ":"+temp[line]+"\n")


	F.close()








	






