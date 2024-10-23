from notification import NotificationFactory
from decorators import SignatureDecorator, UrgencyTemplateDecorator
from observer import NotificationManager, Employee

# Factory para crear notificaciones
factory = NotificationFactory()

# Crear sistema de notificaciones (Observer)
manager = NotificationManager()
employee1 = Employee("Sarah")
employee2 = Employee("Miguel")

manager.subscribe(employee1)
manager.subscribe(employee2)

# Crear y personalizar notificación (Factory y Decorator)
notification = factory.create_notification('sms')
notification = SignatureDecorator(notification, "Equipo de Trabajo")
notification = UrgencyTemplateDecorator(notification)

# Notificar a los empleados (Observer)
manager.notify(notification, "Ha ocurrido un cambio importante en la empresa")
