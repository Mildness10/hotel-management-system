from django import forms
from .models import HotelSystem


class HotelSystemForm(forms.ModelForm):
    class Meta:
        model = HotelSystem
        fields = [
            "room_number",
            "amount_paid",
            "occupant_name",
            "occupant_email",
            "occupant_occupation",
            "number_of_night",
            "start_date",
            "end_date",
        ]
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields["start_date"].widget.format = '%d/%m/%Y'
        self.fields["end_date"].widget.format = '%d/%m/%Y'
        
        self.fields["start_date"].input_formats = ['%d/%m/%Y']
        self.fields["end_date"].input_formats = ['%d/%m/%Y']