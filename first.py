import survey
table = survey.Pregnancies()
table.ReadRecords()
print( 'Number of pregnancies', len(table.records))

LiveBirthCount = 0
FirstBaby = 0
OtherBaby = 0

SumFirstBabyWeeks = 0
SumOtherBabyWeeks = 0

for record in table.records:
    if record.outcome == 1:
        LiveBirthCount += 1
        if record.birthord == 1:
            FirstBaby += 1
            SumFirstBabyWeeks += record.prglength
        else:
            OtherBaby += 1
            SumOtherBabyWeeks += record.prglength

AvgFirst = SumFirstBabyWeeks / FirstBaby
AvgOther = SumFirstBabyWeeks / OtherBaby
Diff = str(AvgFirst - AvgOther) + ' weeks more'

print('Live Birth Count: ' + str(LiveBirthCount))
print('Live Birth Count - First: ' + str(FirstBaby))
print('Live Birth Count - Other: ' + str(OtherBaby))

print('Avg First Baby Weeks: ' + str(AvgFirst))
print('Avg First Other Weeks: ' + str(AvgOther))
print(Diff)
