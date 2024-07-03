from dataclasses import dataclass


@dataclass
class User:  # ci metto tutti gli attributi della tabella
    user_id: str
    votes_funny: int
    votes_useful: int
    votes_cool: int
    name: str
    average_stars: int
    review_count: int

    # è buona prassi fare subito eqauls ed hash

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)

