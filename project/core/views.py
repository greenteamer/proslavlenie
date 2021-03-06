# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from functions import *
from forms import QuestionForm, NeedForm
from project.forms.forms import BSForm
from models import Article, Page, Question,\
    News, SliderItem, Review, Testimony, Video, Ministry, VideoCategory

from django.core.mail import send_mail
from project.settings import ADMIN_EMAIL

from project.payment.forms import PaymentForm
from project.payment.models import Payment


def indexView(request, template_name="catalog/index.html"):
    user = request.user
    articles = Article.objects.order_by('-id')[:4]
    news = News.objects.order_by("-date")[:5]
    slides = SliderItem.objects.all()[:3]

    # получение ссылок для видео
    cat = VideoCategory.objects.all()
    for c in cat:
        if c.slug == 'main':
            main_video = Video.objects.filter(category=c).last()
            main_video.video = main_video.video[17:]
        elif c.slug == 'pritch':
            pritch_video = Video.objects.filter(category=c).last()
            pritch_video.video = pritch_video.video[17:]
        else:
            videoblog_video = Video.objects.filter(category=c).last()
            videoblog_video.video = videoblog_video.video[17:]

    reviews = Review.objects.order_by("-date")[:3]

    form_question = QuestionForm()
    form_need = NeedForm()

    # Отправляем нужду на почту
    if request.method == "POST" and "need" in request.POST:
        form_need = NeedForm(request.POST)
        if form_need.is_valid():
            form_need.save()
            subject = u'Нужда proslavlenie.ru'
            message = u'телефон: %s \n Имя: %s \n Сообщение: %s \n почта: %s'\
                % (
                    request.POST['phone'],
                    request.POST['name'],
                    request.POST['text'],
                    request.POST['email'])

            send_mail(
                subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL],
                fail_silently=False)

    # Отправляем вопрос на почту
    elif request.method == "POST" and "question" in request.POST:
        postdata = {
            'name': request.POST['name'],
            'phone': request.POST['phone'],
            'text': request.POST['text']
        }
        form_question = QuestionForm(postdata)
        if form_question.is_valid():
            subject = u'Вопрос proslavlenie.ru'
            message = u'телефон: %s \n Имя: %s \n Сообщение: %s \n'\
                % (
                    request.POST['phone'],
                    request.POST['name'],
                    request.POST['text']
                )

            send_mail(
                subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL],
                fail_silently=False)

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def articleView(request, slug, template_name="catalog/article.html"):
    user = request.user
    article = Article.objects.get(slug=slug)
    # мета описание
    meta_title = article.meta_title
    if not meta_title or meta_title == '':
        meta_title = article.name
    meta_description = article.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def newsView(request, id, template_name="catalog/news.html"):
    user = request.user
    news = News.objects.get(id=id)
    # мета описание
    meta_title = news.meta_title
    if not meta_title or meta_title == '':
        meta_title = news.name
    meta_description = news.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def newsAllView(request, template_name="catalog/news_all.html"):
    news_all = News.objects.order_by("-date")
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def reviewsView(request, template_name="catalog/reviews.html"):
    reviews = Review.objects.order_by("-date")
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def reviewView(request, id, template_name="catalog/review.html"):
    review = Review.objects.get(id=id)
    # мета описание
    meta_title = review.meta_title
    if not meta_title or meta_title == '':
        meta_title = review.name
    meta_description = review.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def testimonysView(request, template_name="catalog/reviews.html"):
    testimonys = Testimony.objects.all()
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def testimonyView(request, id, template_name="catalog/testimony.html"):
    user = request.user
    testimony = Testimony.objects.get(id=id)
    # мета описание
    meta_title = testimony.meta_title
    if not meta_title or meta_title == '':
        meta_title = testimony.name
    meta_description = testimony.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def ministryView(request, slug, template_name="catalog/ministry.html"):

    if request.path_info == '/ministry/biblejskie-kursy/':
        form = BSForm();

    if request.method == 'POST' and 'bs_form' in request.POST:
        form = BSForm(request.POST)
        if form.is_valid():
            form.save()
            subject = u'Анкета БШ'
            message = u'ФИО: %s \n Дата рождения: %s \n телефон: %s \n город: %s \n Семейное положение: %s \n Принадлежность к церкви: %s \n Город: %s \n Ф.И.О пастора Церкви: %s \n Член Церкви: %s \n Верует ли в Господа: %s \n Дата спасения: %s \n Призвание: %s \n Форма обучения: %s \n Согласен с правилами: %s'\
                % (
                    request.POST['fio'],
                    request.POST['birth_day'],
                    request.POST['phone'],
                    request.POST['city'],
                    request.POST['family_status'],
                    request.POST['you_church'],
                    request.POST['church_city'],
                    request.POST['pastor_fio'],
                    request.POST.get('is_church_member', False),
                    request.POST.get('is_believer', False),
                    request.POST['salvation_day'],

                    request.POST['you_mission'],
                    request.POST['form_of_study'],
                    request.POST.get('rules', False)
                    )

            send_mail(
                subject, message, 'teamer777@gmail.com', ['bk.tomsk@mail.ru'],
                fail_silently=False)

    user = request.user
    ministry = Ministry.objects.get(slug=slug)
    ministry.video = ministry.video[17:]
    # мета описание
    meta_title = ministry.meta_title
    if not meta_title or meta_title == '':
        meta_title = ministry.name
    meta_description = ministry.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def pageView(request, slug, template_name="core/page.html"):
    page = Page.objects.get(slug=slug)
    # мета описание
    meta_title = page.meta_title
    if not meta_title or meta_title == '':
        meta_title = page.name
    meta_description = page.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def questionsView(request, template_name="core/questions.html"):
    questions = Question.objects.all()
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))
