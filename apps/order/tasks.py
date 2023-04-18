from django.core.mail import send_mail

def send_confirmation_mail(instance):
    message = f"""
    Здраствуйте, {instance.user.username}!
    Подтвердите заказ на адрес {instance.address}!

    http://127.0.0.1:8000/order/{instance.pk}/confirm/

    Усли это не Вы, игнорируйте это сообщение
    """
    send_mail(
        subject='Подтверждение заказа',
        message=message,
        recipient_list=[instance.user.email],
        fail_silently=False
    )    