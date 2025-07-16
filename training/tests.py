import pytest
from django.test import TestCase

# Create your tests here.
def test_env():
    assert 1

@pytest.mark.django_db
def test_env_db():
    assert 1
