from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'index.html')

def support(request):
    return render(request,'contact.html')


def lesson(request):
    return render(request,'lesson.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():
            # Extract data from the form

            contact_instance = form.save()
            
            # Prepare email content
            subject = "Thanks for using Syntax School"
            body = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        color: #333;
                        padding: 20px;
                        margin: 0;
                    }}
                    .container {{
                        background-color: #ffffff;
                        border-radius: 8px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        max-width: 600px;
                        margin: auto;
                    }}
                    .header {{
                        background-color: #4CAF50; /* Green */
                        color: white;
                        padding: 10px 15px;
                        text-align: center;
                        border-radius: 8px 8px 0 0;
                    }}
                    .footer {{
                        margin-top: 20px;
                        text-align: center;
                        font-size: 12px;
                        color: #777;
                    }}
                    .message {{
                        font-size: 16px;
                        line-height: 1.5;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Contact Confirmation</h1>
                    </div>
                    <div class="message">
                        <p><strong>Name:</strong> {name}</p>
                        <p><strong>Email:</strong> {email}</p>
                    </div>
                    <div class="footer">
                        <p>Our team will contact you within 24 hours.</p>
                    </div>
                </div>
            </body>
            </html>
            """.format(name=contact_instance.name, email=contact_instance.email,)
        
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [contact_instance.email]    # Make sure this is a list

            # Send the email
            send_mail(
                subject,
                'Thanks for contacting us',  # Plain text message
                email_from,
                recipient_list,
                html_message=body,
                fail_silently=False,
            )

            # Render the success page
            return render(request, 'success.html') 
    else:
        form = ContactForm()  # Initialize an empty form for GET request

    # Render the contact form template with the form context
    context = {'form': form}
    return render(request, 'contact.html', context)