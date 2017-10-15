# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging
import os
import subprocess
import shlex
import tempfile
import shutil
from shutil import copyfile
#from flask import Flask, jsonify, request
import flask_cors
from flask import Flask, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename

import sqlite3
import json
from sqlite3 import Error


app = Flask(__name__)
#Request = app(__Flask__)
flask_cors.CORS(app)
conn = sqlite3.connect('facecon.db')


@app.route('/')
def start():
    return "Hello Chandan !!!"
   

@app.route('/getProfile', methods=['GET'])
def createProfile():
    print "I m inside create Profile"
    #data=request.get_json()
    

    #hi
    #createtable()
    #jsondata=json.dumps(data)
    #dict1 = json.loads(jsondata)
    #print dict1['Userid']
    
    #insertion(dict1)
    #fetch(dict1)
    
    return "Profile created Successfully"

@app.route('/createProfile', methods=['POST'])
def createProfile1():
    print "I m inside create Profile"
    
    data=request.get_json()
    print data;

    #hi
    createtable()
    jsondata=json.dumps(data)
    dict1 = json.loads(jsondata)
    print dict1['Userid']
    
    insertion(dict1)
    fetch(dict1)
    
    return "Profile created Successfully"

@app.route('/fetchProfile/<userId>',methods=['GET'])
def fetchingProfile(userId):	
 		x=fetchProfile(userId)
                response = app.response_class(
                	response=json.dumps(x),
                	status=200,
                	mimetype='application/json'
                 	)
                
         	return response
 


@app.errorhandler(500)
def server_error(e):

    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]






def create_connection(db_file):
    
    conn.commit()
     
  

def createtable():
    c=conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS profile2 (
        Userid TEXT,FirstName TEXT, LastName TEXT, Contact INTEGER, Emailid TEXT, 
         Interest TEXT, path1 TEXT);
     ''')
    conn.commit()
    print "hello"

def insertion(data):
    
    
    cur = conn.cursor()
    print data
    print data['path1']
    #print dict1
    # cur.execute("INSERT INTO profile2 VALUES ('chaitr','chai','ramdas','22222','x@gmail.com','madness','C/fnnnn/sskk')");

    userid=data['Userid']
    firstname=data['FirstName']
    lastname=data['LastName']
    contact=data['Contact']
    emailid=data['Emailid']
    interest=data['Interest']
    path=data['path1']
    cur.execute('INSERT INTO profile2 (Userid,FirstName,LastName,Contact,Emailid,Interest,path1) VALUES(?,?,?,?,?,?,?)',(userid,firstname,lastname,contact,emailid,interest,path))
    conn.commit()
    print "Records created successfully"

   

def fetch(data):
   
    userid=data['Userid']
    c=conn.cursor()
    c.execute('SELECT * FROM profile2 WHERE Userid =?', (userid,))
    
    print(c.fetchone())
    conn.commit()

def fetchProfile(userid):
   
    
    c=conn.cursor()
    c.execute('SELECT * FROM profile2 WHERE Userid =?', (userid,))
    jsonData=c.fetchone()
    print(c.fetchone())
    print('I reached here') 
    conn.commit()
    jData={}
    jData['Userid']=jsonData[0]
    jData['FirstName']=jsonData[1]
    jData['LastName']=jsonData[2]
    jData['Contact']=jsonData[3]
    jData['Emailid']=jsonData[4]
    jData['Interest']=jsonData[5]
    jData['path1']=jsonData[6]
    

    
    return jData  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
 


