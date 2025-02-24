from django.shortcuts import render
from .models import GroceryItem
from .forms import GrocerySelectionForm

def grocery_list(request):
    form = GrocerySelectionForm(request.POST or None)
    selected_items = []
    
    if request.method == 'POST' and form.is_valid():
        # Get selected items
        for field_name, value in form.cleaned_data.items():
            if value:  # If checkbox is checked
                item_id = int(field_name.split('_')[1])
                selected_items.append(GroceryItem.objects.get(id=item_id))
    
    return render(request, 'grocery/index.html', {
        'form': form,
        'selected_items': selected_items
    })