# Documentation
This explains how the following GET/POST/PATCH/DELETE requests can be used to interact with the Thursty Backend RESTful API.

## Party

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

#### Delete a certain party
DELETE: https://thirsty-thursday.herokuapp.com/party/[UniquePartyID]/

## User
Coming soon...
