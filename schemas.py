from typing import List, Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True



class User(BaseModel):
    name: str
    email: str
    password: str


# if i remove below code then the user password will show
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        from_attributes = True
        
# class ShowBlog(BaseModel):
#     title: str
#     body: str
#     creator: ShowUser

#     class Config:
#         from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser] = None  # Mark as optional

    class Config:
        from_attributes = True

class Login(BaseModel):
    Username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokeData(BaseModel):
    email: Optional[str] = None
   
