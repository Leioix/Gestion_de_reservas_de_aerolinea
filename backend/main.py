from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import uuid
from sqlalchemy.orm import Session
from database import SessionLocal, Vuelo, Reserva

app = FastAPI()

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Bienvenido al sistema de gestión de reservas aéreas"}

# Modelos de entrada
class FlightInput(BaseModel):
    origin: str
    destination: str
    date: str
    price: float

class BookingInput(BaseModel):
    flight_id: str
    user: str

# Rutas API
@app.get("/flights", response_model=List[FlightInput])
def get_flights(db: Session = Depends(get_db)):
    return db.query(Vuelo).all()

@app.post("/flights")
def add_flight(flight: FlightInput, db: Session = Depends(get_db)):
    new_flight = Vuelo(
        id=str(uuid.uuid4()), origin=flight.origin,
        destination=flight.destination, date=flight.date, price=flight.price
    )
    db.add(new_flight)
    db.commit()
    return {"message": "Vuelo agregado correctamente"}

@app.post("/bookings")
def book_flight(booking: BookingInput, db: Session = Depends(get_db)):
    flight = db.query(Vuelo).filter(Vuelo.id == booking.flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")

    new_booking = Reserva(id=str(uuid.uuid4()), usuario=booking.user, vuelo_id=booking.flight_id)
    db.add(new_booking)
    db.commit()
    return {"message": "Reserva creada", "booking": new_booking}

@app.get("/bookings", response_model=List[BookingInput])
def get_user_bookings(user: str, db: Session = Depends(get_db)):
    return db.query(Reserva).filter(Reserva.usuario == user).all()

@app.delete("/bookings/{booking_id}")
def cancel_booking(booking_id: str, db: Session = Depends(get_db)):
    booking = db.query(Reserva).filter(Reserva.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    db.delete(booking)
    db.commit()
    return {"message": "Reserva cancelada"}

