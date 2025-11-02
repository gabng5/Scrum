"""
User Story:
As a Platform Manager, I want to suspend unused service categories so that invalid service categories are no longer used.
"""
from app import db
from app.entity.category import Category

class PlatformSuspendCategoryController:
    def suspend_category(self, category_id:int):
        c = Category.query.get(category_id)
        if not c: raise ValueError("Category not found.")
        c.isActive = False; db.session.commit(); return c
