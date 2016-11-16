from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from main.views import home, form
from main.models import Article
from main.forms import SurveyForm

# Create your tests here.
class HomepageTest(TestCase):

    def test_root_resolves_to_home(self):
        root=resolve('/')
        self.assertEqual(root.func,home)

    def test_root_loads_index_html(self):
        request  = HttpRequest()
        response = home(request)
        self.assertTrue(response.content.startswith(b'<!doctype html>\n<html>\n<head>'))
        self.assertIn("Hello World",response.content.decode())


class ModelTest(TestCase):

    def setUp(self):        
        self.test_title = "TEST My Awesome Article TEST"
        self.test_body  = "This is a text"
        Article.objects.create(title=self.test_title, text=self.test_body)        
        self.article = Article.objects.all().filter(title=self.test_title)
        
    def tearDown(self):
        self.article.delete()
        
    def test_able_to_save_entries_to_db(self):
        self.assertEqual(self.article.values()[0]['text'],self.test_body)

    def test_index_html_displays_article(self):
        request = HttpRequest()
        response = home(request)
        self.assertTrue(response.content.startswith(b'<!doctype html>\n<html>\n<head>'))
        self.assertIn(self.test_body,response.content.decode())

class FormTest(TestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.post_dict = {'human':True,'color':'bl','age':29,'name':'David Fozo','subscription':True,'email':'example@gmail.com'}

    def test_form_renders_on_page_properly(self):
        response = form(self.request)
        for i in ['form','input','human','color','age','name','email']:
            self.assertIn(i,response.content.decode())

    def test_form_redirection(self):

        def subs_n_test(subs,red_url):
            self.post_dict['subscription'] = subs
            response = self.client.post('/form/',self.post_dict)
            self.assertRedirects(response,red_url)

        subs_n_test(False,'/thanks/')
        subs_n_test(True, '/subscribed/')

    def test_not_human_raises_error(self):
        self.post_dict['human'] = False
        self.post_dict['color'] = 'rd'
        form = SurveyForm(self.post_dict)
        self.assertEqual(form.is_valid(),False)

