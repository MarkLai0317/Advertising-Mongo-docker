FROM mongo:latest

# Set environment variables
ENV MONGO_INITDB_DATABASE=advertising
# ENV MONGO_INITDB_ROOT_USERNAME=mark
# ENV MONGO_INITDB_ROOT_PASSWORD=markpwd
ENV MONGO_INITDB_REPLICA_SET_NAME=rs0

# Copy the key file and initialization script
COPY ./mongodb-keyfile /etc/mongo/mongodb-keyfile
COPY ./init.js /docker-entrypoint-initdb.d/

# Correct permissions for the key file
RUN chmod 400 /etc/mongo/mongodb-keyfile && chown mongodb:mongodb /etc/mongo/mongodb-keyfile

# Expose default MongoDB port
EXPOSE 27017


# # Set the entrypoint
# ENTRYPOINT ["docker-entrypoint.sh"]
# CMD ["mongod"]

