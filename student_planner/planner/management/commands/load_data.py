from django.core.management.base import BaseCommand
from planner.models import Course, Subject
from planner.api import PlanningCoursesAPI
from tqdm import tqdm
class Command(BaseCommand):
    help = 'Load data from API into database'

    def handle(self, *args, **options):
        api = PlanningCoursesAPI('http://localhost:8080')
        data = api.get_all_courses()


        for item in tqdm(data):
            if item.subjectArea is None or item.course is None:
                continue
            else:
                subject, created = Subject.objects.get_or_create(
                    id=item.subjectArea['id'],
                    defaults={
                        'short_name': item.subjectArea['shortName'],
                        'long_name': item.subjectArea['longName'],
                    }
                )

                course, created = Course.objects.get_or_create(
                    id=item.course['id'],
                    defaults={
                        'subject_area': subject,
                    }
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))