from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug



class Posts(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE,'Active'),
        (DRAFT, 'Draft')
    )
    
    
    category = models.ForeignKey(Category, related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s' % (self.category.slug, self.slug)


class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
        




# Create your models here.
