"""
User Story:
As a PIN, I want to view details of my completed service requests so that I can keep track of previous support.
"""
from app.entity.request import Request

class PinViewCompletedRequestController:
    def view_completed_request(self, pin_id:int, request_id:int):
        r = Request.query.get(request_id)
        if not r or r.pinID != pin_id or r.status != "closed":
            return None
        return r
