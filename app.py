from flask import Flask, render_template, request
import plotly.express as px

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    sales = [100, 150, 200, 180, 250]

    bar_fig = px.bar(
        x=months,
        y=sales,
        title="Monthly Sales Dashboard"
    )

    line_fig = px.line(
        x=months,
        y=sales,
        title="Sales Trend"
    )

    return render_template(
        "dashboard.html",
        graph_html=bar_fig.to_html(full_html=False),
        line_graph=line_fig.to_html(full_html=False)
    )


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    import sqlite3

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO leads
        (name,email,phone,message)
        VALUES (?,?,?,?)
        """,
        (name, email, phone, message)
    )

    conn.commit()
    conn.close()

    return """
    <h2>Lead Saved Successfully!</h2>
    <a href="/">Back to Home</a>
    """


if __name__ == "__main__":
    app.run(debug=True)