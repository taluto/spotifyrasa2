## spotify new account email happy path
* greet
  - utter_greet
  - account_form
  - form{"name": "account_form"}
  - form{"name": null}
  - utter_next
* affirm
  - utter_ask_language
* inform{"language": ["English", "Hindi"]}
  - slot{"language": ["English", "Hindi"]}
  - utter_gotit
