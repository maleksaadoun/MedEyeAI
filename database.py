from mongoengine import Document, StringField, EmailField, IntField, ListField, EmbeddedDocumentField, EmbeddedDocument, DateTimeField
import datetime

class PredictionHistory(EmbeddedDocument):
    filename = StringField(required=True)
    prediction = StringField(required=True)
    confidence = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)
    recommendation = StringField(required=False)

class User(Document):
    meta = {'strict': False} 
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    age = IntField(required=False, min_value=0)
    gender = StringField(required=False)
    profile_picture = StringField() 
    role = StringField(required=True)
    
class Client(Document):
    meta = {'strict': False} 
    email = EmailField(required=True, unique=True)
    history = ListField(EmbeddedDocumentField(PredictionHistory), required=False)
    role = StringField(required=True)

class Admin(Document):
    meta = {'strict': False} 
    email = EmailField(required=True, unique=True)
    role = StringField(required=True)

class Recommendations(Document):
    meta = {'strict': False} 
    state = StringField(required=True)
    recommendation = StringField(required=True)

