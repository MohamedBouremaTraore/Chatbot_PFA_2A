import json
file_name="C:\\Users\\Asus\\Desktop\\S4\\Chatbot_PFA_2A\\data\\chatbot_QA.json"
 
with open(file_name, encoding="utf_8") as json_data:
    data = json.load(json_data)
    jsonList=[{}]
    header=["accounts","cards","fundstransfer","insurance","investments","loans","security"]
    for j in header :
        k=0
        for i in data["bank"][j] :
            question=[]
            response=[]
            question.append(i[0])
            response.append(i[1])
          
            key = ['tag','patterns', 'responses']
            k=k+1
            value = [j+str(k),question,response]
            dict_to_json = dict(zip(key, value))
            jsonList.append(dict_to_json)
    print(type(json.dumps(jsonList)))

    
    jsonFileTainingData = open("intents.json", "w")
    jsonFileTainingData.write(json.dumps(jsonList))
    jsonFileTainingData.close()
 
