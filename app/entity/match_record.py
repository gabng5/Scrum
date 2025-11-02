from app import db

class MatchRecord(db.Model):
    __tablename__ = "match_records"
    matchRecordID = db.Column(db.Integer, primary_key=True)
    requestID     = db.Column(db.Integer, db.ForeignKey("requests.requestID"), nullable=False)
    csrRepID      = db.Column(db.Integer, db.ForeignKey("user_accounts.userID"), nullable=False)
    pinID         = db.Column(db.Integer, db.ForeignKey("user_accounts.userID"), nullable=False)
    categoryID    = db.Column(db.Integer, db.ForeignKey("categories.categoryID"), nullable=False)
    status        = db.Column(db.String(30), default="completed")
