from collections import defaultdict
import csv
from collections import Counter
import os


months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
# months_2016 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
years = ["2011", "2012", "2013", "2014", "2015"]



# gped_by_airline = defaultdict(list)
# with open("alldata_12.csv", 'rb') as inputfile:
#     reader = csv.reader(inputfile)
#     next(reader, None)  # skip the header row
#     for YEAR,MONTH,DAY_OF_MONTH,DAY_OF_WEEK,UNIQUE_CARRIER,ORIGIN,DEST,ARR_DELAY_NEW,CANCELLED,CANCELLATION_CODE,CARRIER_DELAY,WEATHER_DELAY,NAS_DELAY,SECURITY_DELAY,LATE_AIRCRAFT_DELAY in reader:
#         if ARR_DELAY_NEW == '' and MONTH == "1":
#         	ARR_DELAY_NEW = 0
#         gped_by_airline[UNIQUE_CARRIER + "_" + YEAR].append([YEAR, CANCELLATION_CODE, ARR_DELAY_NEW])
# gped_by_year = defaultdict(list)
# gped_by_cancellation = defaultdict(list)
# for key, value in gped_by_airline.items():
#     totalDelay = 0
#     for i in range (len(value)):
#     	try: 
#     		if int(value[i][2] ) != 0:
#     			totalDelay = totalDelay + 1
#     	except ValueError:
#   			print("Error!")
#     totalCancellations = []
#     for i in range (len(value)):
#     	if value[i][1] != "":
#     		totalCancellations.append(value[i][1])
#     gped_by_cancellation[key].append(totalCancellations)
#     gped_by_year[key].append([totalDelay, len(value)])
# gped_by_year_cancellation = defaultdict(list)
# for key, value in gped_by_year.items():
# 	totalNumFlights = value[0][1]
# 	ontimeRatio = float(1 - float(float(value[0][0]) / float(totalNumFlights)))
# 	cancellationRatio = len(gped_by_cancellation[key][0])
# 	cancelledByA = 0
# 	cancelledByB = 0
# 	cancelledByC = 0
# 	cancelledByD = 0
# 	C = Counter(gped_by_cancellation[key][0])
# 	arrangedCancelFlights = [[k,]*v for k,v in C.items()]
# 	for i in range(len(arrangedCancelFlights)):
# 		if arrangedCancelFlights[i][0] == 'A':
# 			cancelledByA = cancelledByA + len(arrangedCancelFlights[i])
# 		if arrangedCancelFlights[i][0] == 'B':
# 			cancelledByB = cancelledByB + len(arrangedCancelFlights[i])
# 		if arrangedCancelFlights[i][0] == 'C':
# 			cancelledByC = cancelledByC + len(arrangedCancelFlights[i])
# 		if arrangedCancelFlights[i][0] == 'D':
# 			cancelledByD = cancelledByD + len(arrangedCancelFlights[i])	
# 	gped_by_year_cancellation[key].append([totalNumFlights, ontimeRatio, cancellationRatio, cancelledByA, cancelledByB, cancelledByC, cancelledByD])
# allAirlnes = []
# for key, value in gped_by_year_cancellation.items():
# 	if key.split("_")[0] not in allAirlnes:
# 		if (value[0][0] > 2):
# 			allAirlnes.append(key.split("_")[0])
# final_dict = []
# for i in range(len(allAirlnes)):
# 	single_airline_info = {"Carrier" : allAirlnes[i]}
# 	for key, value in gped_by_year_cancellation.items():
# 		if key.split("_")[0] == allAirlnes[i]:
# 			single_airline_info[key.split("_")[1] + "_total"] = value[0][0]
# 			single_airline_info[key.split("_")[1] + "_ontime"] = value[0][1]
# 			single_airline_info[key.split("_")[1] + "_cancel"] = value[0][2]
# 			single_airline_info[key.split("_")[1] + "_cancelA"] = value[0][3]
# 			single_airline_info[key.split("_")[1] + "_cancelB"] = value[0][4]
# 			single_airline_info[key.split("_")[1] + "_cancelC"] = value[0][5]
# 			single_airline_info[key.split("_")[1] + "_cancelD"] = value[0][6]
# 	final_dict.append(single_airline_info)

# # def ReadCSVasDict(csv_file):
# #     try:
# #         with open(csv_file) as csvfile:
# #             reader = csv.DictReader(csvfile)
# #             for row in reader:
# #                 print row['Row'], row['Name'], row['Country']
# #     except IOError as (errno, strerror):
# #             print("I/O error({0}): {1}".format(errno, strerror))    
# #     return

# def WriteDictToCSV(csv_file,csv_columns,dict_data):
#     try:
#         with open(csv_file, 'w') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#             writer.writeheader()
#             for data in dict_data:
#                 writer.writerow(data)
#     except IOError as (errno, strerror):
#             print("I/O error({0}): {1}".format(errno, strerror))    
#     return      
# maxIndex = max(enumerate(final_dict), key = lambda tup: len(tup[1]))      
# csv_columns = []

# for key, value in final_dict[maxIndex[0]].items():
# 	print(key)
# 	csv_columns.append(key)

# currentPath = os.getcwd()
# csv_file = "carrier_times_cancellations_12.csv"
# try:
# 	WriteDictToCSV(csv_file,csv_columns,final_dict)
# 	# ReadCSVasDict(csv_file)
# except :
#   	print("error")









for month in months:
	airline_cancellation_info = []
	with open("carrier_times_cancellations_" + month + ".csv", 'rb') as inputfile:
	    reader = csv.DictReader(inputfile)
	    airline_cancellation_info.append({"id":"Carrier", "value": ""})
	    for row in reader:
	    	if row["Carrier"] != '' :
				airline_cancellation_info.append({"id":"Carrier"+ "." +row["Carrier"], "value": ""})
				overallCancels = 0
				overallCancelsA = 0
				overallCancelsB = 0
				overallCancelsC = 0
				overallCancelsD = 0
				for year in years:
					cancelsA=0 
					cancelsB=0 
					cancelsC=0 
					cancelsD = 0
					if row[year + "_cancelA"] == '':
						cancelsA = 0
					else:
						cancelsA = int(row[year + "_cancelA"])
					if row[year + "_cancelB"] == '':
						cancelsB = 0
					else:
						cacelsB = int(row[year + "_cancelB"])
					if row[year + "_cancelC"] == '':
						cancelsC = 0
					else:
						cancelsC = int(row[year + "_cancelC"])
					if row[year + "_cancelD"] == '':
						cancelsD = 0
					else:
						cancelsD = int(row[year + "_cancelD"])
	    			overallCancelsA = overallCancelsA + cancelsA
	    			overallCancelsB = overallCancelsB + cancelsB
	    			overallCancelsC = overallCancelsC + cancelsC
	    			overallCancelsD = overallCancelsD + cancelsD
				# overallCancels = overallCancels + overallCancelsA + overallCancelsB + overallCancelsC + overallCancelsD
				# airline_cancellation_info.append({"id":"Carrier"+ "." +row["Carrier"], "value": overallCancels})
				airline_cancellation_info.append({"id": "Carrier"+ "." +row["Carrier"]+ "." +"cancelA", "value": overallCancelsA})
				airline_cancellation_info.append({"id": "Carrier"+ "." +row["Carrier"]+ "." +"cancelB", "value": overallCancelsB})        
				airline_cancellation_info.append({"id": "Carrier"+ "." +row["Carrier"]+ "." +"cancelC", "value": overallCancelsC})
				airline_cancellation_info.append({"id": "Carrier"+ "." +row["Carrier"]+ "." +"cancelD", "value": overallCancelsD})
	# print(airline_cancellation_info)


	def WriteDictToCSV(csv_file,csv_columns,dict_data):
	    try:
	        with open(csv_file, 'w') as csvfile:
	            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, lineterminator='\n')
	            writer.writeheader()
	            for data in dict_data:
	            	print(data)
	                writer.writerow(data)
	    except IOError as (errno, strerror):
	            print("I/O error({0}): {1}".format(errno, strerror))    
	    return      
	# maxIndex = max(enumerate(final_dict), key = lambda tup: len(tup[1]))      
	csv_columns = ["id", "value"]


	currentPath = os.getcwd()
	csv_file = "cancellationData_" + month+ ".csv"
	try:
		WriteDictToCSV(csv_file,csv_columns,airline_cancellation_info)
	except :
	  	print("Error!")














# with open('mycsvfile.csv', 'wb') as f:  
#     w = csv.DictWriter(f, gped_by_airline.keys())
#     w.writeheader()
#     w.writerow(gped_by_airline)


# Code,Description
# "A","Carrier"
# "B","Weather"
# "C","National Air System"
# "D","Security"








# fout=open("out.csv","a")
# # first file:
# for line in open("data/2011_12.csv"):
#     fout.write(line)
# # now the rest:    
# for num in years:
#         # print(year)
#     # if year == "2016":
#     for num1 in months:
#         f = open("data/"+ num + "_" + num1 + ".csv")
#         f.next() # skip the header
#         for line in f:
#              fout.write(line)
#         f.close() # not really needed
#     # else :
#     #     for num1 in range(0, 11):
#     #         count1 =  11 - num1
#     #         print(months[count1])
# # f = open("data/2016_08.csv")
# # f.next() # skip the header
# # for line in f:
# #      fout.write(line)
# # f.close() # not really needed        
# fout.close()