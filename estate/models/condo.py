from django.db import models
from multiselectfield import MultiSelectField


class Condo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    number_of_floors = models.IntegerField(default=1)

    # admin only
    juristic_persons_number = models.TextField(max_length=25)
    common_fee_account = models.TextField(max_length=25)

    AMENITY_TYPES = (
        ('elevator', 'Elevator'),
        ('parking_lot', 'Parking Lot'),
        ('cctv', 'CCTV'),
        ('security', 'Security'),
        ('wifi', 'WiFi'),
        ('swimming_pool', 'Swimming Pool'),
        ('sauna', 'Sauna'),
        ('garden', 'Garden'),
        ('playground', 'Playground'),
        ('gym', 'Gym'),
        ('shop', 'Shop'),
        ('restaurant', 'Restaurant'),
    )

    amenities = MultiSelectField(
        choices=AMENITY_TYPES, default=None,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the name of the condo."""
        return self.name

    def get_rooms(self):
        rooms = self.room_set.all()
        return rooms

    def get_available_units(self):
        available_units = 0
        for unit in self.get_rooms():
            if not unit.still_on_contract:
                available_units += 1
        return available_units

    def get_all_register_unit(self):
        all_units = 0
        for unit in self.get_rooms():
            all_units += 1
        return all_units

    def get_images(self):
        return self.condoimages_set.all()
        # first().image.url.replace('/estate', '..', 1)

    def get_first_image(self):
        return self.condoimages_set.first().image.url.replace('/estate', '', 1)

    def get_class_name(self):
        return 'Condo'

def conference_directory_path(instance, filename):
    return 'estate/static/estate/images/user_upload/condo/condo_id_{0}/{1}'.format(instance.condo.id, filename)


class CondoImages(models.Model):
    condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=conference_directory_path)
