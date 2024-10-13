from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMessage
from django.http import HttpResponse


# def index(request):

# 	if request.method == 'POST':
# 		pesan = request.POST['message']
# 		# pesan1 = request.POST['message1']
#           # message = f"message :  {pesan}\nemail :  {pesan1}"
# 		message = f"message :  {pesan}"

# 		# Mengirim email ke alamat email yang ditentukan ketika user menekan button
# 		send_mail('Contact Form',
# 		message, 
# 		settings.EMAIL_HOST_USER,
# 		['farkhanmuzaki8@gmail.com'], 
# 		fail_silently=False)
# 	return render(request, 'app/index.html')
	
def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        file = request.FILES.get('file')

        email = EmailMessage(
            'Subject here',
            message,
            'farkhanmuzaki8@gmail.com',
            ['farkhanmuzaki8@gmail.com'],
        )

        if file:
            email.attach(file.name, file.read(), file.content_type)

        email.send()
     #    return HttpResponse('Email sent!')

    return render(request, 'app/index.html')