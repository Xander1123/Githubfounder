from flask import Flask,render_template,request
import requests

app=Flask(__name__)
base_url='https://api.github.com/users/'


@app.route("/",methods = ["GET","POST"])

def index():
    if request.method == "POST":
        githubname=request.form.get("githubname")
        response_user=requests.get(base_url + githubname)
        response_repo=requests.get(base_url +githubname +'/repos')

        repos=response_repo.json()
        user_info=response_user.json()

        if "message" in user_info :
            return render_template('index.html',error="Istifadəçi tapılmadı........")
        else:

            return render_template("index.html",profile = user_info,repos = repos)
    else:
        return render_template("index.html")
if __name__=='__main__':
    app.run(debug=True)