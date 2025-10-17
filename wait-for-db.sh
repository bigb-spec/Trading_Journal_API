#!/bin/sh
set -e

echo "⏳ Waiting for MySQL at $MYSQL_HOST:$MYSQL_PORT..."

until nc -z "$MYSQL_HOST" "$MYSQL_PORT"; do
  sleep 2
  echo "Database not ready yet..."
done
echo "✅ MySQL is up and running!"
