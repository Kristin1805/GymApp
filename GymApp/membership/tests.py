from django.test import TestCase

from GymApp.people.models import People


# Create your tests here.
class PersonTestCase(TestCase):
    def setUp(self):
        People.objects.create(
                                first_name='Person',
                                last_name='Persona',
                                mobile_number='0899966340',
                                email='person27@gmail.com',



                            )

    def test_member(self):
        check = People.objects.get(first_name='Person')
        print(check)