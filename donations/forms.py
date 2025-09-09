# from django import forms
# from .models import Donation

# class DonationForm(forms.ModelForm):
#     class Meta:
#         model = Donation
#         fields = ['donation_type', 'description', 'amount', 'quantity']

#     def clean(self):
#         cleaned_data = super().clean()
#         donation_type = cleaned_data.get('donation_type')
#         amount = cleaned_data.get('amount')
#         quantity = cleaned_data.get('quantity')

#         if donation_type == 'money' and not amount:
#             raise forms.ValidationError("Please enter an amount for money donation.")
#         if donation_type == 'food' and not quantity:
#             raise forms.ValidationError("Please enter quantity for food donation.")

#         return cleaned_data
        
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["food_item", "quantity", "expiry_date", "location"]
        widgets = {
            "food_item": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "expiry_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }
