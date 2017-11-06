# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from .models import Producer


class  ProducerTestCase(TestCase):
    def setUp(self):
     uid = Producer.objects.latest('uid').uid + 1
     Producer.objects.create(uid=uid, name="test", last_name="test", email="test@test.com", address="test address",
                                               password="test",
                                               phone_number="1234",latitude="0",longitude="0", url="url",farmurl="farmurl" )
     def test_addedproducer(self):
        producer = Producer.objects.get(name="test")
        self.assertEqual(producer.last_name, "test")
        self.assertEqual(producer.email, "test@test.com")
        self.assertEqual(producer.password, "test")
        self.assertEqual(producer.phone_number, "1234")

