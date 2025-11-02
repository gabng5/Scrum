"""
User Story:
As a CSR Rep, I want to search my history of service requests so that I can review past opportunities my organization has supported.
"""
from app.entity.match_record import MatchRecord

class CsrSearchMatchRecordController:
    def search_match_records(self, csr_id:int, status:str=None):
        q = MatchRecord.query.filter_by(csrRepID=csr_id)
        if status: q = q.filter_by(status=status)
        return q.all()
