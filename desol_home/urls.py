from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('about-us', about_us, name="about_us"),
    path('contact-us', contact_us, name="contact_us"),
    path('career-destination', career_destination, name="career_destination"),
    path('work-in-poland', about_poland, name="about_poland"),
    path('work-in-lithuania', about_lithuania, name='about_lithuania'),
    path('work-in-latvia', about_latvia, name='about_latvia'),
    path('packages', packages, name="packages"),
    path('news', news, name="news"),
    path('contact-form-submission', customer_details_submission, name="customer_details_submission"),
    path('news/<slug:slug>', PostDetailView.as_view(), name="blog_details"),
]
