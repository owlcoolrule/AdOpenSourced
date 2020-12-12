# AdOpenSourced

Advertise. With an easy format.
Tired of your members advertising in an inproper format? With this AdBot, you can have members answer some simple questions in their DMs, and then a embed sent as them via a webhook will be sent.

# Setup

We don't offer support for this setup, so please don't open a ticket requesting for it. The setup isn't too hard to follow though.

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

# Step three / Hosting

Hosting is easy with [Heroku](https://heroku.com). It shouldn't take too long at all. Go ahead and create a new Heroku account. Go to "new" and choose "create new app". Choose an app name, and then you're (almost) done!

Now, just go to "Deploy" tab, and choose the GitHub option. Sign in with GitHub, and choose the **rep you just forked.** Then click **Deploy**.

Head on over to the "resources" tab and click edit. Then check all the boxes. Your bot should be online within a minute or two.
