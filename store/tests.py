# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from .models import Producer, AdminOffer, Notification


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

class EditOfferTestCase(TestCase):
    def setUp(self):
        id = 1


    def test_editoffer(self):
        actual = AdminOffer.objects.get(id=id)
        actual.unit_price = 5000
        actual.save()
        peticion = AdminOffer.objects.get(id=id)
        self.assertEqual( peticion.unit_price, "5000")


class addNotification(TestCase):
    def setUp(self):
        id = 1

    def test_add_notification(self):
        nueva = Notification.objects.create(title="prueba", text="prueba", img="prueba")
        buscado = Notification.objects.get(id=1)
        self.assertEqual(nueva.title, buscado.title)

    def test_get_all_notifications(self):
        vieja = Notification.objects.get.all()
        nueva = Notification.objects.create(title="prueba", text="prueba", img="prueba")
        nueva.save()
        self.assertEqual(len(vieja)+1,len(nueva))
















