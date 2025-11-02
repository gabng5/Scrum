"""
User Story:
As a CSR Rep, I want to view my shortlisted service requests so that I can assess which opportunities are most suitable to support.
"""
from app.entity.shortlist import Shortlist

class CsrViewShortlistController:
    def view_shortlist(self, csr_id:int):
        return Shortlist.query.filter_by(csrRepID=csr_id).all()
