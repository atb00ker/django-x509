from django.contrib import admin

from .base.admin import AbstractCaAdmin, AbstractCertAdmin, AbstractUUIDCaAdmin, AbstractUUIDCertAdmin
from .models import Ca, Cert, UUIDCa, UUIDCert


class CertAdmin(AbstractCertAdmin):
    pass


class CaAdmin(AbstractCaAdmin):
    pass


class UUIDCaAdmin(AbstractUUIDCaAdmin):
    pass


class UUIDCertAdmin(AbstractUUIDCertAdmin):
    pass


admin.site.register(Ca, CaAdmin)
admin.site.register(Cert, CertAdmin)
admin.site.register(UUIDCa, UUIDCaAdmin)
admin.site.register(UUIDCert, UUIDCertAdmin)
