# vim: set filetype=python ts=2 sw=2 sts=2 expandtab: 
import sys
sys.dont_write_bytecode = True

from machine import Machine
from lib import maybe

# usage:
#   python fsm.py 21083 # for a long-ish run
#   python fsm.py 1     # for a short run

# subclass machine

# ----------------------------------------------
def fsm0(label):
  m     = Machine(label)
  s,t   = m.S, m.T
  foo   = s("foo")
  bar   = s("bar")
  #-- machine
  t(s("entry"), walk, foo)
  t(foo,        walk, foo)
  t(foo,        sit,  s("stop."))
  return m
 
# ----------------------------------------------
def walk(w, a):  return maybe()
def sit(w, a):   return maybe()
def ok(w, a):    return True
def fail(w, a):  return maybe()
def again(w, a): return maybe()

if __name__ == '__main__':
  fsm0(1)
  fsm0(2)
  fsm0(4)
  if len(sys.argv) > 1:
    Machine.run(int(sys.argv[1]))
  else:
    Machine.run()
