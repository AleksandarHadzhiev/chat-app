from src.messages.repositories.factory import RepositoryFactory


class MessagesService:
    def __init__(self, db, settings):
        self.settings = settings
        self.rep = RepositoryFactory(db=db).get_db()

    def get_all(self, group_id):
        # Add proper check for group_id
        return self.rep.get_all(group_id)

    def create(self, data):
        print("function")
        # Add checks for the incoming data
        self.rep.create(data=data)
