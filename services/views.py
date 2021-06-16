from django.shortcuts import render, redirect, get_object_or_404
from .models import Rooms, Booking
from .forms import BookingForm
from datetime import date
from django.core.mail import send_mail


def booking(request, pk):
    obj = get_object_or_404(Rooms, pk=pk)
    form = BookingForm()
    room = Rooms.objects.filter(id=pk)
    if request.method == "POST":
        start_date = request.POST['starting_date']
        start_date = start_date.split('-')
        start_date = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))

        end_date = request.POST['end_date']
        end_date = end_date.split('-')
        end_date = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
        delta = (end_date - start_date).days

        fname = request.POST['first_name']
        lname = request.POST['last_name']
        room_name = request.POST['room_name']
        email_addy = request.POST['email']

        room_price = request.POST['room_price']
        print(room_price)
        total_price = int(room_price) * delta

        form = BookingForm(request.POST)
        if form.is_valid():
            # TODO some cleaning

            # Adding missing values and saving to db
            new_form = form.save(commit=False)
            new_form.total_sum = total_price
            new_form.choice = room_name
            new_form.save()
            form.save()

            # TODO send email (after payment)
            subject = f'Бронь на базе Вершина "ДеЛюкс"!'
            message = f'Добрый день {fname} {lname},\n'\
                      f'Вы успешно забронировали "{room_name}" на базе Вершина ДеЛюкс от {start_date} до {end_date}! ' \
                      f'Хорошего отдыха!\n\nС уважением, \nКоманда Вершины "ДеЛюкс"'
            print(subject)
            print(message)
            send_mail(subject, message,
                      'goshasapps@gmail.com',
                      [str(email_addy)],
                      fail_silently=True)
            return redirect('services:rooms')  # redirects to the payment page

    context = {
        'room': room,
        'form': form,
    }
    return render(request, 'services/booking.html', context)


def rooms(request):
    # form = BookingForm()
    # if request.method == "POST":
    #     start_date = request.POST['starting_date']
    #     start_date = start_date.split('-')
    #     start_date = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    #
    #     end_date = request.POST['end_date']
    #     end_date = end_date.split('-')
    #     end_date = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
    #     delta = (end_date - start_date).days
    #
    #     room_name = request.POST['room_name']
    #
    #     price = [room.price for room in Rooms.objects.filter(name=room_name)]
    #     price = int(price[0])
    #     total_price = int(price) * delta
    #
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         # TODO some cleaning
    #
    #         # Adding missing values and saving to db
    #         new_form = form.save(commit=False)
    #         new_form.total_sum = total_price
    #         new_form.choice = room_name
    #         new_form.save()
    #         form.save()
    #
    #         # TODO send email (after payment)
    #
    #         return redirect('services:rooms')  # redirects to the payment page
    #     else:
    #
    #         print('FuuuuckkkkFUCCK')
    #
    all_rooms = Rooms.objects.all()
    context = {
        'rooms': all_rooms,
        # 'form': form,
    }
    return render(request, 'services/rooms.html', context)


def boats(request):
    return render(request, 'services/boats.html')


def parking(request):
    return render(request, 'services/parking.html')


def egery(request):
    return render(request, 'services/egery.html')
