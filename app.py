from flask import Flask, redirect, render_template, request, abort

import random

app = Flask(__name__)

'''@app.before_request
def before_request():
    print('hello')'''

#WEB STARTS HERE
@app.route('/', methods=["GET"])
def index():
    #userHeader = str(request.headers)
    return render_template('index.html')

@app.route('/load', methods=["get"])
def load():
    userGrade = str(request.values.get("userGrade"))
    userClass = int(request.values.get("userClass")) - 1 

    f = open('./rsc/tt' + userGrade + '.json', encoding  = 'utf8')
    json_data = eval(f.read())

    userClassData = json_data[userClass]
    userElectives = []
    for i in range(6):
        for j in range(5):
            if(len(userClassData[j][i]) > 1):
                for k in range(len(userClassData[j][i])):
                    if(not (userClassData[j][i][k]['subject'] in userElectives)):
                        userElectives.append(userClassData[j][i][k]['subject'])

    userElectives.sort()

    return render_template('choose.html', userClass=(userClass + 1) , userGrade=userGrade , userElectives = userElectives)

@app.route('/submit', methods=["GET"])
def submit():
    userGrade = str(request.values.get("userGrade"))
    userClass = int(request.values.get("userClass")) - 1 
    userElectives = request.values.getlist("userElectives")
    username = request.values.get("username")


    f = open('./rsc/tt' + userGrade + '.json', encoding  = 'utf8')
    json_data = eval(f.read())
    userClassData = json_data[userClass]

    for i in range(6):
        for j in range(5):
            if(len(userClassData[j][i]) > 1):
                for k in range(len(userClassData[j][i])):
                    if(userClassData[j][i][k]['subject'] in userElectives):
                        userClassData[j][i] = eval("["+ str(userClassData[j][i][k]) + "]")
                        break

    days = ['#','Mon','Tue','Wen','Thur','Fri']

    return render_template('table.html', days=days, username=username, userClass=(userClass + 1) , userGrade=userGrade , userClassData = userClassData, userElectives = userElectives)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
