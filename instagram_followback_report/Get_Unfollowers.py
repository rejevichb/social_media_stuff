import argparse
import json

def who_doesnt_follow_back(flwng: dict, flwrs: dict):
	return set(flwng) - set(flwrs)


def get_dict(file: str):
	with open(file, 'r') as f:
		master_dict = json.load(f)
	return master_dict


if __name__ == '__main__':
	p = argparse.ArgumentParser()
	p.add_argument('path', type=str, help='the path to data file')
	args = p.parse_args()
	path = args.path
	#'/Users/brendanrejevich/Documents/InstagramData/breandan_mcelroy_20200402_part_1/connections.json'

	seperator = "---- ---- ---- ---- ---- ---- ----"

	master_dict = get_dict(path)

	print(master_dict.keys())

	f = open("InstagramFollowerAnalysis.txt", "w+")
	f.write("Instagram analysis courtesy of Brendan \n\n")
	close_friends = master_dict['close_friends']
	f.write("Here are your {} besties: \n".format(len(close_friends)))
	for friend in close_friends:
		f.write(friend + '\n')
	f.write(seperator + '\n\n\n')

	no_followbacks = who_doesnt_follow_back(master_dict['following'], master_dict['followers'])
	f.write("There are {} users who do not follow you back \n:".format(len(no_followbacks)))
	f.write(seperator)
	for i in no_followbacks:
		f.write(i + "\n")
	for i in range(2): f.write(seperator + '\n')
	f.write('\n')
	f.write("END")
	f.close()





