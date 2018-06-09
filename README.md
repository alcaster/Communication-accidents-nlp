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

0. Download dump to ./dumps/
1. Set up local db password in file [enviroments/dev/postgres_variables.env]
```bash
POSTGRES_PASSWORD=<HERE>
```
2. Launch postgres
```bash
docker compose run postgres
```
3. Connect to postgres and create database.
```bash
psql -h 127.0.0.1 -p 5432 -U postgres
```
```psql
CREATE DATABASE nlp TEMPLATE template_postgis;
\q
```
4. Import dump of one day
```bash
pg_restore -h localhost -p 5432 -U postgres -d nlp -v dumps/one_day.backup
```

#### Server

0. Add google api key to [enviroments/dev/enviroment_variables.env]
