import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter

from typing import Final
from typing import Dict
from typing import Optional
from app.bp.create_users_usecase import UserCreator

from app.models.user import User



router = APIRouter()

CREATE_USER_ERROR_MESSAGE: Final = "ERROR IN create_user ENDPOINT"
CREATE_USER_ENDPOINT_SUMMARY: Final = "Create a new User"
CREATE_USER_ENDPOINT_PATH: Final = "/create_user"
SUCCESS_KEY: Final = "success"


class CreateUserInput(BaseModel):
    id: int = Field(...)
    username: str = Field(default="Example")
    email: str = Field(default="example@email.com")
    is_active: bool = Field(default=True)
    created_at: Optional[str] = Field()
    updated_at: Optional[str] = Field()
    


@router.post(
    path=CREATE_USER_ENDPOINT_PATH,
    response_model=Dict[str, bool],
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def create_user(new_user_data: CreateUserInput):
    success = False
    try:
        user_creator = UserCreator()
        success = user_creator.run(
            User(
                id=new_user_data.id,
                username=new_user_data.username,
                email=new_user_data.email,
                is_active=new_user_data.is_active,
                created_at=new_user_data.created_at,
                updated_at=new_user_data.updated_at,
            )
        )
    except Exception as error:
        logging.error(CREATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success}
