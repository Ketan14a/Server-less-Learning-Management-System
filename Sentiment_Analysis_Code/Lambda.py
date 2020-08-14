import json
import boto3


def lambda_handler(event, context):
    file_obj = event["Records"][0]
    file_name = str(file_obj['s3']['object']['key'])
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket="chats-analysis-2",Key=file_name)
    file_content = fileObj["Body"].read().decode('utf-8')
    
    Lines = file_content.split("\n")
    comprehend_client = boto3.client("comprehend")
    Sentiments = {}
    i=0
    L = []
    temp = {}
    for line in Lines:
    
        sentiments=json.dumps(comprehend_client.detect_sentiment(Text=line,LanguageCode='en'), sort_keys=True, indent=4)
        sentiments = json.loads(sentiments)
        Sentiment = sentiments["Sentiment"]
        temp[line] = Sentiment
    
    
    myList = []
    
    for key in temp:
        t = key + ":" + temp[key]
        myList.append(t)
    
    
    Ans_str = "\n".join(myList)
    Ans_str = Ans_str.encode("utf-8")
    
    target_bucket = 'sentiments-storage'
    T = file_name.split(".")
    file_name = T[0] + "_sentiment.txt"
    s3_path = file_name
    s3 = boto3.resource("s3")
    s3.Bucket(target_bucket).put_object(Key=s3_path, Body=Ans_str)
    
    return "Done"

    
    

    
    
    
    
