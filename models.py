from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

class NoteClient(Base):
    __tablename__ = "note_clients"
    
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey("notes.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    created_at = Column(DateTime, default=datetime.now)