from flask import Flask, render_template, jsonify, request, make_response

app = Flask(__name__, static_url_path='', static_folder='static')

client_ids = {}

@app.route('/', methods=["GET"])
def hello():   
    resp = make_response(render_template('index.html')) 
    return resp

if __name__ == '__main__':
    app.run()