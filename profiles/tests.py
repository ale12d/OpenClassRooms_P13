import pytest
from .models import Profile
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
@pytest.mark.django_db
def test_profile(client):
    user = User.objects.create(username='Batman',
                               password='jokerwillpay4it',
                               first_name='Bruce',
                               last_name='Wayne',
                               email='bruce.wayne@')
    Profile.objects.create(user_id=user.id,
                           favorite_city='Paris'
                           )

    response = client.get(reverse("profiles_index"))

    assert response.status_code == 200
    assert b"Batman" in response.content


@pytest.mark.django_db
def test_profile_detail(client):
    user = User.objects.create(username='Batman',
                               password='jokerwillpay4it',
                               first_name='Bruce',
                               last_name='Wayne',
                               email='bruce.wayne@')
    Profile.objects.create(user_id=user.id,
                           favorite_city='Paris'
                           )
    response = client.get(reverse("profile", kwargs={"username": user.username}))

    assert b"Paris" in response.content
