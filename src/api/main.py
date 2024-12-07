from typing import Annotated

import uvicorn
from fastapi import FastAPI

from api.dependencies import get_model
from domain.ports import LanguageModel

app = FastAPI()


@app.post('/')
async def message(
    model: Annotated[LanguageModel, get_model()]
):
    print(model)
    return {'healthy': True}


if __name__ == "__main__":
    uvicorn.run(app)