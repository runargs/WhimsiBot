# 🤖 WhimsiBot, the Discord Bot

A silly Discord bot that provides fun commands, especially made to help pass time while in quarantine due to COVID-19. *Necessity is the mother of all invention*, as they say.

This is my first time

* making a Discord Bot, using API calls,
* working with secret tokens and securing them using config variables,
* using an API Wrapper,
* deploying a project to Heroku,
* connecting Heroku to GitHub,
* and taking steps away from GitHub GUI/IDE GUIs for git into the world of command line!

Hope you enjoy.

<img src="https://cdn.pixabay.com/photo/2019/06/22/14/42/robot-4291692_960_720.png" width="200">

## 🔗 Getting Started

To add this bot to your server follow this link:

```
https://discordapp.com/api/oauth2/authorize?client_id=691400372505542746&scope=bot
```

## 🚀 Deployment

This project is deployed on Heroku using a GitHub connection.

## 🤔 Commands

* `!activity` Suggests a random activity to do if you're bored
* `!ascii <text>` Generates an ASCII art representation of the given text
* `!help` Shows available commands
* `!inspire` Provides an inspiring AI generated image-quote
* `!jeopardy` Displays a Jeopardy trivia question with a click-to-reveal answer
* `!joke` Tells a joke, there is no guaruntee it's good
* `!mock <text>` WhimsiBot will mock the text in the style of the classic [Spongebob Meme](https://knowyourmeme.com/memes/mocking-spongebob)
* `!pic <optional keyword>` Provides an image sourced from Unsplash, either a featured photo or one based on the provided keyword search
* `!quarantineActivities` Suggests a random activity that one person can do alone
* `!reverse <text>` Reverses the given text             
* `!whois <name>` Generates a guess of what someone's age and gender are, with probability, based on their name

## 🚧 Built With

* [discord.py](https://github.com/Rapptz/discord.py) - Pythonic API Wrapper
* [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - port of FIGlet (http://www.figlet.org/)
* [Agify](https://agify.io/) - API that guesses age based on name
* [Genderify](https://api.genderize.io) - API that guesses gender based on name
* [jService](http://jservice.io) - Jeopardy Trivia API
* [Unsplash](https://unsplash.com/) - Free stock images
* [icanhazdadjoke](https://icanhazdadjoke.com) - API that provides dad jokes
* [Inspirobot](https://inspirobot.me) - API that provides AI generated inspirational images/quotes
* [BoredAPI](http://www.boredapi.com) - API that provides activity ideas based on type, participants, etc
* A lot of Googling, StackOverflow, and YouTube consumption
