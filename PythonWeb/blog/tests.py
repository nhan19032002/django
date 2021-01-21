from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.Create(
            title = 'myTitle',
            body= 'just a Test'
        )


