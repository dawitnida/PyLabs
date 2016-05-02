from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from myblog.models import Post
from datetime import datetime
# Create your tests here.

# manage.py test myblog.tests.BlogTest
class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.u_name = 'admin'
        self.u_pass = 'admin'
        self.user =  User.objects.create_user(self.u_name, self.u_pass)
        self.blogpost = Post.objects.create(title="Winterwonder",
                                            content="The living star Pluto",
                                            author = self.user,
                                            timestamp= "2014-10-11 22:49:54")
        self.blogp = Post.objects.get(id=1)

    # manage.py test myblog.tests.BlogTest.test_edit_post
    def test_edit_post(self):
        url = reverse('edit_post', args=[4])
        response = self.client.post('/editblog/4/')
        self.assertEqual(response.status_code, 302)

        self.assertEqual(self.user.username, 'admin')
        self.client.login(username=self.user.username, password=self.user.password)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.is_authenticated())
        response = self.client.get(reverse('edit_post', args=[2]))
        self.assertEqual(response.status_code, 200)
        url = reverse('edit_post', args=[15])
        response = self.client.post(url, {'title' : 'Astroid',
                                          'content': 'New C lan guage.',
                                          'timestamp': datetime.now(),
                                          'author': self.user})
        self.failUnlessEqual(response.status_code, 302)

        response = self.client.post('/myblog/4/')
        self.assertEqual(response.status_code, 200)

    # manage.py test myblog.tests.BlogTest.test_blog_model
    def test_blog_model(self):

        self.assertEqual(self.blogp.title, "Winterwonder")
        self.assertEqual(self.blogp.author.username, "carol")
        self.assertEqual(self.blogp.content, "The living star Pluto")


    def test_redirect(self):
        response = self.client.get('/editblog/1/')
        self.failUnlessEqual(response.status_code, 200)



