from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Enterprise IT service desk "}
db={
    1:{"id":1,"title":"Laptop not working"
       ,"description":"power button not working",
       "category":"hardware","status":"new"},
    2:{"id":2,"title":"internet not working"
       ,"description":"wifi problem",
       "category":"hardware","status":"new"},
}
#Schems
class TicketCreate(BaseModel):
    title: str
    description: str
    category: str
    status: str
class TicketResponse(TicketCreate):
    id: int
#APIs
@app.get("/tickets")
def ticket_read_all():
    return list(db.values())
    #to open in server  http://127.0.0.1:8000/tickets
    #to open swagger http://127.0.0.1:8000/docs
    #swagger is execution and documentation tool for fastapi
@app.get("/tickets/{id}")
def ticket_read_by_id(id: int):
    if id not in db:
        raise HTTPException(detail="Ticket not found", status_code=404)
    return db[id]
@app.post("/tickets",status_code=201,response_model=TicketResponse)
def ticket_create(ticket_payload: TicketCreate):
    new_id = max(db.keys(),default=0) + 1
    db[new_id] = {"id": new_id, **ticket_payload.model_dump()}
    return db[new_id]
@app.put("/tickets/{id}",response_model=TicketResponse)
def ticket_update(id: int, ticket_payload: TicketCreate):
    if id not in db:
        raise HTTPException(detail="Ticket not found", status_code=404)
    db[id]= {"id": id, **ticket_payload.model_dump()}
    return db[id]
@app.delete("/tickets/{id}")
def ticket_delete(id: int):
    if id not in db:
        raise HTTPException(detail="Ticket not found", status_code=404)
    del db[id]
    return {"message": "Ticket deleted successfully"}