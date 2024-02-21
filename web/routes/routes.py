from flask import render_template, Blueprint, jsonify

from models.models import Flat

main = Blueprint('main', __name__)


@main.route('/')
def home():
    try:
        flats = Flat.query.all()
        return render_template('home.html', items=flats)
    except Exception as e:
        return f"An error occurred: {e}"


@main.route('/ok', methods=['GET'])
def ok():
    return jsonify({"status": "up"}), 200
