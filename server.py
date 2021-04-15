from crawling import *
import flask
from flask import Flask,render_template

app = Flask(__name__,template_folder='template',static_folder='static')

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/traders-holiday')
def 이마트트레이더스():
  return render_template('traders-holiday.html',이마트=holiday.text)
  
@app.route('/traders-video')
def 이마트트레이더스비디오():
    return render_template('traders-video.html')

@app.route('/teach-video')
def teachvideo():
    return render_template('teach-video.html')
 
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,use_reloader=False, debug=True)