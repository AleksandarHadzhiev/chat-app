from src.messages.repositories.factory import RepositoryFactory


class MessagesService:
    def __init__(self, db, settings):
        self.settings = settings
        self.rep = RepositoryFactory(db=db).get_db()

    def get_all(self, group_id):
        return self.rep.get_all(group_id)

    def create(self, data):
        self.rep.create(data=data)


    def edit(self, data):
        if "content" not in data or "code" not in data:
            print("MISSING DATA")
            return {"fail": "Missing data"}
        elif data["content"] == "" or data["content"] is None or data["code"] is None or data["code"] == "":
            print("INCORRECT FORMAT")
            return {"fail": "Incorrect format"}
        return self.rep.edit(data=data)


    def delete(self, code):

        if (type(code) is str and code is not None):
            return self.rep.delete(code=code)
        return {"fail": "Incorrect code"}
