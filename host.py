from flask import Flask
app= Flask(__name__)
@app.route("/")
def i():
    return 'Hi!'
if __name__ == "__main__":
    i()