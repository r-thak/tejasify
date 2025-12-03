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

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp .env.example .env
```

5. Edit `.env` and add your Discord bot token:
```
DISCORD_BOT_TOKEN=your_actual_token_here
```

### Running the Bot

```bash
python bot.py
```

You should see a message confirming the bot has connected to Discord.

## Usage

Once the bot is running and in your server:

1. The bot automatically monitors all channels it has access to
2. When a user sends 2+ messages in a row, the bot will:
   - Delete those messages
   - Post a combined version with messages separated by `..`
3. If the user continues sending messages, the bot will keep editing its message to append them

### Commands

- `!ping` - Check if the bot is responsive and see latency
- `!help_tejasify` - Show help information

## Required Bot Permissions

- Read Messages/View Channels
- Send Messages
- Manage Messages (to delete user messages)
- Read Message History

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

## Troubleshooting

- **Bot not responding**: Make sure Message Content Intent is enabled in the Discord Developer Portal
- **Can't delete messages**: Ensure the bot has "Manage Messages" permission
- **Bot not seeing messages**: Check that the bot has "Read Messages" and "Read Message History" permissions
