from fastapi import APIRouter, Request
from schemas.users import UserTransfer

router = APIRouter(prefix="/transfer", tags=["transfers"])

@router.post("/")
def transfer(request: Request, t:UserTransfer):
    db = request.app.state.db

    if db and t.from_user_id in db and t.to_user_id in db and t.from_user_id != t.to_user_id:
        if db[t.from_user_id]['balance'] - t.amount >= 0:
            db[t.from_user_id]['balance'] -= t.amount
            db[t.to_user_id]['balance'] += t.amount
            return 0

    return 1
