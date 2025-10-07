from flask import Flask
app = Flask(__name__)

#app.run(debug=True, host='127.0.0.1', port=4000)

@app.route('/')
def home()->str:
    return "<h3>Hello World!</h3>"

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username:str, age:int)->str:
    return f"Profilo di {username}, età:{age}"

@app.route('/post/<int:post_id>')
def show_post(post_id:int)->str:
    return f"Post {post_id}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='John Doe', age=30))
    print(url_for('show_post', post_id=42))