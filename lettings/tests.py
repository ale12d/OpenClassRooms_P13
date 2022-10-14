import pytest
from .models import Letting, Address
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
    response = client.get("/lettings/")

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
    response = client.get(f"/lettings/{letting.id}/")
    print(response.content)

    assert b"Mountain Drive" in response.content
