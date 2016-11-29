from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255)
    body  = models.TextField()
    date  = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:            
            self.slug = slugify(self.title) 
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):        
        return reverse('blog.views.view_post', args=[str(self.slug)])