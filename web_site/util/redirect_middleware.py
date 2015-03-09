from django.contrib.sites.models import Site
from django.http.response import HttpResponseRedirect
from osis.settings import SITE_ID

__author__ = 'Iurii Sergiichuk'


class RedirectMiddleware(object):
    """Middleware class that redirects non "www" subdomain requests to a
    specified URL or business.
    """

    def process_request(self, request):
        """Returns an HTTP redirect response for requests including non-"www"
        subdomains.
        """
        scheme = "http" if not request.is_secure() else "https"
        path = request.get_full_path()
        domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
        pieces = domain.split('.')
        subdomain = ".".join(pieces[:-2])  # join all but primary domain
        default_domain = Site.objects.get(id=SITE_ID)
        if domain in {default_domain.domain}:
            return None
        return HttpResponseRedirect("{0}://{1}".format(
            scheme, default_domain.domain))