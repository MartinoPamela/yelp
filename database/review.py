from dataclasses import dataclass
from datetime import date

from database.business import Business


@dataclass
class Review:
    review_id: str
    stars: float
    review_date: date
    votes_funny: int
    votes_useful: int
    votes_cool: int
    review_text: str

    # dato che ho una relazione uno a molti ho due alternative: o una stringa o un oggetto
    business_id: str
    business: Business

    def __eq__(self, other):
        return self.review_id == other.review_id

    def __hash__(self):
        return hash(self.review_id)


