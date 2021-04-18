from flask import Flask, render_template, request
import requests
import secrets
import json

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    param = {'api-key':secrets.key}
    result = requests.get(base_url,param).json()
    title_list = []
    cnt = 0

    for i in result['results']:
        title_list.append(i['title']) 
        cnt += 1
        if (cnt == 5):
            break

    return render_template('name.html', name=nm, title_list=title_list)    

if __name__ == '__main__':  
    app.run(debug=True)