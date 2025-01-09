from game_builder import GameBuilder

print("Welcome to Pong")
player_1 = "w" #input("enter player 1 name: ")
player_2 = "w"#input("enter player 2 name: ")
max_score = 10 #int(input("enter winning score: "))

game = GameBuilder(player_1, player_2, max_score)

game.build()
game.play()
game.exitonclick()