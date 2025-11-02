from app import db

class Report(db.Model):
    __tablename__ = "reports"
    reportID    = db.Column(db.Integer, primary_key=True)
    reportType  = db.Column(db.String(50), nullable=False)
    generatedBy = db.Column(db.Integer, db.ForeignKey("user_accounts.userID"), nullable=False)
    reportData  = db.Column(db.Text)
    period      = db.Column(db.String(50))
