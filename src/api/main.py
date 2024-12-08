from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI, Header
from pydantic import BaseModel

from src.api.dependencies.model import get_command_handler
from src.application.commands import BaseResponse, Command
from src.application.commands.handlers import CommandHandler

app = FastAPI()


class UserRequest(BaseModel):
    message: str


@app.post("/")
async def message(
    body: UserRequest,
    handler: Annotated[CommandHandler, Depends(get_command_handler)],
    model: str = Header(default="gpt-4o-mini"),
) -> BaseResponse:
    command = Command(user_request=body.message, model=model)
    return await handler.handle(command)


if __name__ == "__main__":
    uvicorn.run(app)
