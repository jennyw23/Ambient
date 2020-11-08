from flask import Flask, request
from Techtogether2020.database import Temp
from Techtogether2020.ambient-temperature-finder import APItemp
temp = Temp()
app = Flask(__name__)

#this is the route that client uses to add a temperature change request
@app.route('/createRequest', methods=['POST'])
def create():
    res = request.json
    Username= res['Username']
    temp = APItemp()
    temp.request()
    
    res = temp.put(Username="Username", TempRequest="Temp")
    #print(res) ## only here for debugging
    return res

#this is the route the admin uses to view the changes requested
@app.route('/view', methods=["GET"])
def viewing():
    res = temp.view()
    return res


if __name__ == '__main__':
    app.run(debug=True)