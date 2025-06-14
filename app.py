from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource
from os import getenv
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.config["FLASK_DEBUG"] = getenv("FLASK_DEBUG", False)
app.config["FLASK_RUN_HOST"] = getenv("FLASK_RUN_HOST")
app.config["FLASK_RUN_PORT"] = getenv("FLASK_RUN_PORT")
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
api = Api(app)
cors = CORS(app)


class Hello(Resource):
    def get(self):
        return {"message": "Server is running !"}, 200


api.add_resource(Hello, "/")


if __name__ == "__main__":
    app.run()
