from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)
@app.route("/ip")
def template_test():
    ip = requests.get('http://icanhazip.com/').text.strip()
    return render_template('index.html', ip=ip)

if __name__ == '__main__':
    app.run(debug=True)
