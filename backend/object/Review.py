class ReviewObj:
    def __init__(self, fair_id, title, date, review, review_body):
        self._id = fair_id
        self._title = title
        self._date = date
        self._review = review
        self._review_body = review_body

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_date(self):
        return self._date

    def get_review(self):
        return self._review

    def get_review_body(self):
        return self._review_body

    def serialize(self):
        return {
            "id": self._id,
            "title": self._title,
            "date": self._date,
            "review": self._review,
            "review_body": self._review_body
        }
