from app.database import Database
from typing import List
from app.models import User


class UserService:
    def __init__(self):
        self.database = Database()
        pass

    def get_users(self) -> List[User]:
        users = []
        users_dict_list = self.database.get_all_active_users()
        users = [User(**user_dict) for user_dict in users_dict_list]
        print(users)
        return users