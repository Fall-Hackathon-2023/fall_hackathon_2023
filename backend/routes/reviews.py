from flask import Blueprint

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@reviews_bp.route("/all", methods=["GET"])
def get_all_reviews():

    all_reviews = [{"id": 1, "name": "bob"}, {"id": 2, "name": "joe"}]

    return jsonify(all_reviews)


