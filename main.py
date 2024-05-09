from fastapi import FastAPI, Path, Query, Body

from typing import Annotated

from models.item import Item
from models.user import User

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

# Multiple body parameters
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Item,
  user: User
):
  response = {"id": id, "item": item, "user": user}

  return response
"""

# Singular values in body
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Item,
  user: User,
  importance: Annotated[int, Body()]
):
  response = {"id": id, "item": item, "user": user, "importance": importance}

  return response
"""

# Multiple body params and query
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Item,
  user: User,
  importance: Annotated[int, Body(gt = 0)],
  q: str | None = None
):
  response = {"id": id, "item": item, "user": user, "importance": importance}

  return response
"""

# Embed a single body parameter
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body(embed = True)]
):
  response = {"id": id, "item": item}

  return response
