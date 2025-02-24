from django import forms
from .models import GroceryItem

class GrocerySelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically create checkbox fields for each grocery item
        items = GroceryItem.objects.all()
        for item in items:
            self.fields[f'item_{item.id}'] = forms.BooleanField(
                label=item.name,
                required=False
            )