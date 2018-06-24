'''
data = eval("[{'subject': '영어IA', 'teacher': '소영'}, {'subject': '영어IB', 'teacher': '윤주'}]")

print(data[0]['subject'])

'''
import json
import pprint

f = open('./rsc/tt2.json', encoding  = 'utf8')
json_data = eval(f.read())

electives = ['수리논술A','미적분IIB','세계사','영화기술A','연극제작실습','지구과학II','사회문화B','생활과윤리B', '스포츠과학A']

userClassData = json_data[0]

print(str(userClassData) + "\n\n\n\n")

'''
for i in range(6):
    for j in range(5):
        if(len(userClassData[j][i]) > 1):
            for k in range(len(userClassData[j][i])):
                if(userClassData[j][i][k]['subject'] in electives):
                    userClassData[j][i] = eval("["+ str(userClassData[j][i][k]) + "]")
                    break

print(str(userClassData))

'''
userElectives = []
for i in range(6):
    for j in range(5):
        if(len(userClassData[j][i]) > 1):
            for k in range(len(userClassData[j][i])):
                if(not (userClassData[j][i][k]['subject'] in userElectives)):
                    userElectives.append(userClassData[j][i][k]['subject'])

userElectives.sort()
print(str(userElectives))
