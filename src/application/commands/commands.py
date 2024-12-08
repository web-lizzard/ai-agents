from pydantic import BaseModel


class Command(BaseModel):
    user_request: str
    model: str


class BaseResponse(BaseModel):
    assistant_message: str
