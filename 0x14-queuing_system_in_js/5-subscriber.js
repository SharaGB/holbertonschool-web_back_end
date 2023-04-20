const redis = require("redis");
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client connected to the server: ${error}`);
});

client.on("ready", () => {
  console.log("Redis client connected to the server");
});

client.on("message", (channel, message) => {
  if (channel.localeCompare("holberton school channel") === 0) {
    console.log(message);

    if (message.localeCompare("KILL_SERVER") === 0) {
      client.unsubscribe(channel);
      client.quit();
    }
  }
});

client.subscribe("holberton school channel");
