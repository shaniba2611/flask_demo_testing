from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return"<h1>THIS IS A FLASK APPLICATION</h1>"



if __name__=="__main__":
    app.run()
