# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def send_contact_email(contact):
    subject = f"New Message from {contact.name}"
    message = f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\n\nMessage:\n{contact.message}"
    recipient_list = ['your_email@example.com']  # Replace with the email address to which the message will be sent
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

@receiver(post_save, sender=Contact)
def contact_post_save(sender, instance, created, **kwargs):
    if created:
        send_contact_email(instance)