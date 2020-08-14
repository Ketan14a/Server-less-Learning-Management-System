import requests
import json
import pymysql


def hello_world(request):
    dbConfig = pymysql.connect("host","admin","pass","UserDB" )
    cursor = dbConfig.cursor();
    request_json = request.get_json()
    registration_url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=APIKEY'
    firebase_obj = {}
    firebase_obj['email']=request_json['email'];
    firebase_obj['password']=request_json['password']
    firebase_obj['returnSecureToken']=True;
    result = requests.post(registration_url, data = json.dumps(firebase_obj))
    firebase_result = result.json()
    print('response::'+str(firebase_result))
    if "idToken" in firebase_result and None!=firebase_result["idToken"] and firebase_result["idToken"] != '':
        print('checkk')
        cursor.execute("INSERT INTO user(`email`,`firstname`,`lastname`,`institution`,`password`,`role`,`active`) VALUES (%s,%s,%s,%s,%s,%s,%s)",(request_json['email'],request_json['firstName'],request_json['lastName'],request_json['institution'],request_json['password'],request_json['role'],'0'))
        dbConfig.commit()
        print('checkk1')
        cursor.execute("INSERT INTO user_security(`email`,`question`,`answer`) VALUES (%s,%s,%s)",(request_json['email'],request_json['question'],request_json['answer']))
        dbConfig.commit()
        print('checkk2')
        return result.text
    elif "error" in firebase_result and firebase_result["error"]!=None and firebase_result["error"]["message"]!= None and firebase_result["error"]["message"] == 'EMAIL_EXISTS':
        return json.dumps({'status':False,'message':'User already exist'})
    else:
        return "failed"