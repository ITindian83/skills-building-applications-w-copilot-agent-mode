from django.core.management.base import BaseCommand
from octofit_tracker.models import ExerciseIssue

class Command(BaseCommand):
    help = 'Populate the ExerciseIssue model with sample data'

    def handle(self, *args, **kwargs):
        sample_issues = [
            {"title": "Push-up Form Issue", "description": "Difficulty maintaining proper form during push-ups."},
            {"title": "Squat Depth Problem", "description": "Struggling to achieve full depth in squats."},
            {"title": "Pull-up Grip Confusion", "description": "Uncertainty about the correct grip for pull-ups."},
        ]

        for issue in sample_issues:
            ExerciseIssue.objects.get_or_create(title=issue["title"], defaults={"description": issue["description"]})

        self.stdout.write(self.style.SUCCESS('Successfully populated ExerciseIssue model with sample data.'))
