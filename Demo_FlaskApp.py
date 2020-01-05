#Basics on Creating & Running a flask app
#Importing Flask  class and possibly other dependencies
from flask import Flask, render_template, request, jsonify, Response
#When creating a Flask instance always use __name__
app = Flask(__name__)

#API route to our brower, what is intended to be hit
#Function Name help generate URL's within a path to trigger responses/requests into browser
@app.route('/', methods = ['GET'])
def about():
    return render_template('a1_about.html')

@app.route('/projects', methods = ['GET'])
def projects():
    return render_template('a2_projects.html')

@app.route('/portfolio', methods = ['GET'])
def portfolio():
    return render_template('a3_portfolio.html')

@app.route('/blogs', methods = ['GET'])
def blogs():
    return render_template('a4_blogs.html')

@app.route('/badges', methods = ['GET'])
def badges():
    return render_template('a5_badges.html')

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template('a6_contact.html')

if __name__ == '__main__':
    app.run(host ='127.0.0.1', port = 5000, debug = True)

#To serve or run your flaskapp 
#$ env FLASK_APP=hello.py flask run
