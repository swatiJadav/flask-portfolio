from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        conn = sqlite3.connect("database.db")
        conn.execute(
            "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )
        conn.commit()
        conn.close()

        return "Data saved successfully"

    return render_template("contact.html")

# View saved data
@app.route("/view")
def view():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM contacts").fetchall()
    conn.close()

    return render_template("view.html", rows=rows)

if __name__ == "__main__":
    app.run()

