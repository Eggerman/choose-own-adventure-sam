import turtle, sys
import os

sam = turtle.Turtle()
pic = turtle.Turtle()
col = turtle.Turtle()

wn = turtle.Screen()

#s1 = True
#s2 = s3 = s4 = False
def strt():
  choose = input("Pick a character: Skeet or Jimmy")
  print("You pick", choose)
  if choose == "Skeet" or choose == "skeet":
      print("Skeet")
  elif choose == "Jimmy" or choose == "Jim" or choose == "jimmy" or choose == "jim":
      print("Jimmy")

def text():
  sam.write("Choose you own adventure! - McSpanky's Adventure", align="center", font=("Arial", 40, "normal"))
  sam.right(90)
  sam.penup()
  sam.forward(50)
  sam.write("By: Samuel Feffer", align="center", font=("Arial", 25, "normal"))
  sam.forward(50)
  sam.write("Directions: The story is created with the print command. Read the story there, and make your choices on the python screen", align="center", font=("Arial", 20, "normal"))
  #sam.forward(120)
  #sam.right(90)
  #sam.forward(10)
  #sam.left(90)
  #sam.write("You are Jimmy Neutron, a young scientist with an intense compassion for cheese. Your greatest desire is to invent a ray that will turn any carbon-based lifeform into molten, gooey cheese.\n One autumn eve, you stumbled apon a great discovery; by shooting lactic acid bacteria and milk at extremely high temperatures thorugh a ray guy into someoneone's flesh could potentially \n turn that person into molten cheese.Your plan is to apply for a job at Mcspankys and convert the restaurant into a giant flying cheese ray. You can't do this job alone though.\nTwo friends come to your mind: Sheen an Carl. Sheen is silly and is always full of energy. He's willing to follow and assist you greatly, but he's easily distracted.\n Carl loves to eat croissants, and you suspect he's in love with your mother. He's slightly cowardly and pessimistic, but he's also willing to aid you.\n Who will you choose? Click choice 1 for Sheen, or click on choice 2 for Carl", align="center", font=("Arial", 15, "normal"))
  sam.forward(50)
  sam.left(90)
  sam.right(90)
def story():
  print("You are Jimbo (Jimmy) Neutron, a young scientist with an intense compassion for cheese.")
  print("Your greatest desire is to invent a ray that will turn any carbon-based lifeform into molten, gooey cheese. One autumn eve,")
  print("you stumbled apon a great discovery; by shooting lactic acid bacteria and milk at extremely high temperatures through a ray guy into someoneone's flesh could potentially turn that person into molten cheese.")
  print("Now, all you have to do is make the ray come to life. ")
  print("Your plan is to apply for a job at Mcspankys and convert the restaurant into a giant flying cheese ray. You can't do this job alone though.")
  print("Two friends come to your mind: Sheen and Carl. Sheen is silly and is always full of energy. He's willing to follow and assist you greatly, but he's easily distracted.")
  print("Carl loves to eat croissants, and you suspect he's in love with your mother. He's slightly cowardly and pessimistic, but he's also willing to aid you.")
  print("Who will you choose? Click choice 1 for Sheen, or click on choice 2 for Carl")
  #go down to choice1 function

def sheen():
  print("1. You choose Sheen. He can be helpful at times, when he is not distracted. Your solution is not allowing him to be distracted in the first place!\nHe has good knowledge on science, and his random ideas might get you somewhere. You and Sheen walk over to Mcspankys. There, you are greeted by The employee of the month, Skeet.\nSkeet immediately likes Sheen and hires him instantaneously. You, on the other hand, Skeet dislikes.\nHe thinks you are too brainy and stupid. In reality, you can tell Skeet is dumb and can be easily manipulated.\nYou plan is to slowly convert the restaurant by day into the flying ray gun, sneak in at night with Sheen and finish the deal.\nSheen loves the new job. He is really good at it too. You end up at the cashier and cleaning up.\nYou hate it. Skeet is no help either, he hates you. He does not even know what sodium chloride is."
        "\nYou decide you should not just turn the restaurant into a cheese ray, but destroy skeet as well. Trying to destroy Skeet seems relatively easy hes dumb and stubborn. At least he seems that way.\nMaybe as the sole protector of McSpankys, he might possess unmeasurable power. Theres only one way to find out though... \n1 To not bother \n2 Destroy Skeet")

def carl():
  #print("radical")
  print("2. Sheens reckless and silly manner could get you killed. Besides, you are running the show. Carl you know will follow what you do blindly and not offer insight because he is a coward. \nWhen you share the news with Carl, he becomes elated. Carl loves food, and working at a fast food restaurant would allow him access to all the food he could possibly want. He happily agrees.\nWhen you apply at McSpankys, a man named Skeet greets you. He asks what you want to order, and you reply to him that you want to apply for a job.\nHe laughs and tells you to leave, but when he sees Carl he immediately changes his mind.\nHe hires Carl to take care of the drive through, and makes you clean the toilet.\nYou hate skeet. He thinks he is smart because he was the Employee of the Month. Skeet thinks you are dumb, and treats you like a child."
        "\nHe tries to correct you on everything you do. On top of that, he makes you dress up in a burger costume and dance out in front of the restaurant.\nBefore you take over the restaurant, Skeet has to go. But how? \nYou have two choices\n1. kidnap skeet from his house\n2. kill him when he is leaving work.")

def leave():
   print("1. Skeet is an annoyance, but since he is dumb there is probably nothing he can do to stop you.\nBesides, dealing with Skeet could create unnecessary complications and further delays.\nYou and Sheen reach an agreement, you will start the transformation of the restaurant this night, and since tomorrow is Thursday, McSpankys will be closed.\nAfter work, you and Sheen tell Skeet you both will work overtime to take care of some problems.\nHe shrugs, and leaves the restaurant. You and Sheen wait until he is out of sight, then begin the transformation.\nAll the furniture from the restaurant is removed first.\nNext, you begin to install the supercomputer. To control the ray and the flight of the restaurant.\nYou only have 3 things left to do, turn the front entrance to the restaurant a big McSpankys head into a ray gun, installing the cheese vats and connected hoses to the ray, and finally installing the jet engines and wings to allow the restaurant to fly.\nBy the time the night ends, you have completed the big ray in the mouth of McSpanky, and installed the wings and engines to allow McSpankys to fly.\nThe only thing left is the cheese and bacteria system. Sheen loves nacho, cheddar cheese and wants to fill the vat with it.\nYou argue Mozzarella cheese is better. He points out Mozzarella is more money, but only a little more.\n1. For Cheddar \n2. For Mozzarella")
#subgroups of leave are ched and moz
def ched():
   print("1. Cheddar Nacho cheese is the best. You out rule Skeet, it is your plan anyway. Since you got to pick the cheese, you agreed to allow Sheen to put his own addition to the restaurant.\nSheen is obsessed with the Ultra Lord, and decides to model the restaurant around him. In the morning, the Ultra Lord McSpankys is ready.\nYou fly around town turning buildings and homes into molten nacho cheese. \nSoon, everything on planet earth will be transformed into cheese.\nTHE END.")

def moz():
   print("2. Mozzarella cheese will have to do. You get working on the restaurant, and 15 minutes in you hear a strange noise coming from the ketchup bottles.\nYou take a closer look and realize they are bombs! Before you have a chance to scream, your head is blown clean off.\nTHE END.")
def destroy():
   print("2. Skeet has to go. He will just get in the way, and since he is stupid, he should not be hard to eliminate. You plan to follow him home from work, and execute him in his home.\nYou can not imagine he has friends or lives with anyone, and by the time it is discovered he is dead, no one will be able to take action, for you and Sheen will conquer Earth.\nThat night as Sheen leaves, you sneak out into the alley to your spaceship and observe Skeet wearily climb into his car. As he drives off, you carefully follow him in your craft as you do not want him to spot you or allow him to hear you.\nFinally, after 15 minutes of driving, Skeet finally turns in his driveway and enters his house. You wait until you see the lights go out, and then you proceed to enter his house.\nYou pick the lock to his front door, then creep along his hallway. As you are sneaking, you hear faint whispering, almost like some kind of chanting.\nAs you creep closer, the whispering grows louder, and soon enough you can make out what is being said, but you cannot understand what is being transmitted.\nIt sounds like gibberish, but as you listen closer, you realize it could be an alien language. Then, in the midst of the whispering, you hear Skeet exclaim, he is here right now!\nHe started working for me about two days ago. He is planning on taking over the restaurant."
         "\nYou freeze. Skeet knows you are hiding! You start to run away from you, but it is too late.\nSkeet burst through the door with three aliens. He pulls out a strange looking alien like ray gun.\nHe cocks in and points it at you. He looks at you and say, sorry kid. It is nothing personal.\nAlmost instantly, you are vaporized into molten cheese.\nTHE END.")
def nap():
   print("1. You highly detest Skeet. Killing him might be taking it too far, so you decide just to kidnap him. Maybe his knowledge on the restaurant can come in handy, and you are sure you can force him into laboring and revealing secrets.\nCarl is also in on the plan. After work, Carl invites Skeet over to his house. Skeet likes Carl and accepts his invitation.\nCarl then proceeds to take Skeet to your house, not his. There, Carl feeds croissants laced with knockout drugs to Skeet to make him fall asleep.\nNext, you and Carl tie him up and place him in your basement. Tomorrow is Thursday, and that means McSpankys is closed.\nAll thursday you and Carl work on the restaurant. By dusk, it is ready.\nThe restaurant looks amazing. It is equipped with a giant cheese ray, flying gear, and a machine that shoots explosive croissants."
         "\nThat night, you and Carl power up the restaurant and the cheese ray. You fly across town turning everything into molten cheese. When you meet resistance, you just shoot explosive croissants at the enemy, and they explode on impact.\nSoon your town is in ruins, and you proceed to conquer the globe. Before long, everything on Earth is molten cheese, even all the oceans.\nYou park your craft on the remains of the beach, and take a plunge into the warm, gooey cheese.\nTHE END.")
def kill():
   print("2. Skeet has to go, immediately. Besides, no one will be able to stop you when you and Carl run the world. You and Carl follow Skeet home from work.\nYou pick the lock, and proceed to creep in the hallways. You and Carl freeze, you hear a noise!\nAs the two of you crawl close to the noise, you can make out low whispering.\nAs you get even closer, you realize the language sounds alien. Your head is spinning.\nHow could a simpleton like Skeet have aliens living in his house. Then, out of nowhere, you hear them say, they are here right now.\nExterminate them. You and Carl freeze, and right then you hear the beings in the room head in your direction.\nYou do not waste time, and burst into the livingroom.\nYou see Skeet surrounded by three aliens, all pointing guns at you. Skeet is holding a giant samurai sword. Skeet begins to talk, but Carl does not waste any time."
         "\nHe hurls a croissant at the nearest alien. It cuts his head clean off! Confused Skeet looks at Carl in disbelief.\nLike Carl, you do not waste time.\nYou pull out a Bop It XT and swing it at Skeet. It vaporizes him instantly.\nThe remaining two aliens being so scared, simultaneously combust leaving a pool of Diet Pepsi. You and Carl proceed to take over the world, and no one even puts up a fight.\nTHE END.")

def button():
  sam.pendown()
  sam.speed(100)
  for i in range(37):
      sam.forward(5)
      sam.right(10)
  sam.right(80)
  sam.penup()
  sam.forward(28)
  sam.pendown()
  sam.left(90)
  sam.forward(15)
  sam.right(180)
  sam.forward(30)
  sam.penup()
  sam.right(90)
  sam.forward(100)
  sam.pendown()
  sam.right(90)
  sam.penup()
  sam.forward(10)
  sam.pendown()
  for i in range(37):
      sam.forward(5)
      sam.right(10)
  sam.right(80)
  sam.penup()
  sam.forward(18)
  sam.pendown()
  sam.left(90)
  sam.forward(15)
  sam.right(180)
  sam.forward(30)
  sam.penup()
  sam.left(90)
  sam.forward(18)
  sam.pendown()
  sam.left(90)
  sam.forward(30)
  sam.penup()
  sam.forward(50)
  #

def stuf():
  sam.goto(-173.0, -143.0)
  sam.pendown()
  sam.write("Choice 1", align="center", font=("Arial", 25, "normal"))
  sam.penup()
  sam.goto(-173, -253)
  sam.pendown()
  sam.write("Choice 2", align="center", font=("Arial", 25, "normal"))
  sam.penup()
  sam.goto(-173, -363)
  sam.pendown()
  sam.write("Choice 3", align="center", font=("Arial", 25, "normal"))
  sam.penup()
  sam.goto(-173, -473)
  sam.pendown()
  sam.write("Choice 4", align="center", font=("Arial", 25, "normal"))
  sam.penup()

def choice1(x, y):
  print(x, y)

#first choice
  if x < 5 and x > -63 and y < -117 and y > -187:
      print("You choose Sheen.")
      sam.goto(-281.0, -208.0)
      sam.write("You choose Sheen", align="center", font=("Arial", 20, "normal"))
      sam.forward(15)
      sam.goto(-300.0, -240.0)
      drawCircles()
      sheen()
          #secondFunctio()
  elif x > 9 and x < 79 and y < -117 and y > -187:
          print("You choose Carl.")
          sam.goto(281.0, -208.0)
          sam.write("You choose Carl", align="center", font=("Arial", 20, "normal"))
          sam.forward(15)
          sam.goto(285.0, -240.0)
          drawCircles()
          carl()

#first choices for Sheen
  if x > -362 and x < -297 and y < -207 and y > -280:
      print("Leave skeet be")
      sam.goto(-519, -317)
      sam.write("Leave Skeet alone", align="center", font=("Arial", 20, "normal"))
      sam.forward(30)
      drawCircles()
      leave()
      #put in function that prints story
  elif x > -290 and x < -224 and y < -207 and y > -280:
      print("Destroy Skeet")
      sam.goto(-174.0, -302.0)
      #sam.write("THE END", align="center", font=("Arial", 20, "normal"))
      #sam.forward(50)
      #function that prints story
      destroy()

   #Carl choices
  if x > 223 and x < 290 and y < -210 and y > -278:
       nap()
  elif x > 297 and x < 361 and y < -210 and y > -278:
      kill()

   #cheese choices
  if x > -1012 and x < -942 and y < -311:
       #print("yuhh")
       ched()
  elif x > -943 and x < -871 and y < -311:
      #print("moz")
      moz()

def drawCircles():
  sam.pendown()
  sam.speed(100)
  for i in range(37):
      sam.forward(5)
      sam.right(10)
  sam.right(80)
  sam.penup()
  sam.forward(28)
  sam.pendown()
  sam.left(90)
  sam.forward(15)
  sam.right(180)
  sam.forward(30)
  sam.penup()
  sam.right(90)
  sam.forward(100)
  sam.pendown()
  sam.right(90)
  sam.penup()
  sam.forward(10)
  sam.pendown()
  for i in range(37):
      sam.forward(5)
      sam.right(10)
  sam.right(80)
  sam.penup()
  sam.forward(18)
  sam.pendown()
  sam.left(90)
  sam.forward(15)
  sam.right(180)
  sam.forward(30)
  sam.penup()
  sam.left(90)
  sam.forward(18)
  sam.pendown()
  sam.left(90)
  sam.forward(30)
  sam.penup()
  sam.forward(50)


def main():
  #strt()
  text()
  story()
  button()
  #stuf()
  wn.addshape(os.path.expanduser("nutron.gif"))
  pic.shape(os.path.expanduser("nutron.gif"))
  pic.penup()
  pic.left(90)
  pic.forward(300)

  wn.onscreenclick(choice1)
  turtle.done()

main()
