from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC', is_superhero=True),
            User(name='Batman', email='batman@dc.com', team='DC', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Workouts
        workouts = [
            Workout(name='Web Swinging', description='Swing through the city', suggested_for_team='Marvel'),
            Workout(name='Gadget Training', description='Use your gadgets', suggested_for_team='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        # Activities
        spiderman = User.objects.get(email='spiderman@marvel.com')
        ironman = User.objects.get(email='ironman@marvel.com')
        wonderwoman = User.objects.get(email='wonderwoman@dc.com')
        batman = User.objects.get(email='batman@dc.com')
        Activity.objects.create(user=spiderman, type='Web Swinging', duration=30, date=timezone.now().date())
        Activity.objects.create(user=ironman, type='Flight Training', duration=45, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, type='Combat', duration=60, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Detective Work', duration=50, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
