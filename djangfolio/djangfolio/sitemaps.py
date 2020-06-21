from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class IndexSitemap(Sitemap):
    """Sitemap for IndexView."""

    changefreq = "monthly"
    priority = 1

    def items(self):
        """
        Get a list of items corresponding to this sitemap.

        :return: a list of urls
        """
        return ["index"]

    def location(self, obj):
        """
        Get the location of an object for this sitemap.

        :param obj: the object to get the location for
        :return: the relative url to the objects location on this site
        """
        return reverse(obj)
