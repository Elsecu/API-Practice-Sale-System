from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import database, models
from schemas import ClientCreate, ClientUpdate, ClientResponse

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

@router.get("/", response_model=list[ClientResponse], status_code=201)
def get_clients(skip: int=0, limit: int=10,db:Session = Depends(database.get_db)):
    get_client = db.query(models.ClientModel).offset(skip).limit(limit).all()
    
    if not get_client:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )
    return get_client

@router.post("/", response_model=ClientCreate,status_code=201)
def create_clients(client: ClientCreate, db: Session = Depends(database.get_db)):
    new_client = models.ClientModel(name= client.name, email= client.email, edad= client.edad)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

@router.delete("/{client_id}", status_code=204)
def delete_clients(id: int, db:Session = Depends(database.get_db)):
    delete_client = db.query(models.ClientModel).filter(models.ClientModel.id == id).first()
    
    if not delete_client:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )
    db.delete(delete_client)
    db.commit()