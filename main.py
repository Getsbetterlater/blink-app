from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from models import Note, Client, NoteClient
from ai import extract_client_names
from models import Base
from database import engine

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Blink app is running"}

@app.post("/notes")
def create_note(content: str):
    db = SessionLocal()
    
    # Save the note
    note = Note(content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    
    # Extract client names using AI
    names = extract_client_names(content)
    
    detected_clients = []
    for name in names:
        # Check if client already exists
        client = db.query(Client).filter(Client.name == name).first()
        if not client:
            # Create new client
            client = Client(name=name)
            db.add(client)
            db.commit()
            db.refresh(client)
        
        # Link note to client
        note_client = NoteClient(note_id=note.id, client_id=client.id)
        db.add(note_client)
        detected_clients.append(name)
    
    db.commit()
    
    # Get the data before closing
    result = {
        "id": note.id,
        "content": note.content,
        "detected_clients": detected_clients
    }
    
    db.close()
    
    return result

@app.get("/search")
def search_notes(client_name: str):
    db = SessionLocal()
    
    # Find the client
    client = db.query(Client).filter(Client.name.ilike(f"%{client_name}%")).first()
    
    if not client:
        db.close()
        return {"notes": [], "message": "No client found with that name"}
    
    # Find all notes linked to this client
    note_links = db.query(NoteClient).filter(NoteClient.client_id == client.id).all()
    
    notes = []
    for link in note_links:
        note = db.query(Note).filter(Note.id == link.note_id).first()
        if note:
            notes.append({
                "id": note.id,
                "content": note.content,
                "created_at": str(note.created_at)
            })
    
    db.close()
    
    return {"client": client.name, "notes": notes}