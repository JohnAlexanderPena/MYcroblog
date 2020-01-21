from flask import Flask


#set to the name of the module being used
app = Flask(__name__)


@app.route("/")

def hello():
    return "WOooooow Chechj it oeute!"

if __name__ == "__main__":
    app.run()


from app import routes
