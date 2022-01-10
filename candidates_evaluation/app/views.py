from django.shortcuts import render,redirect
from .models import Candidate,Registration
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.


def validation_user(formdata):
    name = formdata.get('login_name')
    email = formdata.get('login_email')
    if Registration.objects.filter(email=email).exists():
        message = 'Email already exist'
        return message
    password = formdata.get('login_password')
    confirm_password = formdata.get('login_confirm')
    if not name or type(name) != str:
        message = 'Invalid Name'
        return message
    if not email:
        message = 'Please Enter valid email'
        return message
    if len(password) <= 6 or password.isalpha() or password.isdigit() \
            or not password:
        message = 'Please Enter valid password, Password must be ' \
                  'contains Characters and numbers'
        return message
    if not confirm_password:
        message = 'Please Enter confirm password'
        return message
    if password != confirm_password:
        message = 'Password is Not matching'
        return message


def validation_candidates(formdata):
    name = formdata.get('name')
    email = formdata.get('email')
    if Candidate.objects.filter(email=email).exists():
        message = 'Email already exist'
        return message
    cover_letter = formdata.get('cover_letter')
    cv = formdata.get('cv')
    like = formdata.get('like')
    if not name or type(name) != str:
        message = 'Invalid Name'
        return message
    if not email:
        message = 'Please Enter valid email'
        return message
    if not cover_letter:
        message = 'Please Upload cover letter'
        return message
    if not cv:
        message = 'Please Upload CV'
        return message
    if not like:
        message = 'Please Check Yes or No'
        return message


def add_candidates(request):
    message = ''
    if request.method == 'POST':
        formdata = request.POST
        error = validation_candidates(formdata)
        if error:
            return render(request, 'app/candidate.html',
                          {"name_error": error})
        else:
            candidate = Candidate(name=formdata.get('name'),
                                  email=formdata.get('email'),
                                  web=formdata.get('web_address'),
                                  cover_letter=formdata.get('cover_letter'),
                                  cv=formdata.get('cv'),
                                  like=formdata.get('like'))
            candidate.save()
            message = 'Information successfully uploaded'
    return render(request, 'app/candidate.html', {"context": message})


def add_registration(request):
    message = ''
    if request.method == 'POST':
        formdata = request.POST
        error = validation_user(formdata)
        if error:
            return render(request, 'app/registr.html', {"context": error})
        else:
            password = make_password(formdata.get('login_password'))
            confirm_password = make_password(formdata.get('login_confirm'))
            registration = Registration(name=formdata.get('login_name'),
                                        email=formdata.get('login_email'),
                                        password=password,
                                        confirm_password=confirm_password)
            registration.save()
            messages.info(request, 'Registration Successfully Completed')
            return redirect('http://127.0.0.1:8000/login/')
    return render(request, 'app/registr.html',{"context": message})


def authenticate_user(request):
    message = ''
    if request.method == 'POST':
        formdata = request.POST
        user = formdata.get('user')
        password = formdata.get('password')
        login = Registration.objects.filter(name=user,password=password).first()
        if login:
            request.session['userinfo'] = user
            return redirect('http://127.0.0.1:8000/allcandidates/')
        else:
            messages.info(request,'Invalid Cridentials')
            return redirect('http://127.0.0.1:8000/login/')
    return render(request, 'app/login.html')


def get_all_candidates(request):
    if 'userinfo' in request.session:
        candidates_list = Candidate.objects.all()
        return render(request, 'app/list_candidates.html', {"candidates": candidates_list})
    return render(request, 'app/login.html')


def log_out(request):
    del request.session['userinfo']
    return redirect('http://127.0.0.1:8000/login/')










