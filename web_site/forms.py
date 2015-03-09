from django.forms import fields
from envelope.forms import ContactForm

__author__ = 'Iurii Sergiichuk'


class CustomContactForm(ContactForm):
    phone = fields.CharField(max_length=21)
    organisation = fields.CharField(max_length=50)