# https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=2

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# function that would display the page
# this would return to our home page, we could also say "/home"
@app.route("/<name>")
def home(name):
    return render_template("index.html", content = ["tech", "with", "tim"], r = 2)

if __name__ == '__main__':
    app.run()