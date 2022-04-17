from datetime import datetime
import codecs
import numpy as np


def load_file(file_path):

	error_message = "FILE NOT FOUND OR DOES NOT EXIST!\n\n(or other bad things happened, send help!)"

	data = [ ["Name not found!", "Date not found!"], [] ]

	try:
		with codecs.open(file_path, "r", "UTF-8") as file:
			lines = file.readlines()

		for line in lines:
			if "Listener:" in line:
				data[0][0] = line[+12:-1]
            
			if "Session Started:" in line:
				data[0][1] = line[+19:-1]

			if (line[0] == '[') and "(combat) <color=" in line:
				if get_stats(line) is not None:
					data[1].append(get_stats(line))

	except:
		print(f"\n\n{error_message}\n\n")
		return error_message

	return(data)
	
def get_stats(line):

	def get_value(line):
		string = line.partition("<b>")
		string = string[2].partition("</b>")
		string = string[0]
		string = int(string.split()[0])
		return string

	def get_date(line):
		dates = line.split()
		dates = f"{dates[1]} {dates[2]}"
		return dates

	def get_name(line):
		name = line.partition("<color=0xffffffff>")
		name = name[2].partition("</b><font size=10>")
		name = name[0]
		name = name.split()[0]
		return name

	def get_weapon(l):
		return "DOOMSDAY"							# placesholder for future features

	string = line.split()

	# Mode Values:
	# 0 do damage (0xff00ffff), 1 get damage (0xffcc0000), 2 do remote repair (0xffccff66), 3 get remote repair (0xffccff66),
	# 4 do remote shield, 5 get remote shield, 6 do remote energy (0xffccff66), 7 get remote energy (0xffccff66), 
	# 8 get energy nosferatu (0xff7fffff), 9 give energy nosferatu (0xffe57f7f), 10 do neutralyzing (0xff7fffff), 11 get neutralyzed (0xffe57f7f)
	# 12 missed, 13 miss, 14 undefined

	if "0xff00ffff" in string[5]:																	# first value of the list is the mode which is defined above
		data_list = [0, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffcc0000" in string[5]:
		data_list = [1, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffccff66" in string[5] and "repaired to" in line:
		data_list = [2, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffccff66" in string[5] and "repaired by" in line:
		data_list = [3, get_date(line), get_value(line), "NONE", get_weapon(line), line]
	elif "0xffccff66" in string[5] and "boosted to" in line:
		data_list = [4, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffccff66" in string[5] and "boosted by" in line:
		data_list = [5, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffccff66" in string[5] and "transmitted to" in line:
		data_list = [6, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffccff66" in string[5] and "transmitted by" in line:
		data_list = [7, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xff7fffff" in string[5] and "drained from" in line:
		data_list = [8, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffe57f7f" in string[5] and "drained to" in line:
		data_list = [9, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xff7fffff" in string[5] and "energy neutralized" in line:
		data_list = [10, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "0xffe57f7f" in string[5] and "energy neutralized" in line:
		data_list = [11, get_date(line), get_value(line), get_name(line), get_weapon(line), line]
	elif "misses you completely" in line:
		data_list = [13, get_date(line), 0, "miss", "miss"]
	else:
		return None
	return data_list

def sum_a_stat(mode, data):
	sum = 0
	for i in data[1]:
		if i[0] == mode:
			sum += i[2]
	return sum

def list_a_stat(mode, data):
	stat_list = [ ]
	stat_list.append([get_start_and_end(data)[0], 0])									# dirty hack to put in starting time, so timeline is streamlined.
	for i in data[1]:
		if i[0] == mode:
			stat_list.append([i[1], i[2]])
	return stat_list

def get_start_and_end(data):
	start_date = data[1][0][1]
	end_date   = data[1] [ (len(data[1]) -1) ] [1]
	dates = [start_date, end_date]
	return dates

def to_seconds(data):
	start_date = datetime.strptime(data[0][0], "%Y.%m.%d %H:%M:%S")
	for i in data:
		i[0] = datetime.strptime(i[0], "%Y.%m.%d %H:%M:%S")
		i[0] = (i[0] - start_date)
		i[0] = i[0].seconds
	return data

def from_list_to_timelinedata(mode, data):
	stat_list = list_a_stat(mode, data)
	stat_list = to_seconds(stat_list)
	dates = get_start_and_end(data)

	count_dictonary = {}

	length = (datetime.strptime(dates[1], "%Y.%m.%d %H:%M:%S") - datetime.strptime(dates[0], "%Y.%m.%d %H:%M:%S")).seconds

	i = 0
	while i <= length:
		count_dictonary[i] = 0
		i += 1

	for i in stat_list:
		count_dictonary[i[0]] += i[1]

	return count_dictonary

def moving_average(data):
	pass

def get_plot_data(mode, data):
	plot_data = list(from_list_to_timelinedata(mode, data).items())
	plot_data_x = [i[0] for i in plot_data]
	plot_data_y = [i[1] for i in plot_data]
	np_plot_data_x = np.array(plot_data_x)
	np_plot_data_y = np.array(plot_data_y)
	moving = 6
	ma_np_plot_data_y = np.convolve(np_plot_data_y, np.ones(moving), 'valid') / moving
	ma_np_plot_data_y = np.insert(ma_np_plot_data_y, 0, 0)
	i=2
	while i < moving:
		ma_np_plot_data_y = np.insert(ma_np_plot_data_y, 0, 0)
		i += 1
	return [np_plot_data_x, ma_np_plot_data_y]
