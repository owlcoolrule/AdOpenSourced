# AdOpenSourced

Advertise. With an easy format.
Tired of your members advertising in an inproper format? With this AdBot, you can have members answer some simple questions in their DMs, and then a embed sent as them via a webhook will be sent.

# Setup

If something does go wrong during this setup, please join the Aerolinia support server, which you can find at https://aerolinia.xyz. Though Aerolinia staff may not be able to answer your question, they'll try their best. **Please** read these before creating a ticket.

# Step one - Clone this code

Forking a GitHub rep is easy, just click on the fork button.

# Step two - Edit this code (no coding skills required)

Did not mean to scare you with that 😂, you'll just have to write in English. It's not hard at all, so I'll break it down into three easy to follow steps.

# Step two / Part one - Get a bot token

Go to https://discord.com/developers and click on "New application". Add your name and logo. Then go over to the "Bot" section. Create a bot, save your changes,
and click "copy token". **Now replace the token here in client.run with your token. DO NOT remove the ("").** The final version should look like this:
client.run("asdfhjil;kbhzvlfuioajsv") <- Not a real token so don't even try lol

# Step two / Part two - Get a webhook URL

In your server settings, integrations -> webhooks -> new webhook.
The name and image of the webhook will never be seen, you can totaly ignore it.
**Set the channel to your advertising channel**.

Now, proceed to line 55 of the main code. Replace the Webhook URL here thing with your webhook URL. **Make sure to keep the ''.** It should in the end look like:
``webhook = Webhook.from_url('fakewebhook.com/lol', adapter=AsyncWebhookAdapter(session))`` <- Except make it your real webhook URL.

# Step two / Part three - Hosting

Hosting is easy with [Heroku](https://heroku.com). It shouldn't take too long at all. Go ahead and create a new Heroku account. Go to "new" and choose "create new app". Choose an app name, and then you're (almost) done!

Now, just go to "Deploy" tab, and choose the GitHub option. Sign in with GitHub, and choose the **rep you just forked.** Then click **Deploy**.

# Step four - Inviting

So you've created your bot, but you want to invite it to your server. It's not hard at all! Head on over to https://discord.com/developers, and select the application you made. The choose "OAuth2". You'll see a long list of things, you can ignore them. Find "Bot" on that long list. That should open another checkbox panel, though the bot doesn't really need any perms, you might as well just give it "Administrator" as I might be wrong 🤣. Then go back up to the first checkbox panel. Click on "Copy", open that link in a new tab. Congrats! You just created an ad bot. It's prefix is currently ``!``. Change the ``!`` on line 14 with your prefix, not removing anything else. If I wanted my prefix to be ``?`` instead, it would look like this: ``client = commands.Bot(command_prefix = "?",case_insensitive=True,intents=intents)``.

# FAQs:

**Q -** How would I change the cooldown?
**A -** Head on over to line 22, and note this line:
``@commands.cooldown(1, 14400, commands.BucketType.user)``
**DON'T change anything except the ``14400`` part.** The 14400 is how many *seconds* the cooldown is. 14400 seconds is equivalent to four hours. Change that to however many seconds you want your cooldown to be. You might want to scroll down to line 69 and change the words so it matches your new cooldown.

**Q -** How do I change the channel it sends a message to?
**A -** It's not in the code lol. Head on down to the webhooks section of your server settings and change the channel to your new desired channel. No need to edit the URL, the current one has already updated with the new channel data.
