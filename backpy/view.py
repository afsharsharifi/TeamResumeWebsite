from BackPyContactUs.models import ContactUs
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from BackPySetting.models import Setting, About, SocialMedia, ShareUs, Status
from BackPyTeam.models import TeamMembers
from BackPyBlog.models import Blog
from BackPySlider.models import Slider
from BackPyService.models import Service, Designer
from BackPyPortfolio.models import Section
from BackPyRating.models import Rating
from BackPyContactUs.forms import CreateContactForm


def header(request):
    SiteSetting = Setting.objects.first()
    ShareUsSetting = ShareUs.objects.all()

    context = {
        'setting': SiteSetting,
        'share_us': ShareUsSetting
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request):
    SiteSetting = Setting.objects.first()
    SocialMediaSetting = SocialMedia.objects.all()
    context = {
        'setting': SiteSetting,
        'social_media': SocialMediaSetting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    SiteSetting = Setting.objects.first()
    AboutSetting = About.objects.first()
    TeamMembersSetting = TeamMembers.objects.all()
    BlogSetting = Blog.objects.all()
    StatusSetting = Status.objects.all()
    SliderSetting = Slider.objects.first()
    Services = Service.objects.all()
    Designs = Designer.objects.all()
    Sections = Section.objects.all()
    Rate = Rating.objects.all()

    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        phone = contact_form.cleaned_data.get('phone')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, phone=phone, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contact_form = CreateContactForm()


    count = 0
    for item in Sections:
        if item.active == True:
            count = count + 1

    context = {
        'setting': SiteSetting,
        'about': AboutSetting,
        'team_member': TeamMembersSetting,
        'blog': BlogSetting,
        'status': StatusSetting,
        'slider': SliderSetting,
        'service': Services,
        'design': Designs,
        'section': Sections,
        'count_projects': count,
        'rate': Rate,
        'contact_form': contact_form,
    }
    return render(request, 'home_page.html', context)