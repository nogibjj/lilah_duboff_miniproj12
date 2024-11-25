from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Book Search Route
@app.route("/search", methods=["POST"])
def search_books():
    query = request.form["query"]
   
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)
    data = response.json()

    books = [
        {
            "title": book.get("title"),
            "author": ", ".join(book.get("author_name", [])),
            "cover_i": book.get("cover_i"),
            "key": book.get("key"),
        }
        for book in data.get("docs", [])
    ]

    return render_template("search_results.html", books=books, query=query)


# Book Details Route
@app.route("/works/<key>")
def book_details(key):
    url = f"https://openlibrary.org/works/{key}.json"
    response = requests.get(url)
    book = response.json()

    details = {
        "title": book.get("title"),
        "description": book.get("description", {}),
        "subjects": book.get("subjects", []),
        "cover_id": book.get("covers", [None])[0],
    }

    return render_template("book_details.html", details=details)


if __name__ == "__main__":
    app.run( port=3000, debug=True)

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello, World!"


# if __name__ == "__main__":
#     app.run("0.0.0.0", port=80, debug=True)
