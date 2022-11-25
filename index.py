from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__)


@app.route("/")
def index():
    homepage = "<h1>丁鈺蘋Python網頁</h1>"
    homepage += "<a href=/movie>電影查詢</a><br>"
    return homepage

@app.route("/movie", methods=["GET", "POST"])
def movie():
    if request.method == "POST":
        Cond = request.form["keyword"]
        result = "您輸入的電影關鍵字是：" + Cond

        db = firestore.client()
        collection_ref = db.collection("丁鈺蘋電影")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if Cond in dict["title"]:
                result += "片名:<a href="+ dict["hyperlink"] + ">" + dict["title"] + "</a><br>"
                result += "電影分級:"+ dict["rate"] + "<br><br>"
                #result += "電影介紹:"+ dict["hyperlink"] + "<br>"
        if result =="":
            result = "抱歉,查無相關條件的電影資訊"
        
        return result
    else:
        return render_template("movie.html")


if __name__ == "__main__":
    app.run()
