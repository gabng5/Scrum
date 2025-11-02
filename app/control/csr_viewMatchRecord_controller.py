"""
User Story:
As a CSR Rep, I want to view the history of services by service type and date so that I can track contributions.
(Extend with date filters later.)
"""
from app.entity.match_record import MatchRecord

class CsrViewMatchRecordController:
    def view_match_records(self, csr_id:int):
        return MatchRecord.query.filter_by(csrRepID=csr_id).all()
