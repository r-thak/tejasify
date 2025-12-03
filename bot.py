import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to track combined messages
# Format: {channel_id: {'user_id': user_id, 'messages': [msg1, msg2, ...], 'bot_message': bot_msg_obj, 'combined_content': str}}
channel_tracking = {}


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guild(s)')


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands first
    await bot.process_commands(message)

    channel_id = message.channel.id
    user_id = message.author.id

    # Initialize channel tracking if not exists
    if channel_id not in channel_tracking:
        channel_tracking[channel_id] = {
            'user_id': user_id,
            'messages': [message],
            'bot_message': None,
            'combined_content': None
        }
        return

    tracking = channel_tracking[channel_id]

    # If this is a message from the same user
    if tracking['user_id'] == user_id:
        tracking['messages'].append(message)

        # If we have at least 2 messages, process them
        if len(tracking['messages']) >= 2:
            # Delete the new message
            try:
                await message.delete()
            except discord.errors.Forbidden:
                print(f"Missing permissions to delete messages in {message.channel.name}")
                return
            except Exception as e:
                print(f"Error deleting message: {e}")
                return

            # If this is the second message (first time combining)
            if len(tracking['messages']) == 2:
                # Delete the first message too
                try:
                    await tracking['messages'][0].delete()
                except:
                    pass

                # Create combined message
                combined_content = f"{message.author.display_name}:\n{tracking['messages'][0].content}..{tracking['messages'][1].content}"
                bot_msg = await message.channel.send(combined_content)
                tracking['bot_message'] = bot_msg
                tracking['combined_content'] = combined_content
            else:
                # Edit existing bot message to append new content
                if tracking['bot_message'] and tracking['combined_content']:
                    try:
                        new_content = f"{tracking['combined_content']}..{message.content}"
                        await tracking['bot_message'].edit(content=new_content)
                        tracking['combined_content'] = new_content
                    except Exception as e:
                        print(f"Error editing message: {e}")
    else:
        # Different user sent a message, reset tracking for this channel
        channel_tracking[channel_id] = {
            'user_id': user_id,
            'messages': [message],
            'bot_message': None,
            'combined_content': None
        }


@bot.command(name='ping')
async def ping(ctx):
    """Check if the bot is responsive"""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')


@bot.command(name='help_tejasify')
async def help_tejasify(ctx):
    """Show help information"""
    help_text = """
    **Tejasify Bot**

    This bot automatically combines consecutive messages from the same user.

    When a user sends 2+ messages in a row:
    - The messages are deleted
    - A combined message is posted with format:
      User:
      message1..message2..message3

    Commands:
    - !ping - Check bot latency
    - !help_tejasify - Show this help message
    """
    await ctx.send(help_text)


def main():
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        raise ValueError("DISCORD_BOT_TOKEN not found in environment variables!")

    bot.run(token)


if __name__ == '__main__':
    main()
