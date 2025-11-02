"""
User Story:
As a PIN, I want to delete my service requests so that I can stop receiving offers I do not need.
(Soft delete implemented by marking status='closed'.)
"""
from app import db
from app.entity.request import Request

class PinDeleteRequestController:
    def close_request(self, request_id:int):
        r = Request.query.get(request_id)
        if not r: raise ValueError("Request not found.")
        r.status = "closed"; db.session.commit(); return r
