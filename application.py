from flask import Flask

application = Flask(__name__)  # EB looks for this name

@application.route('/')
def hello():
    return "🚀 Hello from Flask on Elastic Beanstalk!"

if __name__ == "__main__":
    application.run(debug=True)
