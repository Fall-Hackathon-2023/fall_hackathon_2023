from flask import Blueprint, jsonify, request, Response
from backend.object.Review import ReviewObj as Review

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

review_database = []
id_tracker = 0


@reviews_bp.route("/all", methods=["GET"])
def get_all_reviews():
    json_review_list = []

    global review_database

    for review in review_database:
        get_id = review.get_id()
        title = review.get_title()
        date = review.get_date()
        review_flt = review.get_review()
        review_body = review.get_review_body()
        json_review_list.append(
            jsonify(
                {"id": get_id,
                 "title": title,
                 "date": date,
                 "review": review_flt,
                 "review_body": review_body}
            ))

    return jsonify(json_review_list)


@reviews_bp.route("/create", methods=["POST"])
def create_reviews():
    new_review = request.get_json()

    title = new_review['title']
    date = new_review['date']
    review = new_review['review']
    review_body = new_review['review_body']

    review_obj = Review(increment_id(), title, date, review, review_body)

    review_database.append(review_obj)

    return Response(status=204)


def increment_id():
    global id_tracker
    id_tracker += 1
    return id_tracker

def populate_db():
