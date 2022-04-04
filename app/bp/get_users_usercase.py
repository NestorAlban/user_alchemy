from app.services.user_service import UserService
from typing import List
from app.models import User


class UserGetter:
    def __init__(self):
        pass

    def run(self) -> List[User]:
        users = []
        user_service = UserService()
        print("=====================================================")
        users = user_service.get_users()
        print(users, "2")
        print("=====================================================")
        return users