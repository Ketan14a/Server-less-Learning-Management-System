from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import datetime
import json
import boto3
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#text refernce https://www.gutenberg.org/files/60271/60271-8.txt
#text refernce https://www.gutenberg.org/ebooks/1661
# 	"S3 — Boto3 Docs 1.13.16 documentation", Boto3.amazonaws.com, 2020. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html  [Accessed: 26- Jul- 2020].


data = Flask(__name__)
data.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

aws_access_key_id="ASIA4G5DYN6EY4JEPH3D"
aws_secret_access_key="TnyrgeAQGGxMT/r5CllvW1Q4AaL44XjrCh32nKyR"
aws_session_token="FwoGZXIvYXdzEGEaDKQEufC3KrjrsLeN5yK+AZHjFyU36O9042mPiKEDJbMBZkK4c3T+oZ/vSaeRRJvbbSnvA3EQ27drWvboxsfA31YLqeRxkJn1l6bRUs4G5+QPUat5gzOSb87xOhfuecppLNaKQIndN63Nvi9JhAzXkRpSu1WxU5CKxgr1yUafoM5WrbcwBxgE7iXIu/Vc4s5xT7TPjwM2UJFc1DmsTYG4TjfrPfoGxyTMJ1PFjAsodBo570JFiS6ZktusuC+/4iw2hpNnM6U0DlVYk9cLtogohLeG+QUyLcm9DKk9YPzxEDe7Yp+GDGoerc9TlV0QKxgwP9utlpDGu0lS5Cx/Hj57RHl7cA=="
s3r = boto3.resource('s3', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name='us-east-1',aws_session_token=aws_session_token)
s3c = boto3.client('s3', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name='us-east-1',aws_session_token=aws_session_token)
b1 = "data-processing-5410"
b2 = "word-cloud-5410"

@data.route('/', methods=['GET'])
def func1():
	return render_template('upload.html')


@data.route('/upload', methods=['POST', 'GET'])
def func2():
	if request.method == 'POST':
		file = request.files['file']
		print(file)
		# for i in file:
		# 	print(i)
		print(file.content_length)
		file.filename = secure_filename(file.filename)
		try:
			s3c.upload_fileobj(file, b1, file.filename, ExtraArgs={
                "ACL":"public-read",
                "ContentType": file.content_type
            })
		except Exception as e:
			print("Exception: " + str(e))
		print(file)
		print(file.filename)
		return render_template("success.html", message="Success!")
	return render_template("success.html", message="Data Processing Application")

@data.route('/wordcloud', methods=['GET'])
def func3():
	try:
		bucket = s3r.Bucket(b2)
		obj = s3r.Object(b2, "cloud.json")
		body = obj.get()['Body'].read()
		body = body.decode("utf-8")
		dic = json.loads(body)
		text = ""
		for i in dic:
			text+=(i.strip()+" ")*dic[i]
		text=text.strip()
		wc = WordCloud(collocations = False)
		wc.generate(text)
		wc.to_file('./static/output.png')
		bucket = s3r.Bucket(b1)
		key = "img.png"
		bucket.upload_file('./static/output.png', key, ExtraArgs={'ACL':'public-read'})
		url="https://data-processing-5410.s3.amazonaws.com/" + key
		return render_template('wordcloud.html', url = url)
	except Exception as e:
		print("Exception: " + str(e))
		return render_template('wordcloud.html')

@data.route('/clean_data_bucket', methods=['GET'])
def func4():
	bucket = s3r.Bucket(b1)
	bucket.objects.all().delete()
	return render_template("success.html", message="Data Processing Application")


@data.route('/clean_word_bucket', methods=['GET'])
def func5():
	bucket = s3r.Bucket(b2)
	bucket.objects.all().delete()
	return render_template("success.html", message="Data Processing Application")

if __name__ == "__main__":
	data.debug = True
	data.run(host='0.0.0.0', port=8080)


