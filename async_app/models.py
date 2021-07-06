from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    schedule_id = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        schedule = Schedule.objects.create(
            name=self.__str__(),
            func="demo_app.services.send_email",
            args=f"'{self.email}'",
            schedule_type=Schedule.DAILY,
        )
        # Save the model with the schedule id
        self.schedule_id = schedule.pk
        super().save(*args, **kwargs)