from app import db

class Request(db.Model):
    __tablename__ = "requests"
    requestID      = db.Column(db.Integer, primary_key=True)
    pinID          = db.Column(db.Integer, db.ForeignKey("user_accounts.userID"), nullable=False)
    csrRepID       = db.Column(db.Integer, db.ForeignKey("user_accounts.userID"))
    categoryID     = db.Column(db.Integer, db.ForeignKey("categories.categoryID"), nullable=False)
    title          = db.Column(db.String(150), nullable=False)
    description    = db.Column(db.Text)
    status         = db.Column(db.String(30), default="open")
    viewCount      = db.Column(db.Integer, default=0)
    shortlistCount = db.Column(db.Integer, default=0)
    
    category = db.relationship("Category", back_populates="requests", lazy=True)
