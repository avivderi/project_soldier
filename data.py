"""
קובץ זה אחראי על אחסון הנתונים של המערכת.
הנתונים נשמרים כרשימה של מילונים, כאשר כל מילון מייצג חייל.
כולל כעת גם פונקציות לשמירה וטעינה מקובץ JSON.
"""

import json
import os

soldiers_db = []
DATA_FILE = "soldiers_data.json"

def load_data():
    """טוענת את הנתונים מהקובץ אם הוא קיים."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            loaded_data = json.load(file)
            soldiers_db.clear()
            soldiers_db.extend(loaded_data)

def save_data():
    """שומרת את הנתונים הנוכחיים לקובץ JSON."""
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(soldiers_db, file, ensure_ascii=False, indent=4)