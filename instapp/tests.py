
from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestCase(TestCase):
    def setup(self):
        Image.objects.create(title='People', img_description='People having fun')
        Image.objects.create(title='Travelling', img_description='Traveling vehicle')

    def test_Image_create_(self, name= 'title', img_description= 'img_description'):
        return Image.objects.create(title=name, img_description=img_description)

    def test_Image_test_(self):
        obj1 = Image.objects.get(title = 'People')
        obj2 = Image.objects.get(title = 'Travelling')
       
        self.assertEqual(obj1.title,('People'))
        self.assertEqual(obj1.title,('Travelling'))
        self.assertEqual(obj1.img_description,('People having fun'))
        self.assertEqual(obj1.img_description,('Traveling vehicle'))

class categoriesTest(TestCase):
    def setUp(self):
        self.nature = Category(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))

class LocationTest(TestCase):
    def setUp(self):
        self.nairobi = Location(name='nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))

