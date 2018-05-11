# README

## Party API Calls

### What it does

Keeps track of all parties: past, present and future.
Allows access to list of all parties as well as details about a specific party, creation of new parties, updating details for a certain party and deletion of parties.

### Usage

#### Get list of all parties
GET: https://thirsty-thursday.herokuapp.com/party/

#### Get details about one party
GET: https://thirsty-thursday.herokuapp.com/party/[UniquePartyID]/

#### Create new party
POST: https://thirsty-thursday.herokuapp.com/party/

Sample Payload:

    {

        "partyid": "2",
    
        "hostedBy": null,
    
        "eventName": "Post test",
    
        "time": "2011-01-01T13:01:00Z",
    
        "location": "LA Downtown",
    
        "attended": [],
    
        "paidVenmo": [],
    
        "paidCash": []

    }

#### Update a single detail for a certain party
PATCH: https://thirsty-thursday.herokuapp.com/party/[UniquePartyID]/

Sample Payload: Updates status to Live

    {
    
        "status": "Live"

    }

#### Update more than one detail for a party
PUT: https://thirsty-thursday.herokuapp.com/party/[UniquePartyID]/

Sample payload: Updates partyid to 10 and eventName to Post/Put test
(Note: Mandatory field i.e. blank=False, must be specified in the put request even if they are not being modified)

    {
        "partyid": "10",
         
        "hostedBy": null,
    
        "eventName": "Post/Put test",
        
        "time": "2011-01-01T13:01:00Z",
        
        "location": "LA Downtown"
    }
    
#### Delete a certain party
DELETE: https://thirsty-thursday.herokuapp.com/party/[UniquePartyID]/

## User API Calls
Coming soon...

## Party ID Naming Convention

The UniquePartyID field, found in the Party.models.Party in the partyid field is created for a party using the following naming convention:
COLLEGENAME:ORGANIZERID-PARTYNUMBER
where PARTYNUMBER is with respect to the organizer

## Miscellaneous
heroku pg:reset DATABASE_URL --> Destroys existing database: only to be used in emergencies
heroku run python manage.py flush --> resets data in database
heroku run bash
python manage.py makemigrations
python manage.py migrate --run-syncdb --> implements changes made to models in database