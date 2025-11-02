"""
User Story:
As a Platform Manager, I want to generate weekly reports so that I can track weekly usage.
"""
import json
from app import db
from app.entity.report import Report

class PlatformGenerateWeeklyReportController:
    def generate_weekly(self, manager_id:int, week_string:str, data_dict:dict):
        r = Report(generatedBy=manager_id, reportType="weekly", period=week_string, reportData=json.dumps(data_dict))
        db.session.add(r); db.session.commit(); return r
