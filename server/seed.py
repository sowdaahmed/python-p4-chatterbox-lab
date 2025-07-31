from config import app, db
from models import Message
from datetime import datetime

with app.app_context():
    print("Seeding database...")

    Message.query.delete()

    messages = [
        Message(username="Duane", body="Hello from Duane!"),
        Message(username="Zoe", body="What's up!"),
        Message(username="Ayan", body="Flask is awesome 💻"),
    ]

    db.session.bulk_save_objects(messages)
    db.session.commit()

    print("Seeding complete!")
