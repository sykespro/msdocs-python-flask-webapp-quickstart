import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

def query_llm(question): 
    # response = llm_chain.invoke({'question': question})
    # mock response like of object to be used like response.content
    response = {'content': 'This is a mock response for the question: ' + question}
    return response 

@app.route('/poc/vmrx')
def vmrx_index():
   print('Request for vmrx page received')
   return render_template('vmrx/index.html')

@app.route("/poc/vmrx/chatbot", methods=["POST"]) 
def vmrx_chatbot(): 
    data = request.get_json() 
    question = data["question"] 
    response = query_llm(question)   
    return jsonify({"response": response['content']})

if __name__ == '__main__':
   app.run()
