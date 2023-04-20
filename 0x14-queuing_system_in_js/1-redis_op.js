const redis = require("redis");
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client connected to the server: ${error}`);
});

client.on("ready", () => {
  console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
      redis.print(`Reply: ${reply}`);
  });
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
      console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
