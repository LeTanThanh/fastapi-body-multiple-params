from fastapi import FastAPI, Path, Query

from typing import Annotated

from models.item import Item

app = FastAPI()

# Mix Path, Query and body parameters
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[
    int,
    Path(
      ge = 0,
      lt = 1_000,
      description = "The ID of the item to update"
    )
  ],
  q: Annotated[str | None, Query()] = None,
  item: Item | None = None
):
  response = {"id": id}

  if q:
    response.update({"q": q})

  if item:
    response.update({"item": item})

  return response
"""
