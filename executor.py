from jina import Executor, DocumentArray, requests


class ResponseSlimmer(Executor):
    def __init__(self, docs_fields_to_pop=None, matches_fields_to_pop=None, **kwargs):
        super().__init__(**kwargs)
        self.docs_fields_to_pop = docs_fields_to_pop
        self.matches_fields_to_pop = matches_fields_to_pop

    @requests(on='/search')
    def format(self, docs: DocumentArray, **kwargs):
        if self.docs_fields_to_pop:
            for doc in docs:
                doc.pop(self.docs_fields_to_pop)
                for match in doc.matches:
                    match.pop(self.matches_fields_to_pop)
