from .models import User, Team, Activity, Leaderboard, Workout

def populate_database():
    # Create a test user
    user = User.objects.create(username="testuser", email="testuser@example.com", password="password")

    # Create a test team and add the user to it
    team = Team.objects.create(name="Test Team")
    team.members.add(user)

    # Create a test activity
    activity = Activity.objects.create(user=user, activity_type="Running", duration="01:00:00")

    # Create a test leaderboard entry
    leaderboard = Leaderboard.objects.create(user=user, score=100)

    # Create a test workout
    workout = Workout.objects.create(name="Test Workout", description="Test Description")

    print("Database populated with test data.")

if __name__ == "__main__":
    populate_database()
