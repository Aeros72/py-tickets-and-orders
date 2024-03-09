from db.models import User
from django.contrib.auth import get_user_model


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> None:
    user = get_user_model().objects.create_user(
        username=username
    )

    user.set_password(password)

    if email:
        user.email = email

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    user.save()


def get_user(user_id: int) -> User:
    return get_user_model().objects.get(id=user_id)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    user = get_user(user_id)
    parameters = {
        "username": username,
        "password": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name
    }

    for parameter, value in parameters.items():
        if value:
            setattr(user, parameter, value)

    if password:
        user.set_password(password)

    user.save()