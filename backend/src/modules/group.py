class Group:
    def __init__(self, title):
        self.title = title
        self.members = []
        self.messages = []

    def fetch_from_db(self, id, title, members, messages):
        self.id = id
        self.__init__(title=title)
        self._set_members(members=members)
        self._set_messages(messages=messages)

    def _set_members(self, members):
        self.members = members

    def _set_messages(self, messages):
        self.messages = messages
