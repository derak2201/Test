from flask import Flask,render_template,request
from calculation import caleculator
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/homesubmit',methods=['POST'])
def cal():
    if request.method =='POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['opt']
        cal = caleculator.flask_cal()
        ans = cal.caleculation(operation,num1,num2)


        return render_template('output.html',results=ans)




if __name__ == '__main__':
    app.run(debug=True)



