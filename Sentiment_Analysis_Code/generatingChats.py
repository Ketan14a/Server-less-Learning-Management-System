import json


with open('conversation.json') as f:
  data = json.load(f)

Chats = []

for chats in data['conversations']:
	temp = "\n".join(chats)
	Chats.append(temp)


L = len(Chats)

for i in range(L):
	filePath = "./Chats/"+str(i)+".txt"
	target_file = open(filePath,"w")
	target_file.write(Chats[i])
	target_file.close()




