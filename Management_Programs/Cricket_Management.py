import datetime

FILE_NAME = "players.txt"


# -----------------------------
# File Handling
# -----------------------------

def load_data():
    """Load player data from file."""
    players = []
    try:
        file = open(FILE_NAME, "r")
    except FileNotFoundError:
        return players

    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        player = {
            "id": parts[0],
            "name": parts[1],
            "role": parts[2],
            "runs": int(parts[3]),
            "wickets": int(parts[4]),
            "present_days": int(parts[5])
        }
        players.append(player)

    file.close()
    return players


def save_data(players):
    """Save player data to file."""
    file = open(FILE_NAME, "w")
    for p in players:
        line = p["id"] + "," + p["name"] + "," + p["role"] + "," + str(p["runs"]) + "," + str(p["wickets"]) + "," + str(p["present_days"])
        file.write(line + "\n")
    file.close()
    print("Data saved successfully.")

def get_lock_password():  # This function prompts the user to enter password.
    user_password = "91173088"
    entered_password = input("Enter password:")
    if user_password == entered_password:
        return True
    else:
        return False


# -----------------------------
# Date & Time
# -----------------------------

def get_today():
    """Return today's date."""
    today = datetime.date.today()
    return today.strftime("%d-%m-%Y")


def get_current_time():
    """Return current time."""
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


# -----------------------------
# Player Management
# -----------------------------

def generate_player_id(players):
    """Generate a unique player ID."""
    number = len(players) + 1
    return "P" + str(number)


def add_player(players):
    """Add a new player."""
    name = input("Enter player name: ").capitalize()
    role = input("Enter player role: ").capitalize()

    player = {
        "id": generate_player_id(players),
        "name": name,
        "role": role,
        "runs": 0,
        "wickets": 0,
        "present_days": 0
    }
    players.append(player)
    print("Player added with ID:", player["id"])


def view_players(players):
    """Display all players."""
    print("-"*30)
    if len(players) == 0:
        print("No players found.")
        return

    for i,p in enumerate(players):
        print(f"{i+1}. ID: {p["id"]}\n   Name:{p["name"]}\n   Role: {p["role"]}\n   Runs: {p["runs"]}\n   Wickets: {p["wickets"]}")
        print("-"*30)


def search_player(players):
    """Search a player by ID or name."""
    keyword = input("Enter player ID or name: ")
    found = False

    for p in players:
        if p["id"] == keyword or p["name"] == keyword:
            print("ID:", p["id"])
            print("Name:", p["name"])
            print("Role:", p["role"])
            print("Runs:", p["runs"])
            print("Wickets:", p["wickets"])
            print("Present Days:", p["present_days"])
            found = True

    if not found:
        print("Player not found.")


def update_player(players):
    """Update player details."""
    player_id = input("Enter player ID to update: ")

    for p in players:
        if p["id"] == player_id:
            p["name"] = input("Enter new name: ").capitalize()
            p["role"] = input("Enter new role: ").capitalize()
            print("Player updated.")
            return

    print("Player not found.")


def delete_player(players):
    """Delete a player."""
    player_id = input("Enter player ID to delete: ")

    for p in players:
        if p["id"] == player_id:
            players.remove(p)
            print("Player deleted.")
            return

    print("Player not found.")


# -----------------------------
# Attendance
# -----------------------------

def mark_attendance(players):
    """Mark today's attendance."""
    if len(players) == 0:
        print("No players found.")
        return

    for p in players:
        answer = input("Is " + p["name"] + " present today? (y/n): ")
        if answer == "y":
            p["present_days"] = p["present_days"] + 1

    print("Attendance marked for", get_today())


# -----------------------------
# Match Performance
# -----------------------------

def add_match_performance(players):
    """Add today's match statistics."""
    player_id = input("Enter player ID: ")

    for p in players:
        if p["id"] == player_id:
            runs = int(input("Runs scored today: "))
            wickets = int(input("Wickets taken today: "))
            p["runs"] = p["runs"] + runs
            p["wickets"] = p["wickets"] + wickets
            print("Performance added for", p["name"])
            return

    print("Player not found.")


# -----------------------------
# Main Program
# -----------------------------

def main():

    players = load_data()

    while True:

        print("\n===== Cricket Management System =====")
        print("1. Add Player")
        print("2. View Players")
        print("3. Search Player")
        print("4. Update Player")
        print("5. Delete Player")
        print("6. Mark Attendance")
        print("7. Add Match Performance")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_player(players)
            save_data(players)

        elif choice == "2":
            view_players(players)

        elif choice == "3":
            search_player(players)

        elif choice == "4":
            update_player(players)
            save_data(players)

        elif choice == "5":
            delete_player(players)
            save_data(players)

        elif choice == "6":
            mark_attendance(players)
            save_data(players)

        elif choice == "7":
            add_match_performance(players)
            save_data(players)
           
        elif choice == "8":
            save_data(players)
            print("Thank you for using Cricket Management System.")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    get_lock_password()
    main()
else:
    print("Program Interupted")
