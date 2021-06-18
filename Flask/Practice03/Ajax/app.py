from flask import Flask, request, render_template
from dao import EmpDAO

app = Flask(__name__)

# methods 속성 생략시 default:get
@app.route('/', methods=['get'])
def get():
    return render_template('reqres.html')               # http://127.0.0.1:5000/reqres.html URL

@app.route('/getdata', methods=['get'])
def getdata():
    return '{"name" : "재석", "age" : 49}'

@app.route('/getdata2', methods=['get'])
def getdata2():
    return '{"name" : "철희", "age" : 28}'

@app.route('/getemp', methods=['post'])
def getemp():
    empno = request.form.get("empno")
    print(empno)
    
    dao = EmpDAO()
    data = dao.empone(empno)
    return data


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")  # host, port 생략시 default로 실행