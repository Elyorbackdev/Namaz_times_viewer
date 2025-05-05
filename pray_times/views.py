from django.shortcuts import render
from praytimes import PrayTimes
import datetime

def prayer_times_view(request):
    pt = PrayTimes('MWL')  # MUSLIM_WORLD_LANGUAGE

    # Tashkent koordinatalari
    latitude = 41.3111
    longitude = 69.2797
    timezone = 5  # UTC+5

    today = datetime.date.today()
    times = pt.getTimes(
        (today.year, today.month, today.day),
        (latitude, longitude),
        timezone
    )

    context = {
        'date': today.strftime('%d.%m.%Y'),
        "Bomdod": times['imsak'],
        "Quyosh chiqishi": times['fajr'],
        "Peshin": times['dhuhr'],
        "Asr": times['asr'],
        "Quyosh botishi": times['maghrib'],
        "Shom": times['maghrib'],
        "Xufton": times['isha'],
    }

    return render(request, 'prayer_times.html', context)