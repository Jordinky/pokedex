from django import forms


class SearchPokemon(forms.Form):
    pokemon = forms.CharField(label= False , widget=forms.TextInput(attrs={'placeholder': 'Pokemon name or id: magikarp,35...', 'style': 'width:600px;', 'class': 'form-control'}))