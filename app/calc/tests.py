
from django.test import TestCase
from calc import views


class TestWebpage(TestCase):
    def test_index_page(self):

        response=self.client.get("/template/")
        self.assertTemplateUsed(response,"index.html")