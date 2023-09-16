from django.test import TestCase

from django.urls import reverse
import pytest

from django.urls import reverse
import pytest

from tutorials.models import Tutorial
@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial
    assert tutorial.title == "Pytest"