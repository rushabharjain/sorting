from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/selection_sort")
def ss():
    return render_template("selection_sort.html")

@app.route("/bubble_sort")
def bs():
    return render_template("bubble_sort.html")

@app.route("/merge_sort")
def ms():
    return render_template("merge_sort.html")
if __name__=="__main__":
    app.run(debug=True)

