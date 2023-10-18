from random import choice

game_inventory = ["Stone", "Scissor", "Paper"]
your_choice = input('Choose "Stone", "Scissor" or "Paper": ')
your_choice = your_choice.capitalize()
print('\n')

games_choice = choice(game_inventory)

print(f'Your choice "{your_choice}" vs Computer`s choice "{games_choice}"')

match your_choice:
	case 'Stone':
		match games_choice:
			case 'Stone':
				print('Draw')
			case 'Scissor':
				print('Victory')
			case 'Paper':
				print('Defeat')
	case 'Scissor':
		match games_choice:
			case 'Stone':
				print('Defeat')
			case 'Scissor':
				print('Draw')
			case 'Paper':
				print('Victory')
	case 'Paper':
		match games_choice:
			case 'Stone':
				print('Victory')
			case 'Scissor':
				print('Defeat')
			case 'Paper':
				print('Draw')