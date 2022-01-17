import csv

filename = "shots_data.csv"


# initializing the titles and rows list
cols = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    cols = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)





TeamA_X = [0]*280
TeamA_Y = [0]*280
TeamB_X = [0]*280
TeamB_Y = [0]*280
TeamA_fg = [0]*280
TeamB_fg = [0]*280


for j in range(560):
    if(j < 280):
        TeamA_X[j] = float(rows[j][1])
        TeamA_Y[j] = float(rows[j][2])
        TeamA_fg[j] = int(rows[j][3])
    if(j >= 280):
        TeamB_X[j - 280] = float(rows[j][1])
        TeamB_Y[j - 280] = float(rows[j][2])
        TeamB_fg[j -280] = int(rows[j][3])

TeamA_C3 = int(0)
TeamA_C3M = int(0)
TeamA_NC3 = int(0)
TeamA_NC3M = int(0)
TeamA_2PT = int(0)
TeamA_2PTM = int(0)
TeamB_C3 = int(0)
TeamB_C3M = int(0)
TeamB_NC3 = int(0)
TeamB_NC3M = int(0)
TeamB_2PT = int(0)
TeamB_2PTM = int(0)

for i in range(len(rows)):
    if(i < 280):
        #corner threes first
        if( ((TeamA_X[i]**2) + (TeamA_Y[i]**2)**0.5) >= 22 and TeamA_Y[i] <= 7.8): #corner thress have to have the Y coordinate less than or equal to 7.8, and the distance has to be greater than 22
            TeamA_C3 = TeamA_C3 + 1
            if(TeamA_fg[i] == 1):
                TeamA_C3M = TeamA_C3M + 1
        #Non-corner threes
        elif(TeamA_Y[i] > 7.8 and (( (TeamA_X[i]**2) + (TeamA_Y[i]**2)**0.5   ) ) >= 23.75): #non-corner threes have to have a Y coordinate greater than 7.8 and distance greater than or equal to 23.75
            TeamA_NC3 = TeamA_NC3 + 1
            if(TeamA_fg[i] == 1):
                TeamA_NC3M = TeamA_NC3M + 1
        #Two point shots
        elif( (( (TeamA_X[i]**2) + (TeamA_Y[i]**2)**0.5   ) ) < 23.75  and abs(TeamA_X[i] < 22)): #two point shots have to have the absolute value of the x coordinate less than 22 and the distance less than 23.75
            TeamA_2PT = TeamA_2PT + 1
            if(TeamA_fg[i] == 1):
                TeamA_2PTM = TeamA_2PTM + 1
    if(i >= 280):
        #corner threes first
        if( ((TeamB_X[i - 280]**2) + (TeamB_Y[i - 280]**2)**0.5) >= 22 and TeamB_Y[i - 280] <= 7.8):
            TeamB_C3 = TeamB_C3 + 1
            if(TeamB_fg[i - 280] == 1):
                TeamB_C3M = TeamB_C3M + 1
        #Non-corner threes
        elif(TeamB_Y[i - 280] > 7.8 and (( (TeamB_X[i - 280]**2) + (TeamB_Y[i - 280]**2)**0.5   ) ) >= 23.75):
            TeamB_NC3 = TeamB_NC3 + 1
            if(TeamB_fg[i - 280] == 1):
                TeamB_NC3M = TeamB_NC3M + 1
        #Two point shots
        elif( (( (TeamB_X[i - 280]**2) + (TeamB_Y[i - 280]**2)**0.5   ) ) < 23.75  and abs(TeamB_X[i - 280] < 22)):
            TeamB_2PT = TeamB_2PT + 1
            if(TeamB_fg[i - 280] == 1):
                TeamB_2PTM = TeamB_2PTM + 1

 #Verifying total shots for each is 280
TeamA_total = TeamA_C3 + TeamA_NC3 + TeamA_2PT 
TeamB_total = TeamB_C3 + TeamB_NC3 + TeamB_2PT

#verifying total field goals made, checked using google sheets
TeamA_TFGM = TeamA_NC3M + TeamA_2PTM + TeamA_C3M
TeamB_TFGM = TeamB_NC3M + TeamB_2PTM + TeamB_C3M


#eFG = (FGM +(0.5*3PM))/FGA
TeamA_C3_efg = ((1.5*TeamA_C3M)/TeamA_C3)*100
TeamA_NC3_efg = ((1.5*TeamA_NC3M)/TeamA_NC3)*100
TeamA_2PT_efg = ((TeamA_2PTM)/TeamA_2PT)*100
TeamB_C3_efg = ((1.5*TeamB_C3M)/TeamB_C3)*100
TeamB_NC3_efg = ((1.5*TeamB_NC3M)/TeamB_NC3)*100
TeamB_2PT_efg = ((TeamB_2PTM)/TeamB_2PT)*100

#Printing findings
print("Shot Distribution: ")
print("Team A: ")
print("Corner Threes: " + str((TeamA_C3/TeamA_total)*100) + "%")
print("Non-corner Threes: " + str((TeamA_NC3/TeamA_total)*100) + "%")
print("Two point shots: " + str((TeamA_2PT/TeamA_total)*100) + "%")
print("Team B: ")
print("Corner Threes: " + str((TeamB_C3/TeamB_total)*100) + "%")
print("Non-corner Threes: " + str((TeamB_NC3/TeamB_total)*100) + "%")
print("Two point shots: " + str((TeamB_2PT/TeamB_total)*100) + "%")

print("Shot efg%: ")
print("TeamA: ")
print("Corner Threes efg%: " + str(TeamA_C3_efg) + "%")
print("Non-corner Threes efg%: " + str(TeamA_NC3_efg) + "%")
print("Two point efg%: " + str(TeamA_2PT_efg) + "%")
print("TeamB: ")
print("Corner Threes efg%: " + str(TeamB_C3_efg) + "%")
print("Non-corner Threes efg%: " + str(TeamB_NC3_efg) + "%")
print("Two point efg%: " + str(TeamB_2PT_efg) + "%")

