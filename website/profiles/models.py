from django.db import models


class Profile(models.Model):
    """Profile model."""

    active = models.BooleanField(default=False, verbose_name="Show on homepage")
    picture = models.ImageField(upload_to="profile_images/")
    first_name = models.CharField(max_length=512, blank=True)
    second_name = models.CharField(max_length=512, blank=True)
    short_function_description = models.CharField(max_length=4096, blank=True)
    about_me = models.TextField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    about_me_title = models.CharField(max_length=512, default="About me")
    career_title = models.CharField(max_length=512, default="Career")
    projects_title = models.CharField(max_length=512, default="Projects")
    contact_me_title = models.CharField(max_length=512, default="Contact me")
    enable_contact_me = models.BooleanField(
        default=False, verbose_name="Enable the contact me section"
    )

    def save(self, *args, **kwargs):
        """
        Save function to ensure that there is only one Profile object with active=True.

        :param args: arguments
        :param kwargs: keyword arguments
        :return: super(Profile, self).save()
        """
        if self.active:
            Profile.objects.filter(active=True).exclude(pk=self.pk).update(active=False)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        """
        Get this object as string.

        :return: the first name and last name of this object
        """
        return "{} {}".format(self.first_name, self.second_name)


class Career(models.Model):
    """Career model."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_time = models.DateField(null=False, blank=False)
    end_time = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=512, blank=False)
    short_description = models.TextField(blank=True)
    institution = models.CharField(max_length=256, blank=True)

    def __str__(self):
        """
        Get this object as string.

        :return: the title of this object
        """
        return self.title

    class Meta:
        """Meta class."""

        ordering = ["-start_time"]


class Project(models.Model):
    """Project model."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=512, blank=False)
    image = models.ImageField()
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=4096, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        """
        Get this object as string.

        :return: the title of this object
        """
        return self.title

    class Meta:
        """Meta class."""

        ordering = ["-start_time"]
