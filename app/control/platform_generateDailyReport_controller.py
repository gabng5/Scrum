"""
User Story:
As a Platform Manager, I want to generate daily reports so that I can track daily usage.
"""
import json
from app import db
from app.entity.report import Report

class PlatformGenerateDailyReportController:
    def generate_daily(self, manager_id:int, day_string:str, data_dict:dict):
        r = Report(generatedBy=manager_id, reportType="daily", period=day_string, reportData=json.dumps(data_dict))
        db.session.add(r); db.session.commit(); return r
