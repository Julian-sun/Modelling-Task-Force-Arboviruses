import urllib
import time
import numpy as np
from datetime import date
import warnings
warnings.filterwarnings("ignore")

urlorig='ftp://ftp.datasus.gov.br/dissemin/publicos'
page=urllib.request.urlopen(urlorig).read()
line=page.decode("utf-8", "replace").replace('�','Á').split('\r\n')
line=line[:-1]
listdir=[]
for l in line:
  listdir.append(l[39:])
print('\n> Select one option:')
for i,aux in enumerate(listdir):
  print ('    '+str(i)+' = '+aux)
opt=len(listdir)
while opt>len(listdir)-1 or opt<0:
  try:
    opt = int(input('> '))
  except:
    print('Something is not correct, please try again!')
    opt = -1
url=urlorig+'/'+listdir[opt]
print('    Option selected: '+listdir[opt]+'.')
file=line[opt][25:28]
config=listdir[opt]

while file=='DIR':
  page=urllib.request.urlopen(url).read()
  line=page.decode("utf-8", "replace").split('\r\n')
  line=line[:-1]
  listdir=np.array([],dtype=str)
  listdesease=np.array([],dtype=str)
  listyear=np.array([],dtype=str)
  liststate=np.array([],dtype=str)
  for l in line:
    listdir=np.append(listdir,l[39:])
    if len(l[39:])==12 and l[25:28]!='DIR':
      try:
        listdesease=np.append(listdesease,l[39:43])
      except:
        listdesease=np.append(listdesease,'')
      try:
        liststate=np.append(liststate,l[43:45])
      except:
        liststate=np.append(liststate,'')
      try:
        listyear=np.append(listyear,l[45:47])
      except:
        listyear=np.append(listyear,'')
    elif l[25:28]!='DIR' and config=='SINAN':
      try:
        listdesease=np.append(listdesease,l[39:42].upper())
      except:
        listdesease=np.append(listdesease,'')
      try:
        liststate=np.append(liststate,l[42:44].upper())
      except:
        liststate=np.append(liststate,'')
      try:
        listyear=np.append(listyear,l[44:46])
      except:
        listyear=np.append(listyear,'')
  file = l[25:28]

  if l[25:28]=='DIR':
    print('\n> Select one option:')
    for i,aux in enumerate(listdir):
      print ('    '+str(i)+' = '+aux)
    opt=len(listdir)
    while opt>len(listdir)-1 or opt<0:
      try:
        opt = int(input('> '))
      except:
        print('Something is not correct, please try again!')
        opt = -1
    url=url+'/'+listdir[opt]
    print('    Option selected: '+listdir[opt]+'.')


  elif config=='SINAN':
# if zip or pdf doesnt work
    if l[-3:]!='dbc':
      print('This program doesnt open '+l[-3:]+' files.')
      file=''
    else:      
      print('\n> Select deseases separated by ",":')
      for i,aux in enumerate(np.unique(list(map(str.upper,listdesease)))):
        print ('    '+str(i)+' = '+aux)
      opt=[len(np.unique(listdesease))]
      valid=False
      while not valid or opt[0]<0:
        try:
          opt = list(map(int,input('> ').split(',')))
          if len(opt)>1 and sum(i > len(np.unique(listdesease))-1 for i in opt)==0:
            valid=True
          else:
            if opt[0]<len(np.unique(listdesease))-1:
              valid=True
        except:
          print('Something is not correct, please try again!')
          opt = [-1]
      desease=np.unique(list(map(str.upper,listdesease)))[opt]
      if len(desease)>1:
        print('    Options selected: '+', '.join(desease)+'.')
      else:
        print('    Option selected: '+desease[0]+'.')
      
      indexD=np.array([],dtype=int)
      for ide in desease:
        indexD=np.append(indexD,np.where(listdesease==ide)[0])
      print('\n> Select States separated by ",":')
      optstate=np.unique(list(map(str.upper,liststate[indexD])))
      for i,aux in enumerate(optstate):
        print ('    '+str(i)+' = '+aux)
      opt=[len(optstate)]
      valid=False
      while not valid or opt[0]<0:
        try:
          opt = list(map(int,input('> ').split(',')))
          if len(opt)>1 and sum(i > len(optstate)-1 for i in opt)==0:
            valid=True
          else:
            if opt[0]<len(optstate)-1:
              valid=True
        except:
          print('Something is not correct, please try again!')
          opt = [-1]
      state=optstate[opt]
      if len(state)>1:
        print('    Options selected: '+', '.join(state)+'.')
      else:
        print('    Option selected: '+state[0]+'.')

      indexS=np.array([],dtype=int)
      for ist in state:
        indexS=np.append(indexS,indexD[np.where(liststate[indexD]==ist)[0]])
      optyear=np.unique(listyear[indexS])
      print('\n> Select years separated by ",":')
      for i,aux in enumerate(optyear):
        if i>time.localtime().tm_year-2000:
          print ('    '+str(i)+' = 19'+aux)
        else:
          print ('    '+str(i)+' = 20'+aux)
      opt=[len(optyear)]
      valid=False
      while not valid or opt[0]<0:
        try:
          opt = list(map(int,input('> ').split(',')))
          if len(opt)>1 and sum(i > len(optyear)-1 for i in opt)==0:
            valid=True
          else:
            if opt[0]<len(optyear)-1:
              valid=True
        except:
          print('Something is not correct, please try again!')
          opt = [-1]
      year=optyear[opt]

      optyear=[]
      indexY=np.array([],dtype=int)
      for iyr in year:
        indexY=np.append(indexY,indexS[np.where(listyear[indexS]==iyr)[0]])
        if int(iyr)>time.localtime().tm_year-2000:
          optyear.append('19'+iyr)
        else:
          optyear.append('20'+iyr)        
      if len(optyear)>1:
        print('    Options selected: '+', '.join(optyear)+'.')
      else:
        print('    Option selected: '+optyear[0]+'.')          

      file=''

files=[]
for ifil in listdir[indexY]:
  files.append(url+'/'+ifil)



# ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/TETNES18.dbc

# comparar versao do bd
# oq nao tem baixa
# se tem nova versao baixa nova
# o q tem na pasta q nao tem no site