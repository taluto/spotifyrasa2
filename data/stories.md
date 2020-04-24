## spotify new account email happy path 1
* greet
    - utter_greet
    - utter_ask_account
* inform{"account": "Email"}
    - slot{"account": "Email"}
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "Emailid"}
* form: inform{"Emailid": "taluto14@gmail.com"}
    - form: account_form
    - slot{"Emailid": "taluto14@gmail.com"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "april 14 2000"}
    - form: account_form
    - slot{"Date": "april 14 2000"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "male"}
    - form: account_form
    - slot{"Gender": "male"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "talin"}
    - form: account_form
    - slot{"Name": "talin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
* affirm
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* form: inform{"language": "hindi"}
    - slot{"language": ["english", "hindi"]}
    - form: preference_form
    - slot{"language": ["english", "hindi"]}
    - slot{"requested_slot": "artist"}
* form: inform{"Name": "Salman khan"}
    - form: preference_form
    - slot{"artist": ["Drake", "Salman khan"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye
* goodbye

## spotify new account phone happy path 1
* greet
    - utter_greet
    - utter_ask_account
* inform{"account": "Phone"}
    - slot{"account": "Phone"}
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "cellphone"}
* form: inform{"cellphone": "+91 9845012729"}
    - form: account_form
    - slot{"cellphone": "+91 9845012729"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "1st jan 20000"}
    - form: account_form
    - slot{"Date": "1st jan 20000"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "male"}
    - form: account_form
    - slot{"Gender": "male"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "taluto14"}
    - form: account_form
    - slot{"Name": "taluto14"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
* affirm
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* form: inform{"language": "spanish"}
    - slot{"language": ["english", "spanish"]}
    - form: preference_form
    - slot{"language": ["english", "spanish"]}
    - slot{"requested_slot": "artist"}
* form: inform{"Name": "maluma"}
    - form: preference_form
    - slot{"artist": ["Post malone", "maluma"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* thanks
    - utter_goodbye

## spotify new account phone happy path 2
* greet
    - utter_greet
    - utter_ask_account
* inform{"account": "Phone"}
    - slot{"account": "Phone"}
    - slot{"account": "Phone"}
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "cellphone"}
* form: inform{"cellphone": "+91 9845012729"}
    - form: account_form
    - slot{"cellphone": "+91 9845012729"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "1st jan 20000"}
    - form: account_form
    - slot{"Date": "1st jan 20000"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "male"}
    - form: account_form
    - slot{"Gender": "male"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "taluto14"}
    - form: account_form
    - slot{"Name": "taluto14"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
* affirm
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* form: inform{"language": "spanish"}
    - slot{"language": ["hindi", "english", "spanish"]}
    - form: preference_form
    - slot{"language": ["hindi", "english", "spanish"]}
    - slot{"requested_slot": "artist"}
* form: inform{"Name": "diljit singh"}
    - form: preference_form
    - slot{"artist": ["honey singh", "diljit singh"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## spotify new account email happy path 2
* inform
    - utter_greet
    - utter_ask_account
* inform{"account": "Email"}
    - slot{"account": "Email"}
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "Emailid"}
* form: inform{"Emailid": "bajaj.t@husky.neu.edu"}
    - form: account_form
    - slot{"Emailid": "bajaj.t@husky.neu.edu"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "14-04-2000"}
    - form: account_form
    - slot{"Date": "14-04-2000"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "female"}
    - form: account_form
    - slot{"Gender": "female"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "talin rajani"}
    - form: account_form
    - slot{"Name": "talin rajani"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* form: inform{"language": "telegu"}
    - slot{"language": ["hindi", "spanish", "telegu"]}
    - form: preference_form
    - slot{"language": ["hindi", "spanish", "telegu"]}
    - slot{"requested_slot": "artist"}
* form: inform{"Name": "atif aslam"}
    - form: preference_form
    - slot{"artist": ["rajnikanth", "atif aslam"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* thanks
    - utter_goodbye

## multi intent beginning
* greet + inform{"account": "Email"}
    - slot{"account": "Email"}
    - utter_greet
    - utter_help
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "Emailid"}
* form: inform{"Emailid": "talinbajaj@gmail.com"}
    - form: account_form
    - slot{"Emailid": "talinbajaj@gmail.com"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "14th april 2000"}
    - form: account_form
    - slot{"Date": "14th april 2000"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "male"}
    - form: account_form
    - slot{"Gender": "male"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "talin"}
    - form: account_form
    - slot{"Name": "talin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
* affirm
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* form: inform{"language": "english"}
    - slot{"language": ["english"]}
    - form: preference_form
    - slot{"language": "english"}
    - slot{"requested_slot": "artist"}
* form: inform{"Name": "tanesha"}
    - form: preference_form
    - slot{"artist": "tanesha"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## multi intent beginning + stop + continue
* greet + inform{"account": "Email"}
    - slot{"account": "Email"}
    - slot{"account": "Email"}
    - utter_greet
    - utter_help
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "Emailid"}
* form: inform{"Emailid": "talinbajaj@gmail.com"}
    - form: account_form
    - slot{"Emailid": "talinbajaj@gmail.com"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "14th april 2000"}
    - form: account_form
    - slot{"Date": "14th april 2000"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "male"}
    - form: account_form
    - slot{"Gender": "male"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "talin"}
    - form: account_form
    - slot{"Name": "talin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
* affirm
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* stop
    - utter_sorry
    - preference_form
    - slot{"requested_slot": "language"}
* form: inform{"language": "English"}
    - slot{"language": ["Kannada", "English"]}
    - form: preference_form
    - slot{"language": ["Kannada", "English"]}
    - slot{"requested_slot": "artist"}
* form: inform{"Name": "varun dhawan"}
    - form: preference_form
    - slot{"artist": ["chunkey pandey", "varun dhawan"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## multi intent + stop + really stop
* greet + inform{"account": "Email"}
    - slot{"account": "Email"}
    - utter_greet
    - utter_help
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "Emailid"}
* form: inform{"Emailid": "hello@jupiter.money"}
    - form: account_form
    - slot{"Emailid": "hello@jupiter.money"}
    - slot{"requested_slot": "Date"}
* form: inform{"Date": "18 october 1993"}
    - form: account_form
    - slot{"Date": "18 october 1993"}
    - slot{"requested_slot": "Gender"}
* form: inform{"Gender": "male"}
    - form: account_form
    - slot{"Gender": "male"}
    - slot{"requested_slot": "Name"}
* form: inform{"Name": "hannah"}
    - form: account_form
    - slot{"Name": "hannah"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_next
* affirm
    - preference_form
    - form{"name": "preference_form"}
    - slot{"requested_slot": "language"}
* inform{"language": "english"}
    - slot{"language": ["english"]}
    - preference_form
    - slot{"language": "english"}
    - slot{"requested_slot": "artist"}
* stop
    - utter_sorry
* stop
    - action_deactivate_form
    - utter_goodbye

## stop + continue + really stop
* greet
    - utter_greet
    - utter_ask_account
* inform{"account": "Email"}
    - slot{"account": "Email"}
    - account_form
    - form{"name": "account_form"}
    - slot{"requested_slot": "Emailid"}
* stop
    - utter_sorry
* inform{"account": "Email"}
    - slot{"account": "Email"}
    - account_form
    - slot{"requested_slot": "Emailid"}
* form: inform{"Emailid": "jasongirard@gmail.com"}
    - form: account_form
    - slot{"Emailid": "jasongirard@gmail.com"}
    - slot{"requested_slot": "Date"}
* stop
    - utter_sorry
* stop
    - action_deactivate_form
    - utter_goodbye
