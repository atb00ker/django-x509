from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from .. import settings as app_settings

import uuid


def crl_common(request, pk, model):
    authenticated = request.user.is_authenticated
    authenticated = authenticated() if callable(authenticated) else authenticated
    if app_settings.CRL_PROTECTED and not authenticated:
        return HttpResponse(_('Forbidden'),
                            status=403,
                            content_type='text/plain')
    ca = model.objects.get(pk=pk)
    return HttpResponse(ca.crl,
                        status=200,
                        content_type='application/x-pem-file')


def crl(request, pk):
    """
    returns CRL of a CA
    """
    model = crl.ca_model
    return crl_common(request, pk, model)


def uuidcrl(request, pk):
    """
    returns CRL of a UUID_CA
    """
    pk = uuid.UUID(pk)
    model = uuidcrl.ca_model
    return crl_common(request, pk, model)
