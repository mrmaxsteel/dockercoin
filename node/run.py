# encoding=utf-8

from flask import Flask, render_template
import node

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return render_template("index.html", address_list=node.address_list)

@app.route("/getaddr")
def gettaddr():
    return node.address_list[0]['addr']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
