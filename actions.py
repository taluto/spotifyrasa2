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
       #checks account slot to determine questions
       if tracker.get_slot('account') == 'Email':
           return ["Emailid", "Date", "Gender", "Name"]
       #checks account slot to determine questions
       elif tracker.get_slot('account') == 'Phone':
           return ["cellphone", "Date", "Gender", "Name"]

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
       """Define what the form has to do
           after all required slots are filled"""

       # utter submit template
       dispatcher.utter_message(template='utter_submit')
       return []


class PreferenceForm(FormAction):
   """Example of a custom form action"""

   def name(self):
       # type: () -> Text
       """Unique identifier of the form"""

       return "preference_form"

   @staticmethod
   def required_slots(tracker):
       # type: () -> List[Text]
       """A list of required slots that the form has to fill"""
       return ["language", "artist"]

   def slot_mappings(self):
       # type: () -> Dict[Text, Union[Dict, List[Dict]]]:
    """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

    return {
        "language": self.from_entity(entity="language", intent="inform"),
        "artist": self.from_entity(entity="Name", intent="inform"),
    }

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
       """Define what the form has to do
           after all required slots are filled"""

       # utter_gotit template
       dispatcher.utter_message(template='utter_gotit')
       return []
