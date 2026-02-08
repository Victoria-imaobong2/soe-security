# Secure Software Engineering Department System

# Step 1: Define users with roles and credentials
users = {
    "staff1": {"password": "staff123", "role": "staff"},
    "student1": {"password": "stud123", "role": "student"}
}

# Step 2: Define role-based permissions
permissions = {
    "staff": ["post_announcement", "manage_course", "grade_student"],
    "student": ["view_announcement", "submit_assignment", "check_grade"]
}

# Step 3: Activity log
activity_log = []

# Step 4: Authentication
def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        print("Authentication successful")
        return True
    print("Authentication failed")
    return False

# Step 5: Authorization
def authorize(username, action):
    role = users[username]["role"]
    if action in permissions[role]:
        return True
    return False

# Step 6: Input validation
def validate_input(data):
    if data.strip() == "":
        return False
    return True


# Step 7: Perform secure action
def perform_action(username, action, data=""):
    if not authorize(username, action):
        print("Access denied: Unauthorized action")
        return

    if data and not validate_input(data):
        print("Invalid input detected")
        return

    print(f"Action '{action}' performed successfully")
    activity_log.append(f"{username} performed {action}")

# Step 8: View activity logs (monitoring)
def view_logs():
    print("\nSystem Activity Logs:")
    for log in activity_log:
        print(log)

# System Execution (Simulation)

username = input("Enter username: ")
password = input("Enter password: ")

if authenticate(username, password):
    action = input("Enter action to perform: ")
    data = input("Enter data (if required): ")
    perform_action(username, action, data)

view_logs()
