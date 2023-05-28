#for install
print('Cntrl+V your Ryujinx.exe directory and press enter. Sample C:\Games\publish')
ryujinx_dist = input()
#ryujinx_dist+= '/Ryujinx.exe'
print('Cntrl+V your main.py directory and press enter. Sample C:\Games')
main_dist = input()
#main_dist += '/main.py'
ryujinx_dist=ryujinx_dist.replace('\\','/')
main_dist=main_dist.replace('\\','/')
print (ryujinx_dist + ' and ' + main_dist)

file_bat=open('Reserv_Copy_Ryujinx.bat', 'w',encoding = "utf-8" )
file_bat.write('@echo off \n cd "' + main_dist + '" \n start main.py \n cd "' + ryujinx_dist + '" \n start Ryujinx.exe \n exit')
file_bat.close()
print ('ok')

print('Cntrl+V your save dir and press enter. Sample C:\Games\publish')
from_dist = input()
print('Cntrl+V your save reserv save dir and press enter. Sample C:\Games\publish')
to_dist = input()
print (from_dist + ' and ' + to_dist)

to_dist=to_dist.replace('\\','/')
from_dist=from_dist.replace('\\','/')

file_reserv = open('game_reserv_dirrectory.py','w')
file_reserv.write('from_dist = \'' + from_dist + '\'\n' + 'to_dist = \'' + to_dist + '\'' ) #kovichki prover'
file_reserv.close()
print ('ok')

