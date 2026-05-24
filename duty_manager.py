"""
קובץ זה אחראי על ניהול המידע שקשור לתורנויות במערכת:
הוספת תורנות לחייל, עדכון סטטוס תורנות, ושליפת תורנויות של חייל.
"""

from utils import find_soldier_by_id, is_valid_day, is_valid_status

def add_duty(soldier_id, duty_name, day):
    """
    מוסיפה תורנות חדשה לחייל.
    זורקת שגיאות אם החייל לא קיים, אם יש כבר תורנות באותו שם לחייל, או אם היום לא חוקי.
    """
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
        
    # בדיקה האם לחייל כבר יש תורנות באותו שם
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            raise ValueError(f"Duty with name '{duty_name}' already exists for this soldier.")
            
    # בדיקת חוקיות יום
    if not is_valid_day(day):
        raise ValueError(f"Invalid day: '{day}'. Must be a weekday (sunday-thursday).")
        
    # יצירת מילון לתורנות והוספתו לרשימת התורנויות של החייל
    new_duty = {
        "name": duty_name,
        "day": day,
        "status": "pending"  # תורנות חדשה תמיד נוצרת בסטטוס ממתינה
    }
    soldier["duties"].append(new_duty)

def update_duty_status(soldier_id, duty_name, new_status):
    """
    מעדכנת סטטוס של תורנות קיימת לחייל מסוים.
    זורקת שגיאות אם החייל לא קיים, אם התורנות לא קיימת, או אם הסטטוס לא חוקי.
    """
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
        
    if not is_valid_status(new_status):
        raise ValueError(f"Invalid status: '{new_status}'.")
        
    # חיפוש התורנות המבוקשת ועדכון הסטטוס שלה
    duty_found = False
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            duty["status"] = new_status
            duty_found = True
            break
            
    if not duty_found:
        raise KeyError(f"Duty with name '{duty_name}' not found for this soldier.")

def get_soldier_duties(soldier_id):
    """
    מחזירה את רשימת התורנויות של חייל מסוים.
    זורקת שגיאה אם החייל לא קיים.
    """
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
        
    return soldier["duties"]