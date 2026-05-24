"""
נקודת הכניסה למערכת.
קובץ זה מציג את התפריט הראשי, קולט נתונים מהמשתמש,
ותופס שגיאות (Exceptions) שנזרקות מהשכבות הפנימיות.
"""

from soldier_manager import add_soldier, remove_soldier, get_all_soldiers
from duty_manager import add_duty, update_duty_status, get_soldier_duties
from data import load_data, save_data

def handle_add_soldier():
    try:
        soldier_id = int(input("הכנס מספר אישי: "))
        name = input("הכנס שם: ")
        add_soldier(soldier_id, name)
        print("החייל נוסף בהצלחה!")
    except ValueError as e:
        print(f"Error: {e}")

def handle_remove_soldier():
    try:
        soldier_id = int(input("הכנס מספר אישי להסרה: "))
        remove_soldier(soldier_id)
        print("החייל הוסר בהצלחה!")
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid ID format. Must be a number.")

def handle_get_all_soldiers():
    soldiers = get_all_soldiers()
    if not soldiers:
        print("אין חיילים רשומים במערכת.")
        return
    
    print()
    print("--- רשימת חיילים ---")
    for s in soldiers:
        print(f"מספר אישי: {s['id']}, שם: {s['name']}")

def handle_add_duty():
    try:
        soldier_id = int(input("הכנס מספר אישי של החייל: "))
        duty_name = input("הכנס שם תורנות (למשל 'שמירה'): ")
        day = input("הכנס יום (sunday/monday/tuesday/wednesday/thursday): ")
        add_duty(soldier_id, duty_name, day)
        print("התורנות נוספה בהצלחה!")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input format.")

def handle_update_duty_status():
    try:
        soldier_id = int(input("הכנס מספר אישי של החייל: "))
        duty_name = input("הכנס את שם התורנות לעדכון: ")
        status = input("הכנס סטטוס חדש (pending/completed/missed): ")
        update_duty_status(soldier_id, duty_name, status)
        print("סטטוס התורנות עודכן בהצלחה!")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input format.")

def handle_get_soldier_duties():
    try:
        soldier_id = int(input("הכנס מספר אישי של החייל: "))
        duties = get_soldier_duties(soldier_id)
        
        if not duties:
            print("לחייל זה אין תורנויות.")
        else:
            print()
            print(f"--- תורנויות לחייל {soldier_id} ---")
            for d in duties:
                print(f"תורנות: {d['name']}, יום: {d['day']}, סטטוס: {d['status']}")
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid ID format. Must be a number.")

def main():
    # טעינת נתונים קיימים כשהתוכנית עולה
    load_data()
    
    while True:
        print()
        print("=== מערכת לניהול תורנויות חיילים ===")
        print("1. הוספת חייל חדש")
        print("2. הסרת חייל מהמערכת")
        print("3. צפייה ברשימת כל החיילים")
        print("4. הוספת תורנות לחייל")
        print("5. עדכון סטטוס תורנות")
        print("6. צפייה בתורנויות של חייל")
        print("7. יציאה")
        
        choice = input("בחר פעולה (1-7): ")
        
        if choice == '1':
            handle_add_soldier()
        elif choice == '2':
            handle_remove_soldier()
        elif choice == '3':
            handle_get_all_soldiers()
        elif choice == '4':
            handle_add_duty()
        elif choice == '5':
            handle_update_duty_status()
        elif choice == '6':
            handle_get_soldier_duties()
        elif choice == '7':
            save_choice = input("לשמור שינויים? (yes/no): ").strip().lower()
            if save_choice in ['yes', 'y']:
                save_data()
                print("הנתונים נשמרו בהצלחה.")
            print("יוצא מהמערכת... להתראות!")
            break
        else:
            print("Error: Invalid choice. Please select an option from 1 to 7.")

if __name__ == "__main__":
    main()

# git_ripo
# https://github.com/avivderi/project_soldier.git