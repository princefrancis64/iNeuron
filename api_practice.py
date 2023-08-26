from flask import Flask,request, jsonify
app = Flask(__name__)

@app.route('/abc',methods = ['GET','POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b =  request.json['num2']
        result = a+b
        return jsonify(result)

@app.route('/abc1',methods = ['GET'])
def test2():
    a = request.json['num1']
    b = request.json['num2']
    result = a*b
    return jsonify(result)


if __name__=='__main__':
    app.run(debug = True)

