from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^questions$', views.questions, name="questions"),
    # url(r'^add$', views.add, name="add"),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.votes, name="vote"),
]