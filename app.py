from flask import Flask,jsonify,request
import os,json

dir=os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

fileoutput=open(dir+'/data/file.txt','rb')
translations=fileoutput.read()
fileoutput.close()

@app.route('/',methods=['GET'])
def get_items():
	return translations

@app.route('/',methods=['POST'])
def update_json():
	json_obj=request.json
	fileinput=open(dir+'/data/file.txt','a')
	fileinput.write(str(json_obj).replace("'",'"')+'\n')
	fileinput.close()
#	translations=open(dir+'/data/file.txt','rb').read() # update data in localhost
	return translations

if __name__=='__main__':
	app.debug=True
	app.run()
