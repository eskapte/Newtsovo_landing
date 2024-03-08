import json
from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError, HttpResponse
from django.shortcuts import render
from landing.models import House, AdditionalInfo, WellnessTreatment, Action, OurProduct, Event, News, Booking, OurPet


def index(request):
    houses = House.objects.all()
    additional_info = AdditionalInfo.objects.all()
    wellness_treatments = WellnessTreatment.objects.all()
    actions = Action.objects.all()
    available_products = OurProduct.objects.exclude(is_available=False)[:10]
    future_events = sorted(
        filter(lambda event: event.is_passed() is False, Event.objects.all()),
        key=lambda event: event.date)[:5]
    latest_news = News.objects.all()[:5]
    our_pets = OurPet.objects.all()

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
            'news': latest_news,
            'our_pets': our_pets
        })


def events(request):
    events_qs = Event.objects.all()
    future_events = sorted(filter(lambda event: event.is_passed() is False, events_qs), key=lambda event: event.date)
    past_events = sorted(filter(lambda event: event.is_passed() is True, events_qs), key=lambda event: event.date)

    return render(request, "landing/events.html", {
        'future_events': future_events,
        'past_events': past_events
    })


def news(request):
    all_news = News.objects.all()
    paginator = Paginator(all_news, 5)

    page_number = request.GET.get('page') or 1
    news_page = paginator.get_page(page_number)

    return render(
        request,
        'landing/news.html',
        {'news': news_page})


def our_products(request):
    all_products = OurProduct.objects.all()
    return render(
        request,
        'landing/our-products.html',
        {'products': all_products})


def add_booking(request):
    if not request.method == 'POST':
        return HttpResponseBadRequest("The request type must be POST")

    if not request.body:
        return HttpResponseBadRequest("The request body is empty")

    form_data = json.loads(request.body.decode('utf-8'))
    print(form_data)

    new_booking = Booking(
        fio=form_data['fio'],
        phone_number=form_data['phone'],
        adults_count=form_data['adults'],
        childs_count=form_data['childrens'],
        desired_dates=form_data['desired_dates'],
        booking_identifier_id=form_data['booking_identifier'],
        is_has_whatsapp=form_data['whatsapp']
    )

    try:
        new_booking.save()
    except Exception as e:
        err_message = "An error occured while saveing new booking " + str(e)
        print(err_message)
        return HttpResponseServerError(err_message)

    return HttpResponse(status=201)


def get_booked_days(request, booking_identifier_id):
    if not booking_identifier_id or booking_identifier_id == 0:
        return HttpResponseBadRequest("booking_identifier_id is " + str(booking_identifier_id))

    bookings = list(Booking.objects
                    .filter(booking_identifier_id=booking_identifier_id)
                    .exclude(status='c')
                    .values('desired_dates'))

    booked_ranges_strings = list(filter(lambda days: "-" in days['desired_dates'], bookings))
    single_booked_dates = [day for day in bookings if day not in booked_ranges_strings]

    booked_dates = set()

    # работаем с промежутками дат для суточной аренды
    try:
        for booked_day in booked_ranges_strings:
            splited = booked_day['desired_dates'].split('-')
            if not len(splited) == 2:
                continue

            start_date = datetime.strptime(splited[0].strip(), '%d.%m.%Y')
            end_date = datetime.strptime(splited[1].strip(), '%d.%m.%Y')

            current_date = start_date
            while current_date <= end_date:
                booked_dates.add(current_date.strftime('%Y.%m.%d'))
                current_date += timedelta(days=1)
    except Exception as e:
        print("failed to get range booked days: " + str(e))

    date_time_formats = ['%d.%m.%Y %H:%M', '%d.%m.%Y']

    try:
        if 'all' in request.GET:
            for booking in single_booked_dates:
                booked_days = booking['desired_dates'].split(',')
                for booked_day in booked_days:
                    for date_time_format in date_time_formats:
                        try:
                            parsed_date = datetime.strptime(booked_day.strip(), date_time_format).strftime('%Y.%m.%d')
                            booked_dates.add(parsed_date)
                        except ValueError:
                            pass
    except Exception as e:
        print("failed to get single booked days: " + str(e))

    return JsonResponse({'booked_dates': list(booked_dates)})
