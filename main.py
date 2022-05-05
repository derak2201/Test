import caleculator as calc
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/homesubmit',methods=['POST'])
def cal():
    if request.method =='POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['opt']


if __name__ == '__main__':
    app.run(debug=True)



