import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional

from typing import Final

from app.bp import UserGetter

from app.models import User


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Show active Users"
USERS_ENDPOINT_PATH: Final = "/users"

class GetUsersResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[str] = Field()
    created_at: Optional[str] = Field()
    updated_at: Optional[str] = Field()

@router.get(
    path=USERS_ENDPOINT_PATH,
    response_model=List[GetUsersResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_users():
    users_response = []
    try:
        user_getter = UserGetter()
        print("=====================================================")
        users = user_getter.run()
        print(users, "1")
        print("=====================================================")
        users_response = [User(user) for user in users]
        # users_response = [GetUsersResponse(
        #     id=user.id,
        #     name=user.name,
        #     email=user.email,
        #     is_active=user.is_active,
        #     created_at=user.created_at,
        #     updated_at=user.updated_at
        # ) for user in users]
    except Exception as error:
        print(GET_USER_ERROR_MESSAGE, error)
    return users_response