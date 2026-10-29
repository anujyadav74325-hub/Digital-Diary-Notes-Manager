import os

FILE_NAME = "diary.txt"


def load_notes():
    """Load all notes from diary.txt."""
    notes = []
    if not os.path.exists(FILE_NAME):
        return notes
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split("|", 1)
                if len(parts) == 2:
                    notes.append((parts[0].strip(), parts[1].strip()))
    return notes


def save_notes(notes):
    """Save all notes back to diary.txt."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for date_str, text in notes:
            file.write(f"{date_str}|{text}\n")


def is_valid_date(date_str):
    """Validate that the date matches YYYY-MM-DD format."""
    date_str = date_str.strip()
    if len(date_str) != 10 or date_str[4] != "-" or date_str[7] != "-":
        return False
    year, month, day = date_str[:4], date_str[5:7], date_str[8:10]
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    m, d = int(month), int(day)
    if not (1 <= m <= 12 and 1 <= d <= 31):
        return False
    return True


def add_note():
    """Option 1: Add a dated note."""
    date_str = input("Date: ").strip()
    if not is_valid_date(date_str):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    text = input("Text: ").strip()
    if text == "":
        print("Note text cannot be empty.")
        return

    notes = load_notes()
    notes.append((date_str, text))
    save_notes(notes)

    note_num = len(notes)
    print("Note saved.")
    print(f"{note_num} | {date_str} | {text}")


def view_notes():
    """Option 2: View all saved notes."""
    notes = load_notes()
    if not notes:
        print("No notes found. Your diary is empty.")
        return

    for idx, (date_str, text) in enumerate(notes, start=1):
        print(f"{idx} | {date_str} | {text}")


def search_notes():
    """Option 3: Search notes by keyword using lower, strip, and find."""
    keyword = input("Search: ").strip().lower()
    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    notes = load_notes()
    matches = []
    for idx, (date_str, text) in enumerate(notes, start=1):
        if text.lower().find(keyword) != -1:
            matches.append((idx, date_str, text))

    if not matches:
        print("No matching notes found.")
    else:
        print(f"Found {len(matches)} notes:")
        for idx, date_str, text in matches:
            print(f"{idx} | {date_str} | {text}")


def delete_note():
    """Option 4: Delete a note by its note number."""
    num_str = input("Delete note number: ").strip()
    if not num_str.isdigit():
        print("Invalid note number.")
        return

    note_num = int(num_str)
    notes = load_notes()

    if note_num < 1 or note_num > len(notes):
        print(f"Note number {note_num} not found.")
        return

    notes.pop(note_num - 1)
    save_notes(notes)
    print(f"Note {note_num} deleted. Notes left: {len(notes)}")


def main():
    while True:
        print("\nMenu: 1 Add, 2 View all, 3 Search, 4 Delete, 5 Exit")
        choice = input("Select menu option: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()