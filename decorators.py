
from notification import Notification

# Decorador base para notificaciones
class NotificationDecorator(Notification):
    def __init__(self, wrapped: Notification):
        self._wrapped = wrapped
    
    def send(self, message: str) -> None:
        self._wrapped.send(message)

# Decorador para añadir firma
class SignatureDecorator(NotificationDecorator):
    def __init__(self, wrapped: Notification, signature: str):
        super().__init__(wrapped)
        self.signature = signature
    
    def send(self, message: str) -> None:
        message_with_signature = f"{message}\n\nFirma: {self.signature}"
        self._wrapped.send(message_with_signature)

# Decorador para añadir urgencia
class UrgencyTemplateDecorator(NotificationDecorator):
    def send(self, message: str) -> None:
        urgent_message = f"!!!URGENTE!!!\n{message}"
        self._wrapped.send(urgent_message)
