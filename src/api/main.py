from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI

from src.api.dependencies import get_model
from src.domain.ports import LanguageModel

app = FastAPI()


@app.post('/')
async def message(
    model: Annotated[LanguageModel, Depends(get_model)]
):
    print(model)
    return {'healthy': True}


if __name__ == "__main__":
    uvicorn.run(app)