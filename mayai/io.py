import cv2

ACTION_NOOP = 0
ACTION_FIRE = 1
ACTION_UP = 2
ACTION_RIGHT = 3
ACTION_LEFT = 4
ACTION_DOWN = 5
ACTION_UPRIGHT = 6
ACTION_UPLEFT = 7
ACTION_DOWNRIGHT = 8
ACTION_DOWNLEFT = 9
ACTION_UPFIRE = 10
ACTION_RIGHTFIRE = 11
ACTION_LEFTFIRE = 12
ACTION_DOWNFIRE = 13
ACTION_UPRIGHTFIRE = 14
ACTION_UPLEFTFIRE = 15
ACTION_DOWNRIGHTFIRE = 16
ACTION_DOWNLEFTFIRE = 17

ZERO_KEY_CODE = 48

ACTION_KEYS = {
    32: ACTION_FIRE, # Space
    63232: ACTION_UP,
    63233: ACTION_DOWN,
    63234: ACTION_LEFT,
    63235: ACTION_RIGHT,
}

def action_from_key(key):
    if key == 27 or key == 113: # Esc or q
        exit()
    elif key >= ZERO_KEY_CODE and key <= (ZERO_KEY_CODE + 9): # Numeric keys
        action = key - ZERO_KEY_CODE
    elif key in ACTION_KEYS:
        action = ACTION_KEYS[key]
    else:
        action = ACTION_NOOP
    return action

def show_image(img):
  img = cv2.resize(img, None, fx=3.0, fy=3.0)
  cv2.imshow("Game", img)

def wait_keyboard_action(waitMs=50):
  key = cv2.waitKey(waitMs)
  return action_from_key(key)