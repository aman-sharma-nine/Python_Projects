#Australian Road Deaths Database
The Australian Road Deaths Database (ARDD) is maintained and published by BITRE. It commenced in 1989
and is updated on a monthly basis.  
The ARDD contains basic demographic and crash details of people who have died in an Australian road crash.
Every fatal road traffic crash in Australia is in scope, and information is included for all people who were killed.
It is published in two forms
 Fatalities: each record is a killed person
 Crashes: each record is a fatal crash
The link between these is made by the CrashID field. A full list of fields follows:
Note: Missing values for numeric fields are coded with ‘-9’;
Field Description Format Values
Crash ID National crash-identifying number Integer 13 - digit, unique to each fatal crash
State Australian jurisdiction Text Abbreviation for each state/territory
Date Date of crash Date dd-mmm-yyyy
Month Month of crash Text
Year Year of crash Integer
Dayweek Day of week of crash Text
Time Time of crash Time hh:mm
Crash Type Code summarising type of crash:
three values relating to the number
of vehicles involved, and whether a
pedestrian was killed
Text Single
Multiple
Pedestrian
Number of
Fatalities
Number of killed persons
(fatalities) in the crash
Integer
Bus
Involvement
Indicates involvement of a bus in
the crash
Text Yes
No

Heavy rigid
truck
Involvement
Indicates involvement of a heavy
rigid truck in the crash
Text Yes
No
Artic truck
Involvement
Indicates involvement of an
articulated truck in the crash
Text Yes
No
Speed Limit Posted speed limit at location of
crash

Integer (^)
Road User Road user type of killed person Text Driver
Passenger
Pedestrian
Motorcycle rider
Motorcycle pillion passenger
Bicyclist (includes pillion passengers)
Gender Sex of killed person Text Male
Female
Age Age of killed person (years) Integer (^)

This is a offline tool, your data stays locally and is not send to any
