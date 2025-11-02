"""
User Story:
As a Platform Manager, I want to search service categories by name so that I can quickly find a specific category.
"""
from app.entity.category import Category

class PlatformSearchCategoryController:
    def search_category(self, name_keyword:str):
        like = f"%{name_keyword or ''}%"
        return Category.query.filter(Category.categoryName.ilike(like)).order_by(Category.categoryName).all()
