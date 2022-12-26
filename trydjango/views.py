"""
render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
	"""
	Take in a request and
	Return html as response
	"""
	random_id = random.randint(1, 4)
	article_obj = Article.objects.get(id=random_id)
	context = {
		"title": article_obj.title,
		"id": article_obj.id,
		"content": article_obj.content
	}
	HTML_STRING = render_to_string("home_view.html", context=context)
	# HTML_STRING = """
	# <h1>Hello {title} (id: {id})</h1>
	# <h1>Hello {content}!</h1>
	# """.format(**context)

	return HttpResponse(HTML_STRING)

