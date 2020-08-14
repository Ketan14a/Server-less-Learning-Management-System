import boto3
from flask import Flask 
from flask import render_template
from flask import url_for, flash, redirect

app = Flask(__name__)

def getClusters():
	ACCESS_KEY = 'ASIAXPZJUBM2M2BGDDOM'
	SECRET_KEY = 'LZd4uHC223NrZh5MzGQj0+VFSjg314ynja4lf/AR'
	SESSION_TOKEN = 'FwoGZXIvYXdzEMv//////////wEaDHIgvIaV6ysJ1K/XCSLEASp+qBApzZlw7C3PVoOqBmTEI/JMuYqrtnkP2BFiVs6w9b6MtdadJOPWGnu6b6Bh3uIWsJrnqKQfvLGQVyP/cNwPuw+lluH9F7In76pjVnMxYkHVOtsJKg50elIoAqahQAzBBt3JThk98fvFOh+K+tfyY48MIazk3fMBN2vWGmh/RMEkmpUdlXNCFSQfeLmq0oH6cCf85Y4mHagXASAaeso7MGFzuX5IdSHL0CqxKYczZyrSUwGBNkuAmnFbfX7gf+GQqfsovdSd+QUyLaoU2dNJqUTgduLase3qVZg4+1BTewQWxIBRqOK+rDbdmlSvtOBTUIYeelW8aw=='




	s3 = boto3.client('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,region_name='us-east-1',aws_session_token=SESSION_TOKEN)
	bucket = 'clusters-b00839791'

	keys = []
	resp = s3.list_objects_v2(Bucket=bucket)
	for obj in resp['Contents']:
		keys.append(obj['Key'])

	return keys


@app.route("/")
def home():
	keys = getClusters()
	Companies = []
	Exchanges = []
	People = []
	Places = []
	Topics = []
	for key in keys:
		print(key)
		if key[-1]=='/':
			print("Continued")
		elif "Companies" in key:
			temp = key.split("/")
			Companies.append(temp[1])
		elif "Exchanges" in key:
			temp = key.split("/")
			Exchanges.append(temp[1])
		elif "People" in key:
			temp = key.split("/")
			People.append(temp[1])
		elif "Places" in key:
			temp = key.split("/")
			Places.append(temp[1])
		elif "Topics" in key:
			temp = key.split("/")
			Topics.append(temp[1])
		else:
			print("else")

	return render_template('home.html', Companies=Companies, Exchanges=Exchanges, People=People, Places=Places, Topics=Topics)

if __name__ == '__main__':
	app.run(port=9093,debug=True)