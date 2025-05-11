from pydantic import BaseModel

class ContactCreate(BaseModel):
    ad: str
    soyad: str
    konu: str
    ileti: str
