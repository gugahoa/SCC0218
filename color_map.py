import csv

def not_colored_state(states):
	for state in states:
		if states[state]['color'] == 'blank':
			return state

	return None

def can_paint_state(states, state, color):
	for neighboor in states[state]['neighboors']:
		if states[neighboor]['color'] == color:
			return False

	return True

def color_map(states, state):
	if state is None:
		return True

	for color in ['red', 'blue', 'green', 'yellow']:
		if can_paint_state(states, state, color):
			states[state]['color'] = color
			if color_map(states, not_colored_state(states)):
				return True

	states[state]['color'] = 'blank'
	return False

def main():
	states = {}
	with open('input/usa.in', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			states[row[0]] = {'neighboors': row[1:], 'color': 'blank'}

	color_map(states, not_colored_state(states))
	for state in states:
		print(state, states[state]['color'])

if __name__ == '__main__':
	main()
