"""
User Story:
As a Platform Manager, I want to generate monthly reports so that I can track monthly usage.
"""
import json
from app import db
from app.entity.report import Report

class PlatformGenerateMonthlyReportController:
    def generate_monthly(self, manager_id:int, month_string:str, data_dict:dict):
        r = Report(generatedBy=manager_id, reportType="monthly", period=month_string, reportData=json.dumps(data_dict))
        db.session.add(r); db.session.commit(); return r
