# vaccine-notifi-bot
Refer to https://github.com/pranavtendolkr/vaccine-notifi-bot#readme for setup steps.


## SEARCH BY LOCATION


This forked project allow you to find slots from all the available centers near your location.

Update the `lat` and `long` variables in `vaccine.py`

You can get the values by a simple google search. Eg: "vasco da gama coordinates"


**IMPROTANT** : Autoboooking is not tested by me.


### EXAMPLE RUN:

Note that the below data is not real and cannot be referenced for any purpose.

```
$ python3.9.exe .\vaccine.py debug
Found 40 centers near your location
['Ravindra Bhavan Vasco(FLW)', 'Mormugao Ravindra Bhavan', 'Vaatsalya Hospital (PMJAY)', 'INHS Covaxine', 'INHS Jeevanti', 'INHS Jeevanti', 'INS Hansa', 'Pai Hospital (PMJAY)', 'St Andrews HSS Vaddem', 'M P T Hospital', 'MPT Hospital', 'Chicalim SDH Mormugao (FLW)', 'RAJHANS', 'MPT FLW', 'VASCO UHC Mpt HCW', 'SDHospital Chicalim', 'Chicalim( Mop Up)', 'SDH Chicalim', 'SMRCs Hospital (DDSY)', 'Chicalim CHC Mormugao (FLW)', 'SDH Chicalim (Vasco UHC)', 'The Indians Hotels Co. LTD', 'Manipal Hospital', 'Chimbel PHC Manipal Hospital', 'PHC CHIMBEL Manipal Site', 'Chimbel PHC - Manipal Hospital', 'Chimbel Manipal', 'Manipal Hospital Goa', 'Manipal Work place', 'Community Hall Taliegao', 'Community Hall Taliegao', 'PHC Chimbel 18plus', 'Goa Medical College', 'Goa Medical College', 'Primary Health Centre Chimbel', 'Primary Health Centre Chimbel', 'Chimble Public Health Centre', 'PHC Chimble', 'Goa Medical College Bambolim', 'Goa Medical College Bambolim']
 INHS Covaxine, South Goa , 28-05-2021, slots available: 0
 The Indians Hotels Co. LTD, North Goa , 28-05-2021, slots available: 0
 Manipal Hospital, North Goa , 28-05-2021, slots available: 10
 Manipal Hospital, North Goa , 29-05-2021, slots available: 9
 Manipal Hospital, North Goa , 31-05-2021, slots available: 94
 Manipal Hospital, North Goa , 01-06-2021, slots available: 145
 Manipal Hospital, North Goa , 02-06-2021, slots available: 118
 Manipal Hospital, North Goa , 03-06-2021, slots available: 145
 Manipal Hospital, North Goa , 31-05-2021, slots available: 94
 Manipal Hospital, North Goa , 01-06-2021, slots available: 145
 Manipal Hospital, North Goa , 02-06-2021, slots available: 118
 Manipal Hospital, North Goa , 03-06-2021, slots available: 145
 Manipal Hospital, North Goa , 04-06-2021, slots available: 15
 Manipal Hospital, North Goa , 05-06-2021, slots available: 0
 Manipal Hospital Goa, North Goa , 28-05-2021, slots available: 0
 Manipal Hospital Goa, North Goa , 29-05-2021, slots available: 0
 Manipal Hospital Goa, North Goa , 28-05-2021, slots available: 0
 Manipal Hospital Goa, North Goa , 29-05-2021, slots available: 0
 Chimble Public Health Centre, North Goa , 28-05-2021, slots available: 0
 ```