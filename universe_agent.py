import gym
import universe
import cv2
import numpy as np
from mayai import io

games = ["AirRaid-v0","Alien-v0","Amidar-v0","Assault-v0","Asterix-v0","Asteroids-v0",
"Atlantis-v0","BankHeist-v0","BattleZone-v0","BeamRider-v0","Berzerk-v0","Bowling-v0",
"Boxing-v0","Breakout-v0","Carnival-v0","Centipede-v0","ChopperCommand-v0",
"CrazyClimber-v0","DemonAttack-v0","DoubleDunk-v0","ElevatorAction-v0","Enduro-v0",
"FishingDerby-v0","Freeway-v0","Frostbite-v0","Gopher-v0","Gravitar-v0","IceHockey-v0",
"Jamesbond-v0","JourneyEscape-v0","Kangaroo-v0","Krull-v0","KungFuMaster-v0",
"MontezumaRevenge-v0","MsPacman-v0","NameThisGame-v0","Phoenix-v0","Pitfall-v0",
"Pong-v0","Pooyan-v0","PrivateEye-v0","Qbert-v0","Riverraid-v0","RoadRunner-v0",
"Robotank-v0","Seaquest-v0","Skiing-v0","Solaris-v0","SpaceInvaders-v0","StarGunner-v0",
"Tennis-v0","TimePilot-v0","Tutankham-v0","UpNDown-v0","Venture-v0","VideoPinball-v0",
"WizardOfWor-v0","YarsRevenge-v0","Zaxxon-v0"]

# 56 Games, 1 algorithm

gameName = 'Breakout-v0'
score = 0
done = False

print("Game: {}".format(gameName))
env = gym.make(gameName)
env.configure()
env.reset()

while not done:
  img = env.render(mode='rgb_array')
  io.show_image(img)
  action = io.wait_keyboard_action(10)
  _, reward, done, _ = env.step(action)
  score += reward

  if reward:
    print("Score:", score)

print("Final Score", score)