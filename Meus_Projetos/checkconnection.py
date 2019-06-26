#!/usr/bin/python

import os, re

print "Verificando conexao..."
pergunta = raw_input ("Digite o IP:")
cmd = "ping -c4 " + pergunta
r = "".join(os.popen(cmd).readlines())
print r

if re.search ("64 bytes from", r):
  print "Link UP"
else:
  print "Link Down"
