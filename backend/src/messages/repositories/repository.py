class Repository:
    def __init__(self, db):
        pass

    def create(self, data):
        pass

    def get_all(self, group_id):
        pass

    def edit(self, data):
        pass

    async def is_part_of_group(self, user_id, group_id):
        pass

    async def is_author(self, user_id, code):
        pass

    def delete(self, code, group_id, user_id):
        pass

    def get_last_message(self, group_id):
        pass
