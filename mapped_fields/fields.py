from django import forms

from mapped_fields.widgets import (MappedTextInput, MappedDateInput,
    MappedNumberInput)


class MappedFieldMixin(object):
    """
    """

    def __init__(self, field_names, **kwargs):
        """
        """
        super(MappedFieldMixin, self).__init__(**kwargs)
        print self.widget


class CharField(MappedFieldMixin, forms.CharField):
    """
    """
    pass


class DateField(MappedFieldMixin, forms.DateField):
    """
    """
    pass


class IntegerField(MappedFieldMixin, forms.IntegerField):
    """
    """
    pass
