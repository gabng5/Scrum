"""
User Story:
As a CSR Rep, I want to search my shortlisted service requests so that I can quickly find saved opportunities.
"""
from app.entity.shortlist import Shortlist

class CsrSearchShortlistController:
    def search_shortlist(self, csr_id:int, request_id:int=None):
        q = Shortlist.query.filter_by(csrRepID=csr_id)
        if request_id: q = q.filter_by(requestID=request_id)
        return q.all()
