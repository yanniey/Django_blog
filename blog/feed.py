from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPosts(Feed):
	title = "Q blog"
	link = "/feed/"
	description = "Latest Posts of Q"

	def items(self):
		return Entry.objects.published()[:5]