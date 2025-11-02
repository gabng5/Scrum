"""
User Story:
As a CSR Rep, I want to search for service requests so that I can find opportunities that match my organization’s resources.
"""
from app.entity.request import Request
from app.entity.category import Category

class CsrSearchRequestController:
    def search_requests(self, category_name=None, status=None):
        q = Request.query
        if category_name:
            q = q.join(Category, Request.categoryID == Category.categoryID).filter(Category.categoryName.ilike(f"%{category_name}%"))
        if status:
            q = q.filter(Request.status == status)
        return q.order_by(Request.requestID.desc()).all()
