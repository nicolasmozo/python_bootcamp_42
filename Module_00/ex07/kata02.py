import datetime

kata = (2019, 9, 25, 3, 30)
date = datetime.datetime(year=kata[0],day=kata[2],month=kata[1],hour=kata[3],minute=kata[4])
print('{:%m/%d/%Y %H:%M}'.format(date))
#print(f'0{kata[1]}/{kata[2]}/{kata[0]} 0{kata[3]}:{kata[4]}')