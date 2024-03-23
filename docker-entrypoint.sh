#!/bin/bash
set -e

# Start MongoDB in the background
mongod --auth --keyFile /etc/mongo/mongodb-keyfile --replSet "${MONGO_INITDB_REPLICA_SET_NAME}" --bind_ip_all &

# # Wait for MongoDB to start
sleep 10

# # # Initialize the replica set if it hasn't been done
# mongo --eval "rs.initiate({_id: '${MONGO_INITDB_REPLICA_SET_NAME}', members: [{ _id: 0, host: 'localhost:27017' }]})"

# Keep the container running
fg %1
