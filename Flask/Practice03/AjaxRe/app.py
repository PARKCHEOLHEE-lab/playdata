from flask import Flask, request, render_template
from dao import EmpDAO

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return render_template('reqres.html')

@app.route('/getdata', methods=['GET'])
def getdata():
    return '{"name" : "BRIGHT-HOPE", "age" : 28}'

@app.route('/getemp', methods=['POST'])
def getemp():
    empno = request.form.get('empno')
    dao = EmpDAO()
    data = dao.empone(empno)
    return data

if __name__ == '__main__':
    app.run(debug=True)