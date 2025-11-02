"""
User Story:
As a PIN, I want to update my service requests so that I can change details if necessary.
"""
from app import db
from app.entity.request import Request

class PinUpdateRequestController:
    def update_request(self, request_id:int, **fields):
        r = Request.query.get(request_id)
        if not r: raise ValueError("Request not found.")
        for k in ["title","description","status","csrRepID","categoryID"]:
            if k in fields and fields[k] is not None: setattr(r, k, fields[k])
        db.session.commit(); return r
