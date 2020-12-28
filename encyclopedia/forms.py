from django import forms

#search form
class NewSearchForm(forms.Form):
    search = forms.CharField(label="Search",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Search Encyclopedia'}))

#new page
class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title",required = True,help_text="<p class='text-secondary'>Help:<a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> </p>",
    widget= forms.TextInput
    (attrs={'placeholder':'Enter Title','class':'col-sm-5','style':'left: 20px;'}))

    content = forms.CharField(label="Markdown content",required= False, 
    widget= forms.Textarea
    (attrs={'placeholder':'Enter markdown content','class':'col-sm-11','style':'top:0rem'}))

#edit page
class EditForm(forms.Form):
    title = forms.CharField(label="Title",required = True,help_text="<p class='text-secondary'>Help:<a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> </p>",
    widget= forms.TextInput
    (attrs={'placeholder':'Enter Title','class':'col-sm-5','style':'left: 20px;'}))

    content = forms.CharField(label="Markdown content",required= False, 
    widget= forms.Textarea
    (attrs={'placeholder':'Enter markdown content','class':'col-sm-11','style':'margin-bottom: 50px;'}))

