from django.core.management.base import BaseCommand
from octofit_tracker.models import ExerciseIssue  # Assuming ExerciseIssue is a model in your app

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Add your database population logic here
        try:
            # Example: Adding sample exercise issues
            ExerciseIssue.objects.create(title='Push-ups', description='Perform 20 push-ups')
            ExerciseIssue.objects.create(title='Squats', description='Perform 30 squats')
            ExerciseIssue.objects.create(title='Plank', description='Hold a plank for 1 minute')

            self.stdout.write(self.style.SUCCESS('Database populated successfully with exercise issues.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {e}'))
