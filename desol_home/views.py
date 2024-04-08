from django.shortcuts import redirect, render
from desol_home.models.customer_leads import CustomersDetails
from desol_home.models.global_links import *
from desol_home.models.reviews import CustomerReview
from desol_home.models.faqs import FaqSection
from desol_home.models.blogs import BlogsDetail
from hitcount.views import HitCountDetailView
import math
from django.template.defaultfilters import striptags

def homepage(request):
    testimonials = CustomerReview.objects.all()
    faqs = FaqSection.objects.all()
    return render(request, template_name="home/index.html", context={'testimonials': testimonials, 'faqs': faqs})

def global_logo(request):
    context = {
        'logo': Logo.objects.all(),
        'favicon': Favicon.objects.all(),
        'socials': SocialMediaLinks.objects.all()
    }
    return context

def about_us(request):
    return render(request, template_name="home/about-us.html")

def career_destination(request):
    return render(request, template_name="home/career_destination.html")

def about_poland(request):
    return render(request, template_name="home/destinations/about_poland.html")

def about_lithuania(request):
    return render(request, template_name="home/destinations/about_lithuania.html")

def about_latvia(request):
    return render(request, template_name="home/destinations/about_latvia.html")

def packages(request):
    return render(request, template_name="home/packages.html")

def news(request):
    blogs = BlogsDetail.objects.all().filter(is_published=True).order_by('-created_at')
    return render(request, template_name="home/news.html", context={'blogs': blogs})

class PostDetailView(HitCountDetailView):
    model = BlogsDetail
    template_name = 'home/blog_detail.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        stripped_body = striptags(self.object.body)
        total_word_count = len(stripped_body.split())
        total_word_count_per_minutes = math.ceil(total_word_count / 200)
        context.update({
        'popular_posts': BlogsDetail.objects.order_by('-hit_count_generic__hits')[:3],
        'total_time': total_word_count_per_minutes,
        })
        return context

def contact_us(request):
    return render(request, template_name="home/contact_us.html")

def customer_details_submission(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        position = request.POST.get('position')
        destination = request.POST.get('destination')
        
        customer_obj = CustomersDetails.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            country = country,
            position = position,
            destination = destination
        )
        return redirect('homepage')