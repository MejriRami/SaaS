from django.test import TestCase
from django.conf import settings

# Create your tests here.


from django.test import TestCase
from django.conf import settings

class NeonDBTestCase(TestCase):
    def test_db_url(self):
        database_url = getattr(settings, 'DATABASE_URL', '')
        self.assertIn("neon.tech", database_url)
