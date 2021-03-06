from django.db import models
from .condo import Condo
from .owner import Owner


class Room(models.Model):
    condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.RESTRICT)
    number = models.CharField(max_length=10, default="1")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    # admin only
    still_on_contract = models.BooleanField(default=False)
    # contract_over = models.DateTimeField('contract over')

    price_for_rent = models.FloatField(default=0)
    price_for_sell = models.FloatField(default=0)
    floor_number = models.CharField(max_length=10, default="1")
    number_of_bedroom = models.IntegerField(default=1)
    number_of_bathroom = models.IntegerField(default=1)
    area = models.FloatField(default=0)  # in square meters? -> sure

    def __str__(self):
        """Return the title of the room."""
        return self.title

    def get_images(self):
        return self.roomimages_set.all()

    def get_first_image(self):
        return self.roomimages_set.first().image.url.replace('/estate', '', 1)
    
    def get_class_name(self):
        return 'Room'


def conference_directory_path(instance, filename):
    return 'estate/static/estate/images/user_upload/room/room_id_{0}/{1}'.format(instance.room.id, filename)


class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=conference_directory_path)
