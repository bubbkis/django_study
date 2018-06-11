from django.urls import reverse, resolve
from django.test import TestCase

from ..views import BoardListView
from ..models import Board

# Create your tests here.
class IndexTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('boards:index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/boards/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_index_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

