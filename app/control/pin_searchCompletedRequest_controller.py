"""
User Story:
As a PIN, I want to search the history of completed service requests so that I can filter by service and date.
(Simplified to filter by category for now.)
"""
from app.entity.request import Request

class PinSearchCompletedRequestController:
    def search_completed_requests(self, pin_id:int, category_id:int=None):
        q = Request.query.filter_by(pinID=pin_id, status="closed")
        if category_id: q = q.filter_by(categoryID=category_id)
        return q.order_by(Request.requestID.desc()).all()
