from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactMessagesForm


def contact_us(request):
    if request.method == 'POST':
        messages_form = ContactMessagesForm(request.POST)

        if messages_form.is_valid():
            try:
                messages_form.save()
                messages.success(request, "Your message to us has been \
                successfully sent. We will be in contact as soon as possible")
                return redirect(reverse('home'))
            except Exception as e:
                messages.error(request, "There was an error sending your \
                message, please try to send it again")
                return redirect(reverse('contact_us'))
        else:
            messages.error(request, "There was an error sending your message, \
            please try to send it again")
            return redirect(reverse('contact_us'))
    else:
        messages_form = ContactMessagesForm()

    template = 'contact_us/contact_us.html'
    context = {'form': messages_form}
    return render(request, template, context=context)
