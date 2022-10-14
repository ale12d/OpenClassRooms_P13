import pytest
from .models import Letting, Address
from django.urls import reverse


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_letting(client):
    address = Address.objects.create(number=1007,
                                     street='Mountain Drive',
                                     city='Gotham City',
                                     state='NJ',
                                     zip_code='12345',
                                     country_iso_code='USA'
                                     )
    Letting.objects.create(title="Wayne Manor",
                           address_id=address.id)
    response = client.get(reverse("lettings_index"))

    assert response.status_code == 200
    assert b"Wayne Manor" in response.content


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_letting_detail(client):
    address = Address.objects.create(number=1007,
                                     street='Mountain Drive',
                                     city='Gotham City',
                                     state='NJ',
                                     zip_code='12345',
                                     country_iso_code='USA'
                                     )
    letting = Letting.objects.create(title="Wayne Manor", address_id=address.id)
    response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))

    assert b"Mountain Drive" in response.content
