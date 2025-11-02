"""
User Story:
As a CSR Rep, I want to save service requests so that I can view it later.
"""
from app import db
from app.entity.request import Request
from app.entity.shortlist import Shortlist

class CsrAddShortlistController:
    def add_to_shortlist(self, csr_id:int, request_id:int):
        r = Request.query.get(request_id)
        if not r: raise ValueError("Request not found.")
        r.shortlistCount = (r.shortlistCount or 0) + 1
        s = Shortlist(csrRepID=csr_id, requestID=request_id)
        db.session.add(s); db.session.commit(); return s
