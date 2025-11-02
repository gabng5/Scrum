"""
User Story:
As a PIN, I want to view my service requests so that I can know their status.
"""
from app.entity.request import Request

class PinViewRequestController:
    def view_requests(self, pin_id:int):
        return Request.query.filter_by(pinID=pin_id).order_by(Request.requestID.desc()).all()
