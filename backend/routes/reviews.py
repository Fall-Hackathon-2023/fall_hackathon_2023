from flask import Blueprint, jsonify, request, Response, render_template
from backend.object.Review import ReviewObj as Review
from faker import Faker
import random

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
        json_review_list.append(Review(get_id, title, date, review_flt, review_body))

    return jsonify([e.serialize() for e in json_review_list])


@reviews_bp.route("/create", methods=["POST"])
def create_reviews():
    new_review = request.get_json()

    fair_id = new_review['id']
    title = new_review['title']
    date = new_review['date']
    review = new_review['review']
    review_body = new_review['review_body']

    review_obj = Review(fair_id, title, date, review, review_body)

    review_database.append(review_obj)

    return Response(status=204)


def populate_db():
    global review_database

    fake = Faker()

    id_selector = [1, 2, 3, 4, 5, 6, 7, 8]
    id_to_fair = {1: "Grace Hopper Celebration",
                  2: "PyCon",
                  3: "Developer Week",
                  4: "CodePath",
                  5: "RTC",
                  6: "SWE",
                  7: "TAPIA",
                  8: "NSBE",
                  9: "OSU Engineering"}

    for i in id_selector:
        for _ in range(0, random.randint(5, 11)):
            fair_id = i
            fair_title = id_to_fair[i]
            date = fake.date_this_year(True, False)
            date = date.strftime("%m/%d/%y")
            review = round(random.uniform(4.5, 5.0), 2)
            review_body = fake.paragraph(2)
            new_review = Review(fair_id, fair_title, date, review, review_body)
            review_database.append(new_review)
