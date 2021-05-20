Temp_c = 28
Temp_f = ((Temp_c *9/5 ) +32)
if(Temp_f <= 32):
    Temp_f = "its winter...stay home"
elif(Temp_f >= 33  >=55):
    Temp_f = "its fall have a pumpkin flavored anything"
elif(Temp_f>= 56  >=75):
    Temp_f = "its spring...time to lose that weight"
else:
    Temp_f = "better have lost that weight cause its beach season"
print (Temp_f)