"""
User Story:
As a Platform Manager, I want to update service categories so that they remain relevant.
"""
from app import db
from app.entity.category import Category

class PlatformUpdateCategoryController:
    def update_category(self, category_id:int, **fields):
        c = Category.query.get(category_id)
        if not c: raise ValueError("Category not found.")
        for k in ["categoryName","description","isActive"]:
            if k in fields and fields[k] is not None: setattr(c, k, fields[k])
        db.session.commit(); return c
