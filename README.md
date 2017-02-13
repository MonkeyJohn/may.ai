# may.ai
OpenAI Universe solver with opencv and a bag of tricks

`mayai` in swahili means `egg`. 

# Hypothesis
Deep Q learning sends a bunch of pixels into a cnn and then to a rnn to output the next action. This is quite simple and elegant. Although what you notice from the play is it takes a really long time to learn and get some output out of it.

Mayai maps the obervation to a feature vector of objects. Suppose you were to write python code to solve atari games in a generalized way, and you are not a deep learning expert what would you do. This is an exploration of that topic.

The idea is to use opencv to build a feature vecture from raw rgb pixels of the observation, 



e.g

```
struct object {
  type: number // all objects that look like this will get the same type
  boundingBox: float[4]
  position: float[2]
  velocity: float[2]
  
  
```
Opencv
