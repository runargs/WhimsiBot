import discord, random, json, requests, math, asyncio
from discord.ext import commands
from pyfiglet import Figlet

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

def mockMe(str):
    length = len(str)
    r = list(range(0, length))
    newStr = ""
    for ito in range(0,5):
        chosenLetters = random.sample(r,int(length/2))
        for char in range(0,length):
            if char in chosenLetters:
                newStr += str[char].swapcase()
            else:
                newStr += str[char]
        newStr += " "
    newStr += "\nhttps://bit.ly/3do0ICc"
    return newStr

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def mock(ctx, *, text: str):
    result = mockMe(text)
    await ctx.send(result)

@bot.command()
async def ascii(ctx, *, text: str):
    f = Figlet(font='slant')
    result = "```" + f.renderText(text) + "```"
    await ctx.send(result)

@bot.command()
async def whois(ctx, name: str):
    await ctx.send("Hmmm ...")
    ageUrl = "https://api.agify.io/?name=" + name
    genderUrl = "https://api.genderize.io?name=" + name
    ageResponse = requests.get(ageUrl, verify=True)
    genderResponse = requests.get(genderUrl, verify=True)
    myGuess = '''
I think {} is {} years old, .
I also would guess, with {} probability, that they're {}.
    '''.format(
    str(name.capitalize()),
    str(ageResponse.json()['age']),
    str(math.floor(genderResponse.json()['probability']*100)) + "%",
    str(genderResponse.json()['gender'])
    )
    await asyncio.sleep(1)
    await ctx.send(myGuess)

@bot.command()
async def jeopardy(ctx):
    await ctx.send("Here's a Jeopardy question...")
    jServUrl = "http://jservice.io/api/random/"
    jServResp = requests.get(jServUrl, verify=True)
    await asyncio.sleep(1)
    triviaStr = '''

{} points, the category is " {} ".

*{}*

Click for the answer!
|| {} ||
    '''.format(
    str(jServResp.json()[0]['value']),
    str(jServResp.json()[0]['category']['title']).capitalize(),
    str(jServResp.json()[0]['question']),
    str(jServResp.json()[0]['answer']),
    )
    await ctx.send(triviaStr)

@bot.command()
async def pic(ctx, *, keyword: str = ""):
    await ctx.send("https://source.unsplash.com/featured/?" + keyword)

@bot.command()
async def joke(ctx):
    dJokeUrl = "https://icanhazdadjoke.com"
    jokeResp = requests.get(dJokeUrl, headers={"Accept":"application/json"})
    await ctx.send(jokeResp.json()['joke'])

@bot.command()
async def reverse(ctx, *, text: str):
    await ctx.send(text[::-1])

@bot.command()
async def inspire(ctx):
    inspBotUrl = "https://inspirobot.me/api?generate=true"
    inspImg = requests.get(inspBotUrl)
    await ctx.send(inspImg.text)

@bot.command()
async def quarantineActivities(ctx):
    activityUrl = "http://www.boredapi.com/api/activity?participants=1"
    activityResp = requests.get(activityUrl, verify=True)
    await ctx.send(activityResp.json()['activity'])

@bot.command()
async def activity(ctx):
    activityUrl = "http://www.boredapi.com/api/activity?"
    activityResp = requests.get(activityUrl, verify=True)
    await ctx.send(activityResp.json()['activity'])
bot.run(TOKEN)
