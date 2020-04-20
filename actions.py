from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
class AccountForm(FormAction):
   """Example of a custom form action"""

   def name(self):
       # type: () -> Text
       """Unique identifier of the form"""

       return "account_form"

   @staticmethod
   def required_slots(tracker):
       # type: () -> List[Text]
       """A list of required slots that the form has to fill"""
       if tracker.get_slot('account') == 'Email':
           return ["account", "Emailid", "Date", "Gender", "Name"]
       elif:
           if tracker.get_slot('account') == 'Phone':
           return ["account","cellphone", "Date", "Gender", "Name"]

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
       """Define what the form has to do
           after all required slots are filled"""

       # utter submit template
       dispatcher.utter_template('utter_submit', tracker)
       return []
