import csv

def not_colored_state(states):
	ret_state = ''
	min_colors = 5
	for state in states:
		if states[state]['color'] == 'blank' and len(states[state]['possible_colors']) < min_colors:
			ret_state = state
			min_colors = len(states[state]['possible_colors'])

	if ret_state == '':
		return None

	return ret_state

def can_paint_state(states, state, color):
	for neighboor in states[state]['neighboors']:
		if states[neighboor]['color'] == color:
			return False

		if color in states[neighboor]['possible_colors']:
			if len(states[neighboor]['possible_colors']) == 1:
				return False

	return True

def add_possible_color(states, neighboors, color):
	for neighboor in neighboors:
		possible_colors = states[neighboor]['possible_colors']
		if color not in possible_colors:
			possible_colors.append(color)

def remove_possible_color(states, neighboors, color):
	for neighboor in neighboors:
		possible_colors = states[neighboor]['possible_colors']
		if color in possible_colors:
			possible_colors.remove(color)

def color_map(states, state):
	if state is None:
		return True

	for color in ['red', 'blue', 'green', 'yellow']:
		if can_paint_state(states, state, color):
			states[state]['color'] = color
			remove_possible_color(states, states[state]['neighboors'], color)
			if color_map(states, not_colored_state(states)):
				return True

			add_possible_color(states, states[state]['neighboors'], color)

	states[state]['color'] = 'blank'
	return False

def main():
	states = {}
	with open('input/usa.in', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			states[row[0]] = {'neighboors': row[1:], 'color': 'blank', 'possible_colors': ['red', 'blue', 'green', 'yellow']}

	color_map(states, not_colored_state(states))
	for state in states:
		print(state, states[state]['color'])

if __name__ == '__main__':
	main()
