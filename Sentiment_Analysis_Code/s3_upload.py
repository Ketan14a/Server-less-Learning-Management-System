import boto3

ACCESS_KEY = 'ASIAXPZJUBM2GO7LRAHK'
SECRET_KEY = 'sY5Kn8CO88jxCMHrkLWOqv2xAG8UCUXAR3GhcsTM'
SESSION_TOKEN = 'FwoGZXIvYXdzEAQaDPYv/r4WaJzK0n9HJCLEAc4BuQB3ROL0Wbb9gTl95TYdCFx6GbLSDT68igD9Hk6EM7WxlLby8syqlMgD/Zbt8ikUTFGDYZ5BcRTYBS/gqBfejn+qRUAvKL0b1aZEl7niPJ8OI4+1eqjD4YniX9bB9ndFfPEDrwSokezTLbbSAl0MxKDJqdJ2L3JoTDSCAofLLI41zqkXr8oyRmeknGjzE3sYw0rK4Tbzw267ZdjkfYopB+SLVW81/hTeKXGE3GbW6+qvODWKlGl5EfTZhyfnrsIfyHEo4/3x+AUyLbkGgP54/XjctCrkAR3rgIYGLmmt8YJKSROym6lM0stIyuaS1PZ8d/QWNnkJAQ=='

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,region_name='us-east-1',aws_session_token=SESSION_TOKEN)


for i in range(1):
	path = "./Chats/"+str(i)+".txt"
	name = str(i)+".txt"
	s3.upload_file(path, 'chats-analysis-2', name)
       
        