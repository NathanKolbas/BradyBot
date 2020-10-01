const Discord = require("discord.js");
const config = require("./config.json");

const client = new Discord.Client();
const prefix = "brady-bot ";

client.on("message", function(message) {
  if (message.author.bot) return; // Checks if the message was from a bot
  if (!message.content.startsWith(prefix)) return;

  const commandBody = message.content.slice(prefix.length);
  const args = commandBody.split(' ');
  const command = args.shift().toLowerCase();

  if (command === "ping") {
    const timeTaken = Date.now() - message.createdTimestamp;
    message.reply(`Pong! This message had a latency of ${timeTaken}ms.`);
  } else if (command === "sum") {
    const numArgs = args.map(x => parseFloat(x));
    const sum = numArgs.reduce((counter, x) => counter += x);
    message.reply(`The sum of all the arguments you provided is ${sum}!`);
  } else if (command === 'execute') {
    const name = commandBody.substr(commandBody.indexOf(' ') + 1);
    // message.channel.send(`Name: ${name}`);
    message.channel.send(`Name: ${name}`, {
      files: [{
        attachment: 'AmongUsKill.gif'
      }]
    }).then(console.log).catch(console.error);
  } else if (command  === 'test') {
    let member = message.mentions.users.first();
    const avatarUrl = member.avatarURL();
    message.channel.send(`Name: ${member}`, {
      files: [{
        attachment: avatarUrl
      }]
    }).then(console.log).catch(console.error);
  }
});

client.login(config.BOT_TOKEN);
