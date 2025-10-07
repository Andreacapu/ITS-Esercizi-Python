from flask import Flask
app = Flask(__name__)

app.run(debug=True, host='127.0.0.1', port=6000)

@app.route('/')
def home()->str:
    return "<h3>Hello World!</h3>"

@app.route('/user/<string:user>')
def show_user(user:str)->str:
    return f"Benvenuto {user}"