from dataclasses import dataclass

from database.review import Review


@dataclass
class Business:
    business_id: str
    full_address: str
    active: str
    categories: str
    city: str
    review_count: int
    business_name: str
    neighborhoods: str
    latitude: float
    longitude: float
    state: str
    stars: float

    # un business può avere più review, quindi può avere una collection
    reviews_id: list[str]
    reviews: list[Review] = None

    def __eq__(self, other):
        return self.business_id == other.business_id

    def __hash__(self):
        return hash(self.business_id)

    def get_reviews(self):  # se le reviews già ci sono restituiscimele, se non ci sono valle a chiedere al DAO
        """
        questa è quella che si chiama lazy initialitazion, ovvero lo inizializzo solo quando mi serve, quindi
        quando lo costruisco è vuoto e lo creo quando mi serve
        """

        if self.reviews is None:
            # vado a leggerle dal DAO e popolo la lista
            # dao.get_review(self.reviews_id)
            pass
        else:
            # faccio return della lista
            return self.reviews
