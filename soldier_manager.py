"""
קובץ זה אחראי על ניהול המידע שקשור לחיילים במערכת:
הוספה, הסרה ושליפת רשימת החיילים.
"""

from data import soldiers_db
from utils import find_soldier_by_id, is_valid_name

def add_soldier(soldier_id, name):
    """
    מוסיפה חייל חדש למערכת.
    זורקת שגיאות אם הנתונים לא תקינים.
    """
    # בדיקה האם החייל כבר קיים
    if find_soldier_by_id(soldier_id) is not None:
        raise ValueError(f"Soldier with ID {soldier_id} already exists.")
        
    # בדיקה האם השם תקין
    if not is_valid_name(name):
        raise ValueError("Soldier name cannot be empty.")
        
    # יצירת מילון לחייל החדש והוספתו לרשימה
    new_soldier = {
        "id": soldier_id,
        "name": name,
        "duties": []
    }
    soldiers_db.append(new_soldier)

def remove_soldier(soldier_id):
    """
    מסירה חייל מהמערכת לפי מספר אישי.
    זורקת שגיאה אם החייל לא קיים.
    """
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
        
    soldiers_db.remove(soldier)

def get_all_soldiers():
    """
    מחזירה את רשימת כל החיילים במערכת.
    """
    return soldiers_db