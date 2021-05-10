from flask import Flask, render_template, request, send_file
import json
import os

app = Flask(__name__)

base_path = 'D:\\Data\\Projects\\'

def load_files(path):
    files = os.listdir(path)
    fdict = {}
    for file in files:
        fdict[path+str(file)+"\\"] = file
    return fdict


@app.route('/')
def index():
    ip = str(request.remote_addr)
    file_list = load_files(base_path)
    return render_template("index.html", files = file_list, ip = ip)


@app.route('/download')
def download_file():
    try:
        print (request.args.get)
        path = request.args.get("name")
        print("Path:", path)
        file_list = load_files(path)
        return render_template("index.html", files = file_list)
    except NotADirectoryError:
        path = request.args.get("name")
        path = path[:-1]
        return send_file(path, as_attachment=True)        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, threaded = True)