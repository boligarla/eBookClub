import datetime
from django.utils.translation import ugettext_lazy as ul
from django.core.exceptions import ValidationError


from django import forms


class RenewBookForm(forms.Form):
    """Form for a site owner to renew books."""
    renewal_date = forms.DateField(
            help_text="Enter a date between now and 5 weeks (default 3).")

    # def clean_renewal_date(self):
    def valid_renewal_date(self):
        data = self.cleaned_data['book_renewal_date']

        # Check date renewal date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal date is in past'))
        # Check date is in range librarian allowed to change (+5weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=5):
            raise ValidationError(
                ul('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return data.
        return data
