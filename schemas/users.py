from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    balance: int

class UserTransfer(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: int

class UserTransferResponse(BaseModel):
    success: bool