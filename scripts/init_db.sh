#!/bin/bash
set -e

echo "Creating databases..." 
# Create databases
PGPASSWORD=postgres psql -U postgres -c "CREATE DATABASE \"$DB_NAME\";" || true

echo "Creating users..."
# Create users
PGPASSWORD=postgres psql -U postgres -c "CREATE USER $DB_USER WITH SUPERUSER LOGIN PASSWORD '$DB_PASSWORD';" || true

echo "Granting privileges..."
# Grant privileges
PGPASSWORD=postgres psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE \"$DB_NAME\" TO \"$DB_USER\";" || true
