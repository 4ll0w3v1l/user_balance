from fastapi import APIRouter, Request
from schemas.users import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create_user(user: User, request: Request):
    if request.app.state.db:
        last_id = next(reversed(request.app.state.db))
        request.app.state.db[last_id + 1] = user.model_dump()
    else:
        request.app.state.db[0] = user.model_dump()

    return user

@router.get("/", response_model=dict[str, User])
def get_users(request: Request):
    if request.app.state.db:
        return request.app.state.db
    else:
        return []
