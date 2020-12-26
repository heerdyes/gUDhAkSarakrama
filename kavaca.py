from gUDhAkSarakrama import *

# command functions #
def cmd_cs(args):
  if len(args)!=3:
    raise Exception('need 3 arguments for cmd_cs')
  imgin=args[0]
  sdat=args[1]
  imgout=args[2]
  print('transmutation: <%s> + <%s> -> <%s>'%(imgin,sdat,imgout))
  transmute(imgin,sdat,imgout)

def cmd_cf(args):
  if len(args)!=3:
    raise Exception('need 3 arguments for cmd_cf')
  imgin=args[0]
  fdat=args[1]
  imgout=args[2]
  print('transmutation: <%s> + <%s> -> <%s>'%(imgin,fdat,imgout))
  with open(fdat) as df:
    substance=''.join(df.readlines())
    substance+='~'
    transmute(imgin,substance,imgout)

def cmd_rn(args):
  if len(args)!=2:
    raise Exception('need 2 argument for cmd_rn')
  imgin=args[0]
  slen=int(args[1])
  print('revelation: perceiving file [%s]'%imgin)
  sdata=glimpse(imgin,slen)
  print(sdata)

def cmd_rz(args):
  if len(args)!=2:
    raise Exception('need 2 argument for cmd_rz')
  imgin=args[0]
  eofchar=args[1]
  print('revelation: perceiving file [%s]'%imgin)
  sdata=perceive(imgin,eofchar)
  print(sdata)

def cmd_df(args):
  if len(args)!=1:
    raise Exception('need 1 argument for cmd_df')
  imgin=args[0]
  chkfree(imgin)

def cmd_l(args):
  print('available commands are:')
  print('cf <imgin> <fdat> <imgout>       => concealment: <imgin> + <fdat> -> <imgout>')
  print('cs <imgin> <sdat> <imgout>       => concealment: <imgin> + <sdat> -> <imgout>')
  print('rn <imgin> <slen>                => revelation: <imgin> -> data[slen] + img')
  print('rz <imgin> <eofchar>             => revelation: <imgin> -> data[0:indexof(eofchar)] + img')
  print('df <imgin>                       => check embeddable (free) space in <imgin>')
  print('l|h|help                         => this help menu')
  print('exit|x|X|bye|Q|q|quit            => quit program')

# the global command map #
cmdmap={
  'cs':cmd_cs,
  'cf':cmd_cf,
  'rn':cmd_rn,
  'rz':cmd_rz,
  'df':cmd_df,
  'l':cmd_l,
  'h':cmd_l,
  'help':cmd_l
}

def interpretcmd(cmd,params):
  if cmd in cmdmap:
    try:
      cmdmap[cmd](params)
    except Exception as e:
      print(str(e))
  else:
    print('unknown command: %s'%cmd)

# the repl #
def grepl(cmdline):
  cmdline=cmdline.strip()
  if cmdline in ['exit','bye','quit','Q','q','x','X']:
    print('bye!')
    return False
  parts=cmdline.split(' ')
  cmd=parts[0]
  args=parts[1:]
  interpretcmd(cmd,args)
  return True
