from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI, Header
from pydantic import BaseModel  # ignore no-any-unimported

from src.api.dependencies import get_model
from src.domain.ports import LanguageModel
from src.logger import logger

app = FastAPI()


class UserRequest(BaseModel):
    message: str


@app.post("/")
async def message(
    body: UserRequest,
    language_model: Annotated[LanguageModel, Depends(get_model)],
    model: str = Header(default="gpt-4o-mini"),
) -> dict:
    logger.debug(body.message)
    logger.error(model)
    return {"healthy": True}


if __name__ == "__main__":
    uvicorn.run(app)
