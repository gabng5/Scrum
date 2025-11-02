"""
CsrRemoveShortlistController
Removes a service request from a CSR Representative's shortlist.
ADDITIONAL FEATURE
"""

from app import db
from app.entity.shortlist import Shortlist
from app.entity.request import Request


class CsrRemoveShortlistController:
    def remove_from_shortlist(self, csrRepID: int, requestID: int):
        """
        Removes a record from Shortlist table for the given CSR Rep and Request.
        Args:
            csrRepID (int): The ID of the CSR Representative (current_user.userID)
            requestID (int): The ID of the Request to remove
        Returns:
            bool: True if removed successfully, False if no record found
        """
        record = Shortlist.query.filter_by(csrRepID=csrRepID, requestID=requestID).first()

        if not record:
            raise ValueError("Shortlist entry not found.")

        try:
            db.session.delete(record)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Failed to remove from shortlist: {e}")
