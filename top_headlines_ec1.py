from flask import Flask, render_template, request
import requests
import secrets
import json

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/links/<nm>')
def hello_name(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    param = {'api-key':secrets.key}
    result = requests.get(base_url,param).json()
    d = {}
    cnt = 0

    for i in result['results']:
        d[i['title']] = i['url']
        cnt += 1
        if (cnt == 5):
            break

    return render_template('name_ec1.html', name=nm, dict=d)    

if __name__ == '__main__':  
    app.run(debug=True)