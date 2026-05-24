def add_soldier(soldier_id, name):
    """
    מוסיפה חייל חדש למערכת.
    
    קלט:
    soldier_id: מספר אישי של החייל
    name: שם החייל
    
    פלט: None
    
    זורקת ValueError אם ה-id כבר קיים במערכת או אם השם (name) ריק.
    """
    pass

def remove_soldier(soldier_id):
    """
    מסירה חייל מהמערכת.
    
    קלט:
    soldier_id: מספר אישי של החייל להסרה
    
    פלט: None
    
    זורקת KeyError אם החייל לא קיים במערכת.
    """
    pass

def get_all_soldiers():
    """
    שולפת את רשימת כל החיילים הרשומים במערכת.
    
    קלט: אין
    
    פלט: רשימה (list) של כל החיילים.
    """
    pass

def add_duty(soldier_id, duty_name, day):
    """
    משבצת חייל לתורנות מסוימת.
    
    קלט:
    soldier_id: מספר אישי של החייל
    duty_name: שם התורנות
    day: יום בשבוע (לדוגמה: 'sunday')
    
    פלט: None
    
    זורקת KeyError אם החייל לא קיים במערכת.
    זורקת ValueError אם יש כפילות בשם התורנות לחייל זה, או אם היום אינו חוקי (שישי/שבת או פורמט שגוי).
    """
    pass

def update_duty_status(soldier_id, duty_name, new_status):
    """
    מעדכנת סטטוס של תורנות קיימת לחייל.
    
    קלט:
    soldier_id: מספר אישי של החייל
    duty_name: שם התורנות
    new_status: הסטטוס החדש ('pending', 'completed', 'missed')
    
    פלט: None
    
    זורקת KeyError אם החייל לא קיים או אם התורנות לא נמצאה אצל החייל.
    זורקת ValueError אם הסטטוס החדש אינו חוקי.
    """
    pass

def get_soldier_duties(soldier_id):
    """
    מציגה את כל התורנויות שמשובצות לחייל מסוים.
    
    קלט:
    soldier_id: מספר אישי של החייל
    
    פלט: רשימה (list) של התורנויות של החייל.
    
    זורקת KeyError אם החייל לא קיים במערכת.
    """
    pass

def find_soldier_by_id(soldier_id):
    """
    פונקציית עזר: מחפשת חייל לפי מספרו האישי.
    
    קלט:
    soldier_id: מספר אישי של החייל
    
    פלט: מילון (dict) עם פרטי החייל, או None אם החייל לא נמצא.
    """
    pass