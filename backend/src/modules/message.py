from datetime import datetime


class Message:
    def __init__(self, author, user_id, content, group_id):
        self.author = author
        self.user_id = user_id
        self.content = content
        self.group_id = group_id
        self.date_sent = datetime.now()

    def fetch_from_db(self, id, author, user_id, content, group_id, date_sent):
        self.id = id
        self.author = author
        self.user_id = user_id
        self.content = content
        self.group_id = group_id
        self.date_sent = date_sent
