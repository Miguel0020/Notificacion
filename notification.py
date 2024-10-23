
from abc import ABC, abstractmethod

# Interface para la notificación
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

# Notificación vía Email
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Enviando Email: {message}")

# Notificación vía SMS
class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Enviando SMS: {message}")

# Notificación Push
class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Enviando Notificación Push: {message}")

# Factory para crear notificaciones
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        if notification_type == 'email':
            return EmailNotification()
        elif notification_type == 'sms':
            return SMSNotification()
        elif notification_type == 'push':
            return PushNotification()
        else:
            raise ValueError("Tipo de notificación no soportado")
