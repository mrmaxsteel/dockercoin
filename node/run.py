# encoding=utf-8

from flask import Flask, render_template
from node import DCNode
import os

app = Flask(__name__)
dc_node = DCNode(str(os.environ['NODE_ADDRESS']))

@app.route("/dashboard")
def dashboard():
    return render_template("index.html", address_list=dc_node.address_list)

@app.route("/getaddr")
def gettaddr():
    return dc_node.address_list[0]['addr']
