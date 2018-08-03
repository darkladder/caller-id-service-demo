# Caller ID Service Demo

## Prerequisites

This package utilizes Docker to contain everything together, to bundle up all internal dependencies, and to make it easier to distribute the software as originally designed, with included data sets and database.

- Docker
- Docker Compose

## Launching the Service

Please note that after launching the first time, the DB data will seed before proceeding.

```
$ docker-compose up
```

Note, if upgrading from a previous version, run the following to rebuild the Docker containers:

```
$ docker-compose build && docker-compose up
```

### Important

The public web port, etc., can be found in the .env file.

## API

Note: The phone number can be posted in a variety of formats as the internal library does its best to normalize the phone number.

### Add new number to the service

{POST} http://localhost:5000/number
JSON BODY: { “name”: “Bob Barker”, “number”: “+15556789090”, “context”: “personal”}

200 Success Response Example:
```
{"status": "success"}
```

404 Error Response Example:
```
{"error": "Could not add record. Possible duplicate value."}
```

### Retrieve Caller ID detail from the service


{GET} http://localhost:5000/number/13058224036

200 Success Response Example:

```
{"number": "+13058224036", "context": "home", "name": "Nowlin Saul"}
```

404 Error Response Example:
```
{"error": "Could not locate record."}
```

## A note about the seeded data

I seeded about 300,000 records into the DB, and then stopped the process.  The numbers are have been normalized in the E.164 format.

Here's a sample set:



| Number               |  Context      |  Name                      |
|-----------------------|----------------|---------------------------|
| +13058224036   | zendesk      | Nowlin Saul             |
| +16094914267   |  home         | Rubino Lennoxlove  |
| +17157767000   | zendesk     |  Deluna Mcginley      |
| +15203611642   |  blah           |  Spearman Mccreary|
| +16575044762   |  desk.com  |  Briley Hunterstone  |
|   +12164337234  |  facebook  | Luffness Mattison     |
	
