import pytest
from .models import Profile
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
@pytest.mark.django_db
def test_profile(client):
    user = User.objects.create(username='test-username',
                               password='test-password',
                               first_name='test-first_name',
                               last_name='test-last_name',
                               email='test-email')
    Profile.objects.create(user_id=user.id,
                           favorite_city='test-favorite_city'
                           )

    response = client.get(reverse("profiles_index"))

    assert response.status_code == 200
    assert b"test-username" in response.content


@pytest.mark.django_db
def test_profile_detail(client):
    user = User.objects.create(username='test-username',
                               password='test-password',
                               first_name='test-first_name',
                               last_name='test-last_name',
                               email='test-email')
    Profile.objects.create(user_id=user.id,
                           favorite_city='test-favorite_city'
                           )
    response = client.get(reverse("profile", kwargs={"username": user.username}))

    assert response.status_code == 200
    assert b"test-favorite_city" in response.content
