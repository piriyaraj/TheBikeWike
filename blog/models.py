from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from user_profile.models import User
from .slugs import generate_unique_slug

from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(null=True, blank=False,unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description=RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=True)
    slug = models.SlugField(null=True, blank=True)
    banner = models.ImageField(upload_to='blog_banners',null=True)


STATUS = (
    (0, "Updated"),
    (1, "Not updated")
)

class Blog(models.Model):
    user = models.ForeignKey(User,related_name='user_blogs',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='category_blogs',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,related_name='tag_blogs',blank=True)
    likes = models.ManyToManyField(User,related_name='user_likes',blank=True)
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(null=True, blank=True)
    banner = models.ImageField(upload_to='blog_banners')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=True)
    isupdated = models.IntegerField(choices=STATUS, default=0)

    def get_absolute_url(self):
        # return reverse("post/", args=[self.slug])
        return f'/{self.slug}/'
    
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        updating = self.pk is not None
        
        if updating:
            self.slug = generate_unique_slug(self, self.title, update=True)
            super().save(*args, **kwargs)
        else:
            self.slug = generate_unique_slug(self, self.title)
            super().save(*args, **kwargs)


class Biketable(models.Model):
    Model = models.CharField(max_length=200, default="")
    Year = models.CharField(max_length=200, default="")
    Category = models.CharField(max_length=200, default="")
    Rating = models.CharField(max_length=200, default="")
    Displacement = models.CharField(max_length=200, default="")
    Engine_type = models.CharField(max_length=200, default="")
    Power = models.CharField(max_length=200, default="")
    Top_speed = models.CharField(max_length=200, default="")
    Fuel_system = models.CharField(max_length=200, default="")
    Cooling_system = models.CharField(max_length=200, default="")
    Gearbox = models.CharField(max_length=200, default="")
    Transmission_type = models.CharField(max_length=200, default="")
    Clutch = models.CharField(max_length=200, default="")
    Fuel_consumption = models.CharField(max_length=200, default="")
    Greenhouse_gases = models.CharField(max_length=200, default="")
    Frame_type = models.CharField(max_length=200, default="")
    Front_suspension = models.CharField(max_length=200, default="")
    Rear_suspension = models.CharField(max_length=200, default="")
    Front_tire = models.CharField(max_length=200, default="")
    Rear_tire = models.CharField(max_length=200, default="")
    Front_brakes = models.CharField(max_length=200, default="")
    Rear_brakes = models.CharField(max_length=200, default="")
    Dry_weight = models.CharField(max_length=200, default="")
    Power_weight_ratio = models.CharField(max_length=200, default="")
    Seat_height = models.CharField(max_length=200, default="")
    Overall_height = models.CharField(max_length=200, default="")
    Overall_length = models.CharField(max_length=200, default="")
    Overall_width = models.CharField(max_length=200, default="")
    Wheelbase = models.CharField(max_length=200, default="")
    Fuel_capacity = models.CharField(max_length=200, default="")
    Color_options = models.CharField(max_length=200, default="")
    Starter = models.CharField(max_length=200, default="")
    Factory_warranty = models.CharField(max_length=200, default="")
    Comments = models.CharField(max_length=200, default="")
    Update_specs = models.CharField(max_length=200, default="")
    Insurance_costs = models.CharField(max_length=200, default="")
    Finance_options = models.CharField(max_length=200, default="")
    Parts_finder = models.CharField(max_length=200, default="")
    Maintenance = models.CharField(max_length=200, default="")
    Ask_questions = models.CharField(max_length=200, default="")
    Related_bikes = models.CharField(max_length=200, default="")
    idofblog = models.ForeignKey(Blog, related_name='table_blogs', on_delete=models.CASCADE)

class Bikeimage(models.Model):
    image = models.ImageField()
    postId = models.ForeignKey(Blog, related_name='image_blogs', on_delete=models.CASCADE)
    alt = models.TextField(max_length=140, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_comments',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blog_comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_replies',
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='comment_replies',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


