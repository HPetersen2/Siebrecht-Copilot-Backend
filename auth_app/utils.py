from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def send_reset_password_email(saved_account, verification_link):
    """Sends a password reset email with a verification link."""
    subject = 'Reset your password'
    from_email = None
    context = {
        'email': saved_account,
        'verification_link': verification_link,
    }
    text_content = render_to_string(
        'emails/reset_password_email.txt', context)
    html_content = render_to_string(
        'emails/reset_password_email.html', context)

    email = EmailMultiAlternatives(
        subject, text_content, from_email, [saved_account.email])
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)