import pytest
from .models import Letting, Address
from django.urls import reverse


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_letting(client):
    address = Address.objects.create(number=1,
                                     street='test-street',
                                     city='test-city',
                                     state='test-state',
                                     zip_code='12345',
                                     country_iso_code='FR'
                                     )
    Letting.objects.create(title="test-title", address_id=address.id)
    response = client.get(reverse("lettings_index"))

    assert response.status_code == 200
    assert b"test-title" in response.content


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_letting_detail(client):
    address = Address.objects.create(number=1,
                                     street='test-street',
                                     city='test-city',
                                     state='test-state',
                                     zip_code='12345',
                                     country_iso_code='FR'
                                     )
    letting = Letting.objects.create(title="test-title", address_id=address.id)
    response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))

    assert response.status_code == 200
    assert b"test-street" in response.content
