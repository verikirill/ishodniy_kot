from sqlalchemy import Column, Integer, Float, String, Boolean, Text, JSON, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__: str = 'users'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    tg_id: Column(Integer, unique=True, nullable=True)
    username: Column = Column(String)
    folders = relationship('Folder', back_populates='user')


class Folder(Base):
    __tablename__: str = 'folders'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Column = Column(Integer, ForeignKey('users'), nullable=False)
    name: Column = Column(String, nullable=False)
    emoji: Column = Column(String)
    notes = relationship('Note', back_populates='folder')


class Note(Base):
    __tablename__: str = 'notes'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    folder_id: Column = Column(Integer, ForeignKey('folders'), nullable=False)
    name: Column = Column(String)
    content: Column = Column(Text)
