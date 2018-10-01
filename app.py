import navigation
from flask import Flask, render_template, jsonify
from map_render import *

import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/scan')
def scan():
    return render_template('index_camera.html')

@app.route('/directions/<start>/<dest>', methods=['GET'])
def render_directions(start, dest):

    instructions = directions(start, dest)["direction"]
    map = directions(start,dest)["map_render"]


    encoding = map[2: -1]
    print(encoding)
    print(len(encoding))
    return render_template("results.html", instructions=instructions, map = encoding, start= start, end = dest)



def directions(start, dest):

    nodes = navigation.g.shortest_path(start, dest)

    response = {
        "direction": navigation.generate_route(nodes),
        "map_render": str(render_map(nodes))}

    return response

    # return jsonify(response)

if __name__ == '__main__':
    app.run(debug = True)
