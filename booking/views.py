import re
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookForm, ConfirmForm, NameForm
from .models import Book


@login_required
def BookUI(request):

    # Show booking form with POST request
    form = BookForm(request.POST)

    if form.is_valid():
        # Preprocessing for sessions
        date = json.dumps(form.cleaned_data['date'],cls=DjangoJSONEncoder)
        time = json.dumps(form.cleaned_data['time'],cls=DjangoJSONEncoder)
        date_re = re.sub('[^a-zA-Z0-9-_*.]','', date)
        time_re = time.replace('"', '')
        phone_format = form.cleaned_data['phone_number']
        phone_number = str(phone_format).replace('+', '')

        # Initiate sessions
        request.session['date'] = date_re
        request.session['time'] = time_re
        request.session['phone_number'] = phone_number

        # Compare selected date and time to records in database
        check_date_time = Book.objects.filter(date=date_re, time=time_re).values('date', 'time')

        # Check availability the selected date and time
        if check_date_time:
            # Show alert message
            messages.info(request, 'Sorry, someone has made an appointment at the selected time. Please choose another time!')
        else:
            # Go to confirm page
            return HttpResponseRedirect('confirm/')

    else:
        # Reload  form if form is invalid
        form = BookForm()

    # Context dictionary for template tagging
    context = {'form': form}

    # Return an HttpResponse by combining template and context dictionary
    return render(request, 'booking/new.html', context)


@login_required
def ConfirmUI(request):

    # Declare variable for sessions
    date = request.session['date']
    time = request.session['time']
    phone_number = request.session['phone_number']

    # Show confirm form and name form with POST request
    confirmform = ConfirmForm(request.POST)
    ## Instance model relation with the current user
    userform = NameForm(request.POST, instance=request.user)

    if confirmform.is_valid() and userform.is_valid():
        # Create new object for Book model
        book = Book()
        # Initiate sessions to record in database
        book.date = date
        book.time = time
        ## Initiate form field data to record in database
        book.service = confirmform.cleaned_data['payment_type']
        book.phone_number = phone_number
        # Initiate user to the current user
        book.user = request.user
        # Save all record to database
        book.save()
        # Save all user change info field to database
        userform.save()

        # Finish booking step form, go to booking history
        return HttpResponseRedirect('history/')

    else:
        # Reload confirm form and user form if form is invalid
        confirmform = ConfirmForm()
        userform = NameForm(instance=request.user)

    context = {'confirmform': confirmform, 'nameform': userform}

    return render(request, 'booking/confirm.html', context)


@login_required
def HistoryUI(request):

    # Show booking history of the current user
    history = Book.objects.filter(user=request.user)

    context = {'history': history}

    return render(request, 'booking/history.html', context)
