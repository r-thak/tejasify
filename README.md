# tejasify

tejasify allows you to make any discord server into a discord server with career_maxxing in it by condensing several successive messages into a single message separated by two periods ".."

- Automatically detects when a user sends 2+ consecutive messages
- Deletes the duplicate messages
- Posts a combined message in format: `@user message1..message2..message3`
- Continues to append messages if the user keeps sending without interruption
- Only resets when a different user (not the bot) sends a message

## Setup
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Under the bot's username, click "Reset Token" to get your token
5. Enable the following Privileged Gateway Intents:
   - Message Content Intent
   - Server Members Intent (optional)
6. Go to OAuth2 → URL Generator
7. Select scopes: `bot`
8. Select bot permissions: `View Channels`, `Send Messages`, `Manage Message`, `Read Message History`
9. Copy the generated URL and open it in your browser to invite the bot to your server

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd tejasify
```

2. Create a `.env` file and add your Discord bot token:
```bash
cp .env.example .env
nano .env
DISCORD_BOT_TOKEN=your_actual_token_here
```

3. Build and run with Docker Compose:
```bash
docker-compose up -d
```

View logs:
```bash
docker-compose logs -f
```

Stop the bot:
```bash
docker-compose down
```


### Commands

- `!ping` - Check if the bot is responsive and see latency
- `!help_tejasify` - Show help information

## Example

User sends:
```
User: Hello
User: How are you
User: Today?
```

Bot will delete those messages and post:
```
@User Hello..How are you..Today?
```

[My Instance's Invite Link](https://discord.com/oauth2/authorize?client_id=1445638105687265290&permissions=76800&integration_type=0&scope=bot)
