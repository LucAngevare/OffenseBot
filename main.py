import discord
import json

class MyClient(discord.Client):
    async def on_ready(self):
      #This basically just says who it is
      print('Logged on as', self.user)

    async def on_message(self, message):
      #Everyone with the name Alfreaca gets ignored
      #Haha fuck you Alf, you're being skippedd
      #Nah man jk love you (nohomo tho)
      member = discord.utils.get(message.guild.members, name='Alfreaca')

      #I came up with this genius loop so it doesn't loop over it's own messages.
      if member != message.author:
        if message.author == self.user:
          return

        #This OCR feature has killed me so I killed it haha

        #Open the words.json file, and make it a list
        with open("words.json") as f:
          datas = json.loads(f.read())
          datas = datas["words"]

        #This is the loop for checking the words.json file
        for data in datas:
          if data in str(message.content).lower():
            #This loads up the OffenseWarnings channe;
            modroom = client.get_channel(568732658411110410)
            print(message.author)

            #Again, absolutely genius
            if message.author != self.user:
              await message.delete()
            
            #Tells momma anyway
            #brothers (◔_◔) amirite
            await modroom.send("{0} said `{1}`, which consists of a blacklisted word.".format(message.author, message.content))

            #This DM's the dude/dudina to not do it again or it'll tell mommy
            channel = await message.author.create_dm()
            await channel.send("You said `{}`, which consists of a blacklisted word. You have been added to the list of warnings, meaning that if you do this again, you will be banned/kicked/muted.".format(message.content))

#This just runs the class
client = MyClient()

#This runs the bot
client.run("#")
#I ain't falling for it again haha fuck you sync
#no jk man, love you 2 (nohomo tho)