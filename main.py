from flask import Flask, render_template
loggedin=False
app=Flask(__name__)
def bolden(f):
    def inner():
        if loggedin:
            return f"<h1>{f()}</h1>"
        else:
            return "Please wait a bit before doing this"
    return inner
@app.route("/")
@bolden
def main():
    return "Hello World"
if __name__=="__main__":
    app.run(port=3000)
