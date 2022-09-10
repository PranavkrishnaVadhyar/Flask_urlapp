from flask import Flask, render_template, request ,redirect ,url_for ,flash, abort, session ,jsonify ,Blueprint
import json
import os.path

app = Flask(__name__)
app.secret_key="ksncwxodjwxmjxdm"

@app.route('/')

def home():
    return render_template("home.html", codes=session.keys())

@app.route('/your_url',methods = ['GET','POST'])

def your_url():
    if request.method=='POST':
        url = {} #creating an empty dict
        
        if os.path.exists('url.json'):        #this is for ensuring that the is no urls with the same short name 
            with open('url.json') as url_file:
                url = json.load(url_file)
                
    
        if request.form['code'] in url.keys():#this returns to the homepage if the short name already exists
                flash('That short name has already been taken. Please give another short name')
                return redirect(url_for('home'))
            
            
        if 'url' in request.form.keys():    #this is to check weather the form content is a file or url
            url[request.form['code']] = {'url':request.form['url']}  #request.form[] accesses the values entered in the coulmns with value given to the(url,code etc) 
                                                                     #dictname[key] = value ,here value is another dict
        
        with open ("url.json",'w') as url_file:
            json.dump(url, url_file)
            session[request.form['code']] = True #this is used to access the history of 
        return  redirect(url_for('home'))  #args is a dictionary that conatins parameters that can be used. Request contains the commands GET and POST etc. GET is default
    else:
        return redirect(url_for('home'))           #this is used to redirect to the home page when the user is invalid
                                                   #url_for is used to access the url using the function
                                                   
                                                   
@app.route('/<string:code>') 
    
def redirect_to_url(code):    #this function is used to redirect to the url using the code given by the user eg:if you give http://127.0.0.1:5000/you it will send you to youtube.com
    if os.path.exists('url.json'):
        with open('url.json') as urls_file:
            url = json.load(urls_file)
            if code in url.keys():
                if 'url' in  url[code].keys():
                    return redirect(url[code]['url'])
                else:
                    return redirect(url_for('static', filename = 'user_files/' + url[code]['file']))
    return abort(404)

@app.errorhandler(404)

def page_not_found(error):
    
   return render_template("page_not_found.html") 


@app.route('/api')

def api():
    return jsonify(list(session.keys()))
