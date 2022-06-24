from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

from .models import TinyModel


class TinyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit', css_class='mt-2'))
        self.helper.layout = Layout(
            Row(
                Column('url', css_class='mt-4'),
                Column('alias', css_class='mt-4')
            )
        )

    class Meta:
        model = TinyModel
        fields = ['url', 'alias']
        labels = {
            'url': 'Enter url',
            'alias': 'Alias (Optional)' 
            }
