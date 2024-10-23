
from notification import Notification

# Clase Employee que actúa como observador
class Employee:
    def __init__(self, name: str):
        self.name = name
    
    def update(self, notification: Notification, message: str) -> None:
        print(f"Notificando a {self.name}:")
        notification.send(message)

# Clase Subject que actúa como el tema al que los empleados se suscriben
class NotificationManager:
    def __init__(self):
        self._subscribers = []
    
    def subscribe(self, employee: Employee):
        self._subscribers.append(employee)
    
    def unsubscribe(self, employee: Employee):
        self._subscribers.remove(employee)
    
    def notify(self, notification: Notification, message: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(notification, message)
