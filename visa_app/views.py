import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.core.exceptions import ValidationError


def visa_home(request):
    testimonial = Testimonials.objects.all()
    api_url = "https://crm.theskytrails.com/api/Product/"
    response = requests.get(api_url)

    if response.status_code == 200:
        products = response.json()
        latest_products = products[:6]
    else:
        products = []

    context = {"testimonial": testimonial, "products": latest_products}

    return render(request, "VisaPage/home.html", context)


def visa_details(request):
    api_url = "https://crm.theskytrails.com/Api/VisaCountry/"
    response = requests.get(api_url)

    if response.status_code == 200:
        country = response.json()
    else:
        country = []

    api_url = "https://crm.theskytrails.com/Api/VisaCategory/"
    response = requests.get(api_url)

    if response.status_code == 200:
        category = response.json()
    else:
        category = []
        
    featureblog = Blogs.objects.filter(blogs_type="Featured Articles").order_by("-id")

    context = {"country": country, "category": category, "featureblog":featureblog}
    return render(request, "VisaPage/Visa1.html", context)


def investvisa_details(request):
    return render(request, "VisaPage/Investvisa.html")


def studyvisa_details(request):
    return render(request, "VisaPage/Studyvisa.html")


def ssdc(request):
    return render(request, "VisaPage/ssdc.html")


def overseas(request):
    return render(request, "VisaPage/Overseas.html")


def overseas_all(request):
    return render(request, "VisaPage/overseasjobs2.html")


def overseas_details(request):
    return render(request, "VisaPage/overseasjob3.html")


def blog(request):
    blogs = Blogs.objects.filter(blogs_type="Latest Updates").order_by("-id")[:1]
    blog = Blogs.objects.filter(blogs_type="Latest Updates").order_by("-id")
    editorblog = Blogs.objects.filter(blogs_type="Editors Pick").order_by("-id")
    featureblog = Blogs.objects.filter(blogs_type="Featured Articles").order_by("-id")
    context = {
        "blogs": blogs,
        "blog": blog,
        "editorblog": editorblog,
        "featureblog": featureblog,
    }
    return render(request, "VisaPage/Blogs1.html", context)


def blog_details(request, id):
    blog = Blogs.objects.get(id=id)
    featureblog = Blogs.objects.filter(blogs_type="Featured Articles").order_by("-id")
    context = {"blog": blog, "featureblog": featureblog}
    return render(request, "VisaPage/blog_details.html", context)


def immigrationblog(request):
    return render(request, "VisaPage/immigrationblog.html")


def aboutus(request):
    return render(request, "VisaPage/Aboutus.html")


def privacypolicy(request):
    return render(request, "VisaPage/Privacypolicy.html")


def antifraud(request):
    return render(request, "VisaPage/Antifruad.html")


def termscondition(request):
    return render(request, "VisaPage/Termscondition.html")


def refundcancellation(request):
    return render(request, "VisaPage/Refundcancelation.html")


def save_cv(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("email")
        contact_no = request.POST.get("contact_no")
        address = request.POST.get("address")
        country = request.POST.get("country")
        job_profile = request.POST.get("job_profile")
        cv_file = request.FILES.get("cv_file")

        try:
            cv_submit = Cvsubmit(
                Name=name,
                email=email,
                contact_no=contact_no,
                address=address,
                country=country,
                job_profile=job_profile,
                cv_file=cv_file,
            )
            cv_submit.full_clean()
            cv_submit.save()
            return redirect("visa_home")
        except ValidationError as e:
            return render(request, "VisaPage/home.html", {"error_message": str(e)})

    return render(request, "VisaPage/home.html")


def connectus(request):
    if request.method == "POST":
        Firstname = request.POST.get("Firstname")
        lastname = request.POST.get("lastname")
        Phone_number = request.POST.get("Phone_number")
        Email = request.POST.get("Email")
        visa_services = request.POST.get("visa_services")
        notes = request.POST.get("notes")

        try:
            contact_us = ContactUs(
                Firstname=Firstname,
                lastname=lastname,
                Phone_number=Phone_number,
                Email=Email,
                visa_services=visa_services,
                notes=notes,
            )
            contact_us.full_clean()
            contact_us.save()
            return HttpResponseRedirect(reverse("visa_home"))
        except:
            pass

    # return render(request, 'VisaPage/home.html')


def appointment(request):
    if request.method == "POST":
        Firstname = request.POST.get("Firstname")
        lastname = request.POST.get("lastname")
        Phone_number = request.POST.get("Phone_number")
        Email = request.POST.get("Email")
        visa_services = request.POST.get("visa_services")
        notes = request.POST.get("notes")
        date = request.POST.get("date")

        try:
            appointment = Appointment(
                Firstname=Firstname,
                lastname=lastname,
                Phone_number=Phone_number,
                Email=Email,
                visa_services=visa_services,
                notes=notes,
                date=date,
            )
            appointment.full_clean()
            appointment.save()
            return HttpResponseRedirect(reverse("visa_home"))
        except:
            pass
