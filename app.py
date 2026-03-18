from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import hashlib
import uvicorn

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./supply_chain.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    blockchain_hash = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String)
    status = Column(String)

Base.metadata.create_all(bind=engine)

# Seed data
def seed_data(db):
    if not db.query(Product).first():
        product1 = Product(id="1", name="Product 1", status="In Transit", blockchain_hash=hashlib.sha256(b"Product 1").hexdigest())
        product2 = Product(id="2", name="Product 2", status="Delivered", blockchain_hash=hashlib.sha256(b"Product 2").hexdigest())
        db.add(product1)
        db.add(product2)
        db.commit()

# Pydantic models
class ProductCreate(BaseModel):
    name: str
    status: str

class UserLogin(BaseModel):
    username: str
    password: str

# Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/products", response_class=HTMLResponse)
async def read_products_page(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})

@app.get("/track", response_class=HTMLResponse)
async def read_track_page(request: Request):
    return templates.TemplateResponse("track.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def read_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/api/products", response_model=List[ProductCreate])
async def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/api/products", response_model=ProductCreate)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(id=str(len(db.query(Product).all()) + 1), name=product.name, status=product.status, blockchain_hash=hashlib.sha256(product.name.encode()).hexdigest())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/api/products/{product_id}", response_model=ProductCreate)
async def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/api/track/{product_id}", response_model=ProductCreate)
async def track_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/api/auth/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user is None or db_user.password_hash != hashlib.sha256(user.password.encode()).hexdigest():
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"token": "fake-jwt-token"}

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    uvicorn.run(app, host="0.0.0.0", port=8000)
