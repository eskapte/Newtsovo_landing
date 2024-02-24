from django.shortcuts import render
from django.views.generic import DetailView

from landing.models import House, AdditionalInfo, WellnessTreatment, Action, OurProduct, Event, News


def index(request):
    houses = House.objects.order_by("start_price").all()
    additional_info = AdditionalInfo.objects.all()
    wellness_treatments = WellnessTreatment.objects.all()
    actions = Action.objects.all()
    available_products = OurProduct.objects.exclude(is_available=False)[:10]
    future_events = sorted(
        filter(lambda event: event.is_passed() is False, Event.objects.all()),
        key=lambda event: event.date)[:5]
    latest_news = News.objects.all()[:5]

    return render(
        request,
        'landing/index.html',
        {
            'houses': houses,
            'additional_info': additional_info,
            'wellness_treatments': wellness_treatments,
            'actions': actions,
            'our_products': available_products,
            'future_events': future_events,
            'news': latest_news
        })


def events(request):
    events_qs = Event.objects.all()
    future_events = sorted(filter(lambda event: event.is_passed() is False, events_qs), key=lambda event: event.date)
    past_events = sorted(filter(lambda event: event.is_passed() is True, events_qs), key=lambda event: event.date)

    return render(request, "landing/events.html", {
        'future_events': future_events,
        'past_events': past_events
    })


class EventDetailView(DetailView):
    model = Event
    template_name = 'landing/event_detail.html'


def news(request):
    all_news = News.objects.all()
    return render(
        request,
        'landing/news.html',
        {'news': all_news})


class NewsDetailView(DetailView):
    model = News
    template_name = 'landing/news_detail.html'


def our_products(request):
    all_products = OurProduct.objects.all()
    return render(
        request,
        'landing/our-products.html',
        {'products': all_products})