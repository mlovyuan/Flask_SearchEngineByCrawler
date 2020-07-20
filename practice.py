from flask import Flask
from flask import render_template
from crawler import get_google_info
from flask import request

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/search")
def Search():
    # get Index.html內的name = "q"的value
    inputWord = request.args.get("q")
    resultHtml = get_google_info(inputWord)
    return resultHtml

# 固定在這個檔案才能執行
if __name__ == "__main__":
    app.run()