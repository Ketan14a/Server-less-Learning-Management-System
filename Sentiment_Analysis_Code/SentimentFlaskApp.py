import boto3
from flask import Flask 
from flask import render_template
from flask import url_for, flash, redirect

app = Flask(__name__)

def getSentimentData():
	ACCESS_KEY = 'ASIAXPZJUBM2M2BGDDOM'
	SECRET_KEY = 'LZd4uHC223NrZh5MzGQj0+VFSjg314ynja4lf/AR'
	SESSION_TOKEN = 'FwoGZXIvYXdzEMv//////////wEaDHIgvIaV6ysJ1K/XCSLEASp+qBApzZlw7C3PVoOqBmTEI/JMuYqrtnkP2BFiVs6w9b6MtdadJOPWGnu6b6Bh3uIWsJrnqKQfvLGQVyP/cNwPuw+lluH9F7In76pjVnMxYkHVOtsJKg50elIoAqahQAzBBt3JThk98fvFOh+K+tfyY48MIazk3fMBN2vWGmh/RMEkmpUdlXNCFSQfeLmq0oH6cCf85Y4mHagXASAaeso7MGFzuX5IdSHL0CqxKYczZyrSUwGBNkuAmnFbfX7gf+GQqfsovdSd+QUyLaoU2dNJqUTgduLase3qVZg4+1BTewQWxIBRqOK+rDbdmlSvtOBTUIYeelW8aw=='
	
	s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,region_name='us-east-1',aws_session_token=SESSION_TOKEN)
	bucket = s3.Bucket('sentiments-storage')


	L = []
	for obj in bucket.objects.all():
		body = obj.get()['Body'].read().decode('utf-8')
		temp = []
		s = body.split("\n")
		for i in s:
			temp.append(i)

		L.append(temp)


	return L

@app.route("/")
def home():
	Sentiments = getSentimentData()
	return render_template('home.html', myPosts=Sentiments)



if __name__ == '__main__':
	app.run(port=9091,debug=True)