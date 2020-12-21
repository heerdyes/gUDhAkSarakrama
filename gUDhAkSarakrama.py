from PIL import Image
import sys

# ------------ #
# funxionality #
# ------------ #
def extractchar(pixlist):
  if len(pixlist)!=3:
    raise Exception('exactly 3 pixels must be passed')
  bitstr=''
  for p in pixlist:
    bitstr+='0' if p[0]%2==0 else '1'
    bitstr+='0' if p[1]%2==0 else '1'
    bitstr+='0' if p[2]%2==0 else '1'
  return chr(int(bitstr,2))

def extractstring(img,n):
  s=''
  for i in range(n):
    p1=img.getpixel((i*3,0))
    p2=img.getpixel((i*3+1,0))
    p3=img.getpixel((i*3+2,0))
    s+=extractchar([p1,p2,p3])
  return s

# use this for infinite for loops
def zero_to_infinity():
  i=0
  while True:
    yield i
    i+=1

def extractstringtilleof(img,eofchar):
  s=''
  w,h=img.size[0],img.size[1]
  for i in range(w*h//3):
    p1=img.getpixel((i*3,0))
    p2=img.getpixel((i*3+1,0))
    p3=img.getpixel((i*3+2,0))
    c=extractchar([p1,p2,p3])
    if c==eofchar:
      break
    s+=c
  return s

def tamperpixel(bs,px):
  return tuple(x+1 if x%2==0 and bs[i]=='1' or x%2!=0 and bs[i]=='0' else x for i,x in enumerate(px))

def injectstring(img,s):
  print('injecting payload: %s'%s)
  ctr=0
  w,h=img.size[0],img.size[1]
  print('image dimensions: width: %d, height: %d'%(w,h))
  for c in s:
    bitstr="{0:09b}".format(ord(c))
    p0=img.getpixel((ctr%w,ctr//h))
    img.putpixel((ctr%w,ctr//h),tamperpixel(bitstr[0:3],p0))
    ctr+=1
    p1=img.getpixel((ctr%w,ctr//h))
    img.putpixel((ctr%w,ctr//h),tamperpixel(bitstr[3:6],p1))
    ctr+=1
    p2=img.getpixel((ctr%w,ctr//h))
    img.putpixel((ctr%w,ctr//h),tamperpixel(bitstr[6:9],p2))
    ctr+=1

def transmute(imgin,sdat,imgout):
  try:
    img=Image.open(imgin)
    injectstring(img,sdat)
    img.save(imgout)
    img.close()
  except IOError as ioe:
    print(str(ioe))

def glimpse(imgin,slen):
  try:
    img=Image.open(imgin)
    dstr=extractstring(img,slen)
    img.close()
    return dstr
  except IOError as ioe:
    print(str(ioe))

def perceive(imgin,eofchar):
  try:
    img=Image.open(imgin)
    dstr=extractstringtilleof(img,eofchar)
    img.close()
    return dstr
  except IOError as ioe:
    print(str(ioe))

def chkfree(imgin):
  try:
    img=Image.open(imgin)
    w,h=img.size[0],img.size[1]
    print('[%s] total pixels: %d, embed capacity: %d bytes'%(imgin,w*h,w*h//3))
    img.close()
  except IOError as ioe:
    print(str(ioe))
