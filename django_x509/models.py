from .base.models import AbstractCa, AbstractCert, AbstractUUIDCa, AbstractUUIDCert


class Ca(AbstractCa):
    """
    Concrete Ca model
    """
    class Meta(AbstractCa.Meta):
        abstract = False


class Cert(AbstractCert):
    """
    Concrete Cert model
    """
    class Meta(AbstractCert.Meta):
        abstract = False

class UUIDCa(AbstractUUIDCa):
    """
    Concrete UUID Ca model
    """
    class Meta(AbstractUUIDCa.Meta):
        abstract = False


class UUIDCert(AbstractUUIDCert):
    """
    Concrete UUID Cert model
    """
    class Meta(AbstractUUIDCert.Meta):
        abstract = False
