import requests
import json
import pymysql

def hello_world(request):
    dbConfig = pymysql.connect("host","admin","pass","UserDB" )
    cursor = dbConfig.cursor();
    request_json = request.get_json()
    registration_url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=APIKEY'
    firebase_obj = {}
    firebase_obj['email']=request_json['email'];
    firebase_obj['password']=request_json['password']
    firebase_obj['returnSecureToken']=True;
    result = requests.post(registration_url, data = json.dumps(firebase_obj))
    firebase_result = result.json()
    if "error" in firebase_result and firebase_result["error"]!= None:
        return json.dumps({'status': False, 'message': 'Invalid Username or Password'})
    elif "registered" in firebase_result and firebase_result["registered"] == True:
        cursor.execute("select question, answer from user_security where email = %s", (request_json["email"]))
        row = cursor.fetchone()
        if row != None:
            firebase_result['question'] = row[0]
            firebase_result['answer'] = row[1]
    return json.dumps(firebase_result)

