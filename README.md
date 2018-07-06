# README

## Party API Calls

### What it does

Keeps track of all parties: past, present and future.
Allows access to list of all parties as well as details about a specific party, creation of new parties, updating details for a certain party and deletion of parties.

### Usage

#### Get list of all parties
GET: https://thirsty-thursday.herokuapp.com/party/all/

#### Get details about one party
GET: https://thirsty-thursday.herokuapp.com/party/search/[UniquePartyID]/

#### Create new party
POST: https://thirsty-thursday.herokuapp.com/party/all/

Sample Payload:

    {
        
        "partyid": "UCLA:105032378-1", //Refer to party naming convention
 
        "eventName": "Post Test",
 
        "hostedBy": "UCLA:105032378",

        "hostedByNameCache": "Siddharth",
        
        "status": "Current",
        
        "time": "2018-05-12T21:42:22.890158Z",
        
        "location": "Canyon Point",
        
        "guests": [
            "UCLA:105032378"
        ],
        
        "guestsNameCache": [
            "Siddharth"
        ],
        
        "entryTime": [
            "2018-05-12T21:42:22.890158Z"
        ],
        
        "exitTime": [
            "2018-05-12T21:52:22.890158Z"
        ],
        
        "paymentMethod": [
            "Cash"
        ]
    
    }

#### Update a single detail for a certain party
PATCH: https://thirsty-thursday.herokuapp.com/party/search/[UniquePartyID]/

Sample Payload: Updates status to Live

    {
    
        "status": "Live"

    }

#### Update more than one detail for a party
PUT: https://thirsty-thursday.herokuapp.com/party/search/[UniquePartyID]/

Sample payload: Updates Party ID to UCLA:105032378-2 and changes the time
(Note: Mandatory field i.e. blank=False, must be specified in the put request even if they are not being modified)

    {
        
        "partyid": "UCLA:105032378-2",
 
        "eventName": "Post Test",
 
        "hostedBy": "UCLA:105032378",

        "hostedByNameCache": "Siddharth",
        
        "status": "Current",
        
        "time": "2018-05-12T22:42:22.890158Z",
        
        "location": "Canyon Point",
        
        }
    
#### Delete a certain party
DELETE: https://thirsty-thursday.herokuapp.com/party/search/[UniquePartyID]/

#### Get all parties for a particular college
GET: https://thirsty-thursday.herokuapp.com/party/filter/college/[CollegeName]/

#### Get all parties for a particular organizer
GET: https://thirsty-thursday.herokuapp.com/party/filter/organized-By/[OrganizerUniqueID]/

##Guest API Calls

### What it does

Provides functionality to check in guest or check out a guest.
Also allows the user to view the guest instances for a single party (as well as filter them by college, organizer or view all of them).  

###Usage

#### Get all guest instances
GET: https://test-thursday.herokuapp.com/guest/all/

#### Check in new guest
POST: https://test-thursday.herokuapp.com/guest/checkin/ HTTP/1.1

{

    "guestInstanceID": "UCLA:105032378-1UCLA:000000001",

    "partyID": "UCLA:105032378-1",

    "userID": "UCLA:000000001",

    "firstName": "Joesephine",

    "lastName": "Bruin",

    "college": "UCLA",

    "entryTime": "2018-07-06T23:00:00Z",

    "exitTime": "1970-01-01T00:00:00Z",

    "paymentMethod": "Venmo"

}

#### Check out guest

PATCH:  https://test-thursday.herokuapp.com/guest/search/UCLA:105032378-1UCLA:000000001/ HTTP/1.1

{

    "exitTime": "2018-07-07T00:00:00Z"

}

#### Filter by Party
GET: https://test-thursday.herokuapp.com/guest/party/UCLA:105032378-1/ HTTP/1.1

## User API Calls
Coming soon...

## Naming Conventions

### Party ID 

The unique Party ID found in the Party.models.Party model in the partyid field is created for a party using the following naming convention:
COLLEGENAME:ORGANIZERID-PARTYNUMBER
where PARTYNUMBER is with respect to the organizer

### User ID
The unique User ID found in the User.models.User field in the uniqueID field is created for a user using the following naming convention:
COLLEGENAME:USERID - where USERID is the user's college identification number. 

## Miscellaneous
heroku pg:reset DATABASE_URL --> Destroys existing database: only to be used in emergencies
heroku run python manage.py flush --> resets data in database
heroku run bash
python manage.py makemigrations
python manage.py migrate --run-syncdb --> implements changes made to models in database
