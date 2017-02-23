from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Place

# Create your tests here.

class TestViewHomePageIsEmptyList(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist\wishlist.html')
        self.assertFalse(response.context['places']) # Empty lists are false

class TestWishList(TestCase):

    # Load dataset from fixtures
    fixtures = ['test_places']

    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        # Check correct template
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What data was sent?
        data_rendered = list(response.context['places'])
        # What data is in the databases
        data_expected = list(Place.objects.filter(visited=False))
        # Is it the same?
        self.assertCountEqual(data_rendered, data_expected)
