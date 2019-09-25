#!/usr/bin/env python
# coding: utf-8

"""
This example shows how sending a single message works.
"""

from __future__ import print_function

import can

def hellocan():
    # define busses
    bustype='socketcan'
    senderBus  ='can0'
    receiverBus='can1'
    bitrate=1000000
    
    sender = can.interface.Bus(bustype=bustype,
      channel = senderBus,
      bitrate = bitrate,
      receive_own_messages = True)
      
    listener = can.interface.Bus(bustype=bustype,
      channel = receiverBus,
      bitrate = bitrate)
    
    # define a sample message
    msg = can.Message(arbitration_id=0xc0ffee,
      data=[0, 25, 0, 1, 3, 1, 4, 1],
      is_extended_id=True)

    # send and receive
    try:
          listener.recv()
          sender.send(msg)
          print("Message sent on {}".format(sender.channel_info))
    except can.CanError:
        print("Message NOT sent")

if __name__ == '__main__':
    hellocan()
