# ChessBot reopening script

import os
import time

def reopen_chessbot():
  while True:
    chessbot_status = os.popen("tasklist | findstr ChessBot.exe").read()
    if "ChessBot.exe" not in chessbot_status:
      os.startfile("C:\ChessBot/ChessBot.exe")
      time.sleep(1)
    else:
      time.sleep(1)

# Start the ChessBot reopening script
reopen_chessbot()
