import json
import boto3


# 	"S3 — Boto3 Docs 1.13.16 documentation", Boto3.amazonaws.com, 2020. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html  [Accessed: 26- Jul- 2020].
# 	"Removing stop words with NLTK in Python - GeeksforGeeks", GeeksforGeeks, 2020. [Online]. Available: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/ . [Accessed: 26- Jul- 2020].
# 

def lambda_handler(event, context):
    dic={}
    aws_access_key_id="ASIA4G5DYN6EYBXFL54A"
    aws_secret_access_key="V57d11F3GAoKv1Adsgz2p2Wmhp+gFQ0zxIb04QtO"
    aws_session_token="FwoGZXIvYXdzEEAaDPiYwZt1upLivxwTLiK+AcHXOS+qZW6VeAmeJSB0QiP5oXhJV3KXUnubuQaium/SbtKN+MyaRggpFHGlQuzfYMsQQmuwybcGqb/orntkpT73VjcXMiICZsU+NMOHrqVxYgvdGVs9infenARVMuAsNM4faNdZ/kgh17H1Fg0sXdTKZ+UwiHUXMVnd+zuyYU1jTrh76OIk3Y1fDHKoHYcvaZQ1eFVgbeTRBABxmr5h7eQaTvixoXL9W000M+qFHE8NavBZohya4YrR22Cjp78o0In/+AUyLUzjIIMO6KZeSOY4Y/ZKUrYLddlVOlX4/nOzuUd7kO124RoKAEZX2XAR/sDCfQ=="
    s3r = boto3.resource('s3', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name='us-east-1',aws_session_token=aws_session_token)
    s3c = boto3.client('s3', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name='us-east-1',aws_session_token=aws_session_token)
    # s3 = boto3.client("s3",aws_access_key_id='',aws_secret_access_key='')
    bucket = "data-processing-5410"
    # This list of stopwords has been taken from NLTK python library. from nltk.corpus import stopwords
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    # again assumes boto.cfg setup, assume AWS S3
    for key in s3c.list_objects(Bucket=bucket)['Contents']:
        key = key['Key']
        print("in for loop")
        break
    # key = 'test_file.txt'
    file = s3c.get_object(Bucket = bucket, Key = key)
    print(file)
    p = file["Body"].read().decode("utf-8")
    li = p.split("\n")
    


    for line in li:
        words = line.split(" ")
        for word in words:
            if word not in stopwords:
                word = word.strip()
                word = word.lower()
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word]+=1
    print(dic)
    js_tags = json.dumps(dic)
    print(js_tags)
    Bcloud = "word-cloud-5410"
    s3r.Bucket(Bcloud).put_object(Key="cloud.json",Body=str(js_tags))