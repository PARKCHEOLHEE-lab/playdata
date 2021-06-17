from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def signup():
    return render_template('request.html')

@app.route('/info', methods=['post'])
def info():
                               # name
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email = request.form.get('e_mail')
    dob = request.form.get('DOB')
    country = request.form.get('country')
    intro = request.form.get('subject')

    info = {'first_name':fname, 'last_name':lname, 'e_mail':email, \
            'dob':dob, 'country':country, 'intro':intro}

    return render_template('response.html', user_info = info)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)