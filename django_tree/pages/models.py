from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, blank=True, null=True, default="")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=256, blank=True, null=True, default="")

    def save(self, *args, **kwargs):
        if not self.parent:
            if self.slug:
                self.url = f"{self.slug}/"
            else:
                self.url = "/"
        else:
            self.url = f"{self.parent.url}{self.slug}/"
        super().save(*args, **kwargs)

        for child in self.children.all():
            child.save()

    def __str__(self):
        return self.name
