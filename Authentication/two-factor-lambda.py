import json
import pymysql


db = pymysql.connect("host","admin","pass","UserDB")
cursor = db.cursor()

def lambda_handler(event, context):
        #body = json.loads(event["body"])
        body=json.loads(event["body"])
        
        cursor.execute("select 1 from user_security where answer = %s and email = %s; ",(body["answer"],body["email"]))
        result = cursor.fetchone()
        if result is not None:
            cursor.execute("select firstname,lastname,role,institution from user where email = %s;", (body["email"]))
            output = {}
            row = cursor.fetchone()
            if row != None:
                output['firstname'] = row[0]
                output['lastname'] = row[1]
                output['role'] = row[2]
                output['institution'] = row[3]
                cursor.execute("update user set active=1 where email= %s ; ", (body["email"]))
                db.commit()
            return {
                'statusCode': 200,
                'body': json.dumps(output)
            }
        else:
             return {
                'statusCode': 200,
                'body': json.dumps(False)
            }