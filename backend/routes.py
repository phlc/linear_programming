from flask import Blueprint, request



routes = Blueprint("routes", __name__)


@routes.route('/', methods=['GET'])
def home():
    return {"Hello": "Worldfrsf"}