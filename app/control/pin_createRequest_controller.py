"""
User Story:
As a PIN, I want to create a service request (e.g. transportation, wheelchair) so that I can get assistance.
"""
from app import db
from app.entity.request import Request
from app.entity.category import Category

class PinCreateRequestController:
    def create_request(self, pin_id:int, category_name:str, title:str, description:str):
        c = Category.query.filter_by(categoryName=category_name, isActive=True).first()
        if not c: raise ValueError("Category not found or inactive.")
        r = Request(pinID=pin_id, categoryID=c.categoryID, title=title, description=description, status="open")
        db.session.add(r); db.session.commit(); return r
