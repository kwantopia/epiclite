from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import uuid, json

# Create your tests here.

class SimpleTest(TestCase):

  def setUp(self):
    self.client = Client()

  def runTest(self):
    pass

  def test_creating_epics(self):
    connect_device_id = str(uuid.uuid4())
    # open the app
    response = self.client.post(reverse("app-opened"), {
      "device_id": connect_device_id,
      "location": "POINT(23.42334 -72.23432)"
      })

    # start an epic, will return the device id from session and an epic number
    epic_start_response = self.client.get(reverse("start-epic"))

    epic_start = json.loads(epic_start_response.data)

    # create a wake up alarm that asks you to run
    response = self.client.post(reverse("epic-list"), {
        "organizer_id": connect_device_id,
        "user": None,
        "title": "Wake up at 7 AM for jogging",
        "epic_num": epic_start["epic_num"],
        "location": "POINT(23.42334 -72.23432)",
        "address": None,
        "city": None,
        "state": None,
        "zipcode": None,
        "country": None,
        "description": "Feel free to join me for early jogging around Charles River",
        "target_day": "2014-02-15",
        "target_time": "2014-02-15T07:00:00+03:00",
        "public": None,
        "repeated": 1,
      })

    # start an epic, will return the device id from session and an epic number
    epic_start_response = self.client.get(reverse("start-epic"))

    # create a coffee catchup
    response = self.client.post(reverse("epic-list"), {
        "organizer_id": connect_device_id,
        "user": None,
        "title": "Catch up for coffee",
        "epic_num": epic_start["epic_num"],
        "location": "POINT(24.42334 -70.23432)",
        "address": "1369 Coffee House",
        "city": "Cambridge",
        "state": "MA",
        "zipcode": "02139",
        "country": "US",
        "description": "Let's catch up on how things are going with your business",
        "target_day": "2014-02-16",
        "target_time": "2014-02-16T15:00:00+03:00",
        "public": None,
        "repeated": 1,
      })


    # start an epic, will return the device id from session and an epic number
    epic_start_response = self.client.get(reverse("start-epic"))

    # create a date, dinner at Casa Romero
    response = self.client.post(reverse("epic-list"), {
        "organizer_id": connect_device_id,
        "user": None,
        "title": "Catch up for coffee",
        "epic_num": epic_start["epic_num"],
        "location": "POINT(24.42334 -70.23432)",
        "address": "1369 Coffee House",
        "city": "Cambridge",
        "state": "MA",
        "zipcode": "02139",
        "country": "US",
        "description": "Let's catch up on how things are going with your business",
        "target_day": "2014-02-16",
        "target_time": "2014-02-16T15:00:00+03:00",
        "public": None,
        "repeated": 1,
      })

    # start an epic, will return the device id from session and an epic number
    epic_start_response = self.client.get(reverse("start-epic"))
    # create a house cleaning activity
    response = self.client.post(reverse("epic-list"), {
        "organizer_id": connect_device_id,
        "user": None,
        "title": "Cleanup My Place",
        "epic_num": epic_start["epic_num"],
        "location": "POINT(24.42334 -70.23432)",
        "address": "369 Franklin St. 101",
        "city": "Cambridge",
        "state": "MA",
        "zipcode": "02139",
        "country": "US",
        "description": "This is just a reminder for me to cleanup my place",
        "target_day": "2014-02-17",
        "target_time": "2014-02-17T15:00:00+03:00",
        "public": False,
        "repeated": 1,
      })

    # start an epic, will return the device id from session and an epic number
    epic_start_response = self.client.get(reverse("start-epic"))
    # create a meeting with 3 other friends to get together for ice saking
    response = self.client.post(reverse("epic-list"), {
        "organizer_id": connect_device_id,
        "user": None,
        "title": "Weekday Ice Skate Outing",
        "epic_num": epic_start["epic_num"],
        "location": "POINT(24.42334 -70.23432)",
        "address": "Frog Pond",
        "city": "Boston",
        "state": "MA",
        "zipcode": "02125",
        "country": "US",
        "description": "It's a special night for ice skating at the frog pond",
        "target_day": "2014-02-20",
        "target_time": "2014-02-20T20:00:00+03:00",
        "public": None,
        "repeated": 1,
      })    

  def test_join_epic(self):
    # need to join epic as another user

    # join epic for the ice skating get together

    # join epic for date dinner

    # join public epic to wake up and run
    pass

  def test_active_epics(self):
    # shows epics you have created 
    # Epic.objects.filter(organizer_id="Your ID")
    # and joined
    # EpicSubscription.objects.filter(participant_id= "Your ID")
    # with different flags
    pass

  def test_public_epics(self):

    # show list of public epics that you haven't organized

    pass

  def test_leave_epic(self):
    # when you want to bail out of an epic


    # leave all epics you joined above

    pass