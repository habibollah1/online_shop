from django.test import TestCase
from django.shortcuts import reverse


# from django.contrib.auth import User

# from .views import HomePageView

class PagesTest(TestCase):

    # def setUpTestData(cls):
    #     # cls.author = User.client
    #     home.objects.create(
    #         title: 'title1'
    #         text: 'text1'
    #     )

    def test_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_home_html_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # def test_home_title_content(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertContains(response, self.title)
