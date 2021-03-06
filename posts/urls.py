from django.urls import path
from django.contrib.auth.views import TemplateView
from . import views

app_name = "posts"

urlpatterns = [
    path('like_post/<int:id>/', views.likePost, name='like-post'),

    path('events/', views.events, name="events"),
    path('polls/', views.polls, name="polls"),
    path('like_post/<int:id>/', views.likePost, name='like-post'),
    path('edit-post/<int:encrypted_id>/', views.edit_post, name="post-edit"),
    path('edit-poll/<int:encrypted_id>/', views.edit_poll, name="poll-edit"),
    path('edit-event/<int:encrypted_id>', views.events_edit, name="events_edit"),
    # path('add-user-event-interested', views.interested_event)
    path('<slug:club_name_slug>/create-poll/', views.create_poll, name='create_poll'),
    # path('<slug:club_name_slug>/submit-poll/', views.submitPoll, name='submit_poll'),
    path('<slug:club_name_slug>/', views.club_posts, name="club_posts"),
    path('<slug:club_name_slug>/events/', views.club_events, name="club_events"),
    path('<slug:club_name_slug>/polls/', views.club_polls, name="club_polls"),
    path('<slug:club_name_slug>/<int:encrypted_id>', views.post_detail, name="post_detail"),
    path('<slug:club_name_slug>/create', views.create_post, name="post-add"),

    path('<slug:club_name_slug>/<int:encrypted_id>/issue-update', views.post_update, name="post-update"),

    path('<slug:club_name_slug>/<int:encrypted_id>/vote', views.cast_vote, name='cast-vote'),
    path('<slug:club_name_slug>/<int:encrypted_id>/subscribe', views.subscribe, name='subscribe'),
    path('<slug:club_name_slug>/<int:encrypted_id>/unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('<slug:club_name_slug>/<int:encrypted_id>/event_interested', views.event_interested, name='event_interested'),
    path('<slug:club_name_slug>/<int:encrypted_id>/event_not_interested', views.event_uninterested,
         name='event_uninterested'),

    path('<slug:club_name_slug>/events/create', views.events_create, name="events_create"),

    # path('ajax/interested_event', views.interested_event, name="interested_event"),

    path('<slug:club_name_slug>/<int:encrypted_id>/pin', views.pin_post, name="pin-post"),
    path('<slug:club_name_slug>/<int:encrypted_id>/unpin', views.unpin_post, name="unpin-post"),
    path('', views.posts, name='posts'),

]
