from flask import Flask, request
app= Flask(__name__)

@app.route('/default/<name>')
def show_post(name):
    print(name)
    return 'the value is ' + name

if __name__=="__main__":
     app.run()
