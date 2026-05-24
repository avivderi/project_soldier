"""
קובץ זה מכיל פונקציות עזר שמשמשות את שאר קבצי המערכת.
זה עוזר לנו לשמור על קוד נקי ולמנוע כפילויות (DRY).
"""

from data import soldiers_db

def find_soldier_by_id(soldier_id):
    """
    מחפשת חייל לפי מספר אישי.
    מחזירה את המילון של החייל אם נמצא, אחרת מחזירה None.
    """
    for soldier in soldiers_db:
        if soldier["id"] == soldier_id:
            return soldier
    return None

def is_valid_name(name):
    """
    בודקת האם שם החייל תקין (לא ריק).
    """
    if not name or name.strip() == "":
        return False
    return True

def is_valid_day(day):
    """
    בודקת האם היום בשבוע הוא יום חוקי לתורנות (ראשון עד חמישי).
    """
    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day in valid_days

def is_valid_status(status):
    """
    בודקת האם סטטוס התורנות חוקי.
    """
    valid_statuses = ["pending", "completed", "missed"]
    return status in valid_statuses