const redis = require("redis");
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client connected to the server: ${error}`);
});

client.on("ready", () => {
  console.log("Redis client connected to the server");
});

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish("holberton school channel", message);
  },time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
