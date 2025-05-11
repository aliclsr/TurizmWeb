from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(
    prefix="/iletisim",
    tags=["İletişim"]
)

# DB oturumu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@router.post("/gonder")
def mesaj_gonder(
    ad: str = Form(...),
    soyad: str = Form(...),
    konu: str = Form(...),
    ileti: str = Form(...),
    db: Session = Depends(get_db)
):
    yeni = models.ContactMessage(ad=ad, soyad=soyad, konu=konu, ileti=ileti)
    db.add(yeni)
    db.commit()
    return RedirectResponse(url="/contact?success=true", status_code=303)
