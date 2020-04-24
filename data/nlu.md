## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:inform
- [phone](account:Phone)
- [email](account:Email)
- My [email](account:Email) id is [jupiter@gmail.com](Emailid)
- [email](account:Email) is [saturn@gmail.com](Emailid)
- its [talinbajaj@hotmail.com](Emailid)
- [bangalore@outlook.com](Emailid)
- [justin2000@jupiter.money](Emailid)
- [modi@northeastern.edu](Emailid)
- [tom_@india.io](Emailid)
- yes sure it is [salman12@yahoo.com](Emailid)
- [greetings@bangalore.com](Emailid)
- [hello@india.com](Emailid)
- [14th April 2000](Date)
- [4 March 2018](Date)
- I am born on [1 May 1982](Date)
- My date of birth is [08 Oct 2010](Date)
- [April 27 1980](Date)
- [Sep 1 1976](Date)
- [9-4-1993](Date)
- [14-12-2004](Date)
- my dob is [03-03-2003](Date)
- [12-12-86](Date)
- [2/12/2033](Date)
- [20/12/2009](Date)
- [3/2/99](Date)
- [october 9th 1933](Date)
- [nov 9th 1933](Date)
- [male](Gender)
- [female](Gender)
- i am a [male](Gender)
- i am a [female](Gender)
- my [phone](account:Phone) number is [+91 9845012729](cellphone)
- my [phone](account:Phone) number is [8419845012779](cellphone)
- [+18574729171](cellphone)
- [+917263487619](cellphone)
- [8012798766](cellphone)
- [+91 8310275672](cellphone)
- [+123 86598 78965](cellphone)
- [981 8748300345](cellphone)
- [+91 984-501-2729](cellphone)
- [+1 333-344-8732](cellphone)
- my name is [Talin](Name)
- [Jagdish Bajaj](Name)
- [Zaid Khuram](Name)
- [Rajram Mohanlal Bajaj](Name)
- [Siddivinayak](Name)
- [Van der Humpton](Name)
- [Michael D'Angelo](Name)
- [Mitali Ajay Rajani](Name)
- [Ajay](Name)
- [Vishal Vishal](Name)
- [Jiten Gupta](Name)
- [Dipali](Name)
- [Isemail](Name)
- [raj menda](Name)
- [vikram subbiah](Name)
- [mohit](Name)
- I would like to listen to [English](language) and [Hindi](language)
- I would listen to [English](language), [Hindi](language), [Kannada](language)
- I listen to [Spanish](language) [English](language) [Russian](language)
- umm just [Bengali](language)
- only [arabic](language)
- I like [Korean](language)
- [Drake](Name) and [Arijit Singh](Name)
- I would like to listen to [YNW Melly](Name)
- I want to listen to [archana](Name)
- [Post Malone](Name) and [Roddy Rich](Name)
- I would like to listen to [Ashwin Makhija](Name) and [Salman Khan](Name)
- [John](Name), [Badshah](Name), [Weeknd](Name)
- [phone](account:Phone) number please
- [+91 9845012729](cellphone)
- [1st jan 20000](Date)
- my name is [taluto14](Name)
- only [english](language) and [spanish](language) please
- [Post malone](Name) and [maluma](Name)
- [hindi](language) [english](language) [spanish](language)
- [honey singh](Name) and [diljit singh](Name)
- hello i would like to open a new account
- [bajaj.t@husky.neu.edu](Emailid)
- the name i want to use is [talin rajani](Name)
- i listen to [hindi](language), [spanish](language), [telegu](language)
- [rajnikanth](Name) and [atif aslam](Name)
- [talinbajaj@gmail.com](Emailid)
- [14th april 2000](Date)
- [Kannada](language), [English](language)
- [chunkey pandey](Name) and [varun dhawan](Name)
- [hello@jupiter.money](Emailid)
- [18 ovtober 1993](Date:18 october 1993)
- [make](Gender:male)
- [hannah](Name)
- [email](account:Email)
- okay my [email](account:Email)

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- okay
- okay sure

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:stop
- ok then you cant help me
- i do not want to choose this now
- you can't help me
- that's not what i want
- this is leading to nothing
- this conversation is not helpful
- you cannot help me with what I want
- hm i don't think you can do what i want
- stop

## intent:thanks
- thank you
- thanks
- thanks for the help

## intent:greet + inform
- hello i want to open a new account with my [email](account:Email)
- hello i want to use my [email](account:Email) to create an account

## synonym:18 october 1993
- 18 ovtober 1993

## synonym:Email
- email

## synonym:Phone
- phone

## synonym:male
- make

## regex:Date
- (JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|NOV|OCT|DEC)\s[\d]{1,2}[\d]{4}
- (January|February|March|April|May|June|July|August|September|October|November|December)\s[\d]{1,2}[\d]{4}
- [\d]{1,2} [ADFJMNOS]\w* [\d]{4}
- [\d]{1,2} [ADFJMNOS]\w* [\d]{4}
- [\d]{1,2}-[\d]{1,2}-[\d]{2}
- [\d]{1,2}/[\d]{1,2}/[\d]{4}
- [\d]{1,2}\s(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|NOV|OCT|DEC)\s[\d]{4}
- [\d]{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December)\s[\d]{4}

## regex:Emailid
- [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-+-]+\.[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+$
- [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

## regex:Name
- /^[a-z ,.'-]+$/i
- ^[A-Z]'?[-a-zA-Z]+$
- ^[A-Z][-a-zA-Z]+$
- ^[A-Z][a-zA-Z]+$

## regex:cellphone
- \d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}
- ^\+(?:[0-9] ?){6,14}[0-9]$
- ^\d{3}-\d{3}-\d{4}$

## lookup:language
- English
- Hindi
- Spanish
- Mandarin
- Japanese
- Punjabi
- Tamil
- Telugu
- Malayalam
- Marathi
- Gujarati
- Bengali
- Kannada
- Arabic
- Russian
- Nepali
- French
- Portuguese
- Greek
- Urdu
- Korean
- German
