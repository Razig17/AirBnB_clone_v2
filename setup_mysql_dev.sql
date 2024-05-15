--   Creates a MySQL server with:
--   Database hbnb_dev_db and User hbnb_dev localhost with password hbnb_dev_pwd
--   Grants all privileges for hbnb_dev on hbnb_dev_db.
--   Grants SELECT privilege for hbnb_dev on performance

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES