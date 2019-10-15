from django import forms
from .models import Post, PostUpdate, Event, Poll


class PostFilterForm(forms.Form):
    page = forms.IntegerField(required=False)
    events_only = forms.BooleanField(required=False, initial=False)
    polls_only = forms.BooleanField(required=False, initial=False)
    query = forms.CharField(required=False)

    def filter_posts(self, posts):
        if self.is_valid():
            if self.cleaned_data['events_only']:
                if self.cleaned_data['polls_only']:
                    posts = posts.exclude(event=None, poll=None)
                posts = posts.exclude(event=None)

            if self.cleaned_data['polls_only']:
                posts = posts.exclude(poll=None)

            if self.cleaned_data['query'] != 'None':
                posts = posts.filter(title__contains=self.cleaned_data['query'])

        return posts

print('abc')
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('start_date', 'end_date', 'venue')


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "cover_image", 'is_public', 'is_published', 'notify_followers')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostUpdate
        fields = ['content']


class PollCreateForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['track_votes']


class PollUpdateForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['track_votes']
