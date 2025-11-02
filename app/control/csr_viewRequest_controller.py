"""
User Story:
As a CSR Rep, I want to view the details of a service request so that I can understand the PIN’s needs.
"""
from app import db
from app.entity.request import Request

class CsrViewRequestController:
    def view_request(self, request_id:int):
        r = Request.query.get(request_id)
        if not r: raise ValueError("Request not found.")
        r.viewCount = (r.viewCount or 0) + 1
        db.session.commit(); return r
