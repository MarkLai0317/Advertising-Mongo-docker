// init.js

// Connect to the default database
// rs.initiate({
//     _id: 'rs0',
//     members: [{ _id: 0, host: 'mongo1:27017' }]
// });

let db = db.getSiblingDB('advertising');

// Create a collection named 'mycollection'
db.createCollection('advertisement');

// Create  index
// follow ESR rule
db.advertisement.createIndex({
    "conditions.genders": 1,
    "endAt": 1,
    "startAt": 1,
    "conditions.ageStart": 1,
    "conditions.ageEnd": 1,
})

db.advertisement.createIndex({ "endAt": 1 }, { expireAfterSeconds: 0 });




