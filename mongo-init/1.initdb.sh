#!/bin/bash
set -e;

if [ -n "${DB_USERNAME:-}" ] && [ -n "${DB_PASSWORD:-}" ]; then
    "${mongo[@]}" "$MONGO_INITDB_DATABASE" <<-EOJS
        db.createUser({
            user: $(_js_escape "$DB_USERNAME"),
            pwd: $(_js_escape "$DB_PASSWORD"),
            roles: [
                {
                    role: "readWrite",
                    db: $(_js_escape "$MONGO_INITDB_DATABASE")
                }
            ]
        })
EOJS
else
    echo "Create User fail"
fi