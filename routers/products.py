from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import database, models
from schemas import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

#Products
@router.post("/", response_model=ProductCreate, status_code=201)
def create_products(product:ProductCreate, db:Session = Depends(database.get_db)):
    new_product = models.ProductModel(product=product.product, unit=product.unit)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return(new_product)

@router.get("/", response_model=list[ProductResponse], status_code=201)
def get_products(skip: int=0, limit: int = 10, db: Session = Depends(database.get_db)):
    get_product = db.query(models.ProductModel).offset(skip).limit(limit).all()

    if not get_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return get_product

@router.delete("/{product_id}", status_code=204)
def delete_products(id: int, db:Session = Depends(database.get_db)):
    delete_product = db.query(models.ProductModel).filter(models.ProductModel.id == id).first()

    if not delete_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    db.delete(delete_product)
    db.commit()