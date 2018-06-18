# Communication-accidents-nlp
An application of tracking ztm history of communication accidents for course of nlp.
## Running
```bash
docker compose up
```
### Prerequisites
- docker
- docker-compose
- postgres-client(for simplicity, can be done only by docker)

## Initial setup

#### Database
To create local database for development you need to import data.
Only executed first time, data is persisted in database/data

0. Download dump to ./db/imports/

#### Server

0. Add google api key to [enviroments/dev/enviroment_variables.env]
