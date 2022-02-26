import pyrebase

config = {
	"apiKey": "AIzaSyDrdiYaeeC_kFwgiR27apzWhX-dzoacOCI",
    "authDomain": "indent-for-purchase.firebaseapp.com",
    "projectId": "indent-for-purchase",
    "storageBucket": "indent-for-purchase.appspot.com",
    "messagingSenderId": "655214437659",
    "appId": "1:655214437659:web:61c24f217752a9358a1fbe",
    "measurementId": "G-5JPWPNQ52F",
	"databaseURL":"https://indent-for-purchase-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':
			dic={}
			dic["Indenter"] = request.form['Indenter']
			dic["Budget"] = request.form['Budget']
			dic["Cost"] = request.form['Cost']
			dic["Item"] = request.form['Item']
			# stocks = ['reliance', 'infosys', 'tcs']
			# prices = [2175, 1127, 2750]
			# dictionary = dict(zip(stocks, prices))
			# print(dictionary)

			db.child("form").push(dic)
			# db.child("todo").push(Budget)
			# db.child("todo").push(Cost)
			# db.child("todo").push(Item)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html')# t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
