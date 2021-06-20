from flask import Flask, request, render_template
from dao import EmpDAO
from dto import EmpDTO

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
    data = EmpDAO().empone(empno)
    return data

@app.route('/insertemp', methods=['POST'])
def insertemp():
    dto = EmpDTO(request.form.get("empno"), request.form.get("ename"), request.form.get("sal"))
    EmpDAO().empinsert(dto)
    # return EmpDAO().empone(request.form.get("empno")) search input tag에 값 반환됨
 
@app.route('/updateemp', methods=['PUT'])
def updateemp():
    dto = EmpDTO(request.form.get("empno"), request.form.get("ename"), request.form.get("sal"))
    EmpDAO().empupdate(dto)   
    # return EmpDAO().empone(request.form.get("empno")) search input tag에 값 반환됨

@app.route('/deleteemp', methods=['DELETE'])
def deleteemp():
    dao = EmpDAO()
    empno = EmpDTO(request.form.get("empno"), request.form.get("ename"), request.form.get("sal"))
    dao.empdelete(empno)

    return dao.empone(request.form.get('empno'))

@app.route("/emplist", methods=["get"])
def emplist():
    return EmpDAO().empall()


if __name__ == '__main__':
    app.run(debug=True)