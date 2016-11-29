from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.models import BlogPost
from blog.views  import view_post

# Create your tests here.
class BlogPostTest(TestCase):

    def setUp(self):
        self.title = "Blog Post Test" 
        self.slug  = "blog-post-test"
        self.body  = "This is a test."
        self.date  = "2016-11-26"

        BlogPost.objects.create(
            title=self.title,
            slug=self.slug,
            body=self.body,
            date=self.date)

    def test_blogpost_resolves_to_slug(self):
        blogpost = resolve('/blog/' + self.slug + '/')
        self.assertEqual(blogpost.func,view_post)

    def test_blogpost_displays_article(self):

        request = HttpRequest()
        response = view_post(request,self.slug)
        self.assertTrue(response.content.startswith(b'<!doctype html>'))
        for i in [self.title,self.body]:
            self.assertIn(i,response.content.decode())

    def tearDown(self):
        BlogPost.objects.all().filter(title=self.title).delete()


    # def test_index_html_displays_article(self):
    #     request = HttpRequest()
    #     response = home(request)
    #     self.assertTrue(response.content.startswith(b'<!doctype html>\n<html>\n<head>'))
    #     self.assertIn(self.test_body,response.content.decode())



    # def setUp(self):        
    #     self.test_title = "TEST My Awesome Article TEST"
    #     self.test_body  = "This is a text"
    #     Article.objects.create(title=self.test_title, text=self.test_body)        
    #     self.article = Article.objects.all().filter(title=self.test_title)
        
    # def tearDown(self):
    #     self.article.delete()
        
    # def test_able_to_save_posts(self):
    #     self.assertEqual(self.article.values()[0]['text'],self.test_body)

