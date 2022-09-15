from django.urls import path
from.import views

app_name = 'blog'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index2"),
    path('good/',views.GoodView.as_view(),name="good"),
    path('inquiry2/',views.InquiryView.as_view(),name="inquiry2"),
]
