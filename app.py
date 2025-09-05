from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "<h1>Hello from Flask!</h1><p>This is a dynamic Python app.</p>"

if _name_ == "__main__":

    app.run(debug=True)
