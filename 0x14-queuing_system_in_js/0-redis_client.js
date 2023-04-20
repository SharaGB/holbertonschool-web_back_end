const redis = require("redis");
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client connected to the server: ${error}`);
});

client.on("ready", () => {
  console.log("Redis client connected to the server");
});
