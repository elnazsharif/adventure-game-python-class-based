
from Room import Room
from TextUI import TextUI


"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game. Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game. It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage.
"""


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_rooms()
        self.current_room = self.gate
        self.textUI = TextUI()

    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        """some rooms with their descriptions are added"""
        self.gate = Room("You are in front of city gate ")
        self.bar = Room("You are in bar ")
        self.prison = Room(
            "You are in prison . There are some friends in the downstairs to need be rescued.")
        self.prisonDownstairs = Room(
            "You are in the scariest place in the world, downstairs of our city prison")
        self.hospital = Room(
            "You are in hospital. Safe place. ")
        self.restaurant = Room(
            " You are in restaurant. ")
        self.Bazzar = Room("You are in Bazzar.")
        self.school = Room(
            "You are in school. For going forward you should know the password.")
        self.bank = Room(
            "You are in bank. I see you found the money. Now you can run away from road.")
        self.road = Room("You are in road. Well done")

        self.gate.set_exit("west", self.bar)
        self.bar.set_exit("east", self.gate)
        self.bar.set_exit("south", self.prison)
        self.prison.set_exit("north", self.bar)
        self.prison.set_exit("west", self.hospital)
        self.prison.set_exit("downstairs", self.prisonDownstairs)
        self.prisonDownstairs.set_exit("upstairs", self.prison)
        self.prisonDownstairs.set_exit("west", self.restaurant)
        self.hospital.set_exit("east", self.prison)
        self.hospital.set_exit("south", self.restaurant)
        self.hospital.set_exit("west", self.school)
        self.restaurant.set_exit("north", self.hospital)
        self.restaurant.set_exit("south", self.Bazzar)
        self.restaurant.set_exit("west", self.school)
        self.Bazzar.set_exit("north", self.restaurant)
        self.school.set_exit("north", self.hospital)
        self.school.set_exit("east", self.restaurant)
        self.school.set_exit("south", self.bank)
        self.bank.set_exit("north", self.school)
        self.bank.set_exit("south", self.road)
        self.road.set_exit("north", self.bank)
        """The rooms and their routes are intriduced to system. if the second word of command equalls to 
        north, west, east, south, downstairs and upstais, the next room from these directions is written next to the directions"""

    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        finished = False
        while not finished:  #  while (finished == False):
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("Thank you for playing!")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return:
        """
        self.textUI.print_to_textUI(
            "Welcome player, you came to city to rub the city bank. ")
        self.textUI.print_to_textUI(
            "For that, you should go to bank and grab money and run away from road.")
        self.textUI.print_to_textUI(
            "Do not forget, there are some of your friends who need your help. You can find them in downstair of prison. help them. You need them too.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(
            f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit']

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.do_go_command(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Don't know what you mean.")

        return want_to_quit

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI(
            "Welcome player, you came to city to rub the city bank.")
        self.textUI.print_to_textUI(
            "For that, you should go to bank and grab money and run away from road.")
        self.textUI.print_to_textUI(
            "Do not forget, there are some of your friends who need your help. You can find them in downstair of prison. help them. You need them too.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(
            f'Your command words are: {self.show_command_words()}.')

    def win(self):
        """print some sentences when player win"""
        print("Well done. Now, you are in road.... " +
              "run away immidiately")
        print(" You won.")

    """the list of b is global, because it uses in some methods"""
    global b
    b = []

    def adding(self):
        """
        this method adds some arrays from  list of a to  list of b.
        the collection variable is true, becuase when it is true the while loop excute, when it is false, the loop finishes
        when player adds some items to list the variable of savepeople will be true
        """
        self.collection = True
        self.savepeople = False

        self.a = ["Tom", "Jery",
                  "Pat", "Mat"]
        print('Your friens were surrounded by  police. save them.')
        while self.collection:
            for item in self.a:
                print(f'You can rescue {self.a}. Do you help them, yes or no?')
                """the player enter yes or no, each word has its own condition"""
                pickup = input()
                if pickup == "yes":
                    """the list of b can not have more than 3 items"""
                    if len(b) < 3:
                        b.append(item)
                        self.savepeople = True
                        print(
                            f'you have saved {b}. Good Job Player, you are life saver. Look he/she whisper a name. money')
                        """when player picks up item, one password reveals, money"""
                    else:
                        print(
                            'Sorry your car is full. You cannot ride people more than this. Go forward.Exits: [west, upstairs] ')
                        self.textUI.print_to_textUI(
                            f'Your command words are: {self.show_command_words()}')
                        self.collection = False
                        self.savepeople = True
                        """the variable of collection become false because exit the loop and variable of savepeople become true that shows player pick up all the items"""
                        break
                    pass

                else:
                    if self.savepeople == True:
                        self.collection == False
                        """the variable of collection become false because exit the loop and variable of savepeople become true that shows player pick up some the items"""
                        print(
                            'You had more space, but okay, Continue! Go forward.Exits: [west, upstairs]')
                        self.textUI.print_to_textUI(
                            f'Your command words are: {self.show_command_words()}')
                        """use command words becuase player can undrestand should continue"""
                        return self.collection

                    if self.savepeople == False:
                        self.collection = False
                        """both variables are false, first one shows player do not pick up, second exit the loop"""
                        print(
                            f'Nika, you made a mistake. Unity is the success key of Iran\'s road. You should have saved them.Exits: [west, upstairs]')
                        self.textUI.print_to_textUI(
                            f'Your command words are: {self.show_command_words()}')

                    break

    def releasepeople(self):
        """In this method player remove one of the item from the list of b, the asks do you want to remove it or not and the yes or no answer have their own conditons"""
        print('Tom has loved a girl in the city. Leave him to the girl.Okay? yes or no')
        self.release = input()
        if self.release == 'yes':
            if 'Tom' in b:
                """at first with this codition look at the list,if the item exist execute these instructions """
                b.remove('Tom')
                print(
                    f'Good job player. You can continue you way with your new friends{b}. Go forward, Exits: [west, south, east]')
                self.textUI.print_to_textUI(
                    f'Your command words are: {self.show_command_words()}')

            else:
                """if the player enters yes, but the item does not exist in list"""
                print(
                    'Where is he? His girl is worried. Pick up him from downstairs of prison. Go forward, Exits: [west, south, east]')
                self.textUI.print_to_textUI(
                    f'Your command words are: {self.show_command_words()}')

        else:
            """if the player enters no"""
            print(
                ' It would be better if he did not come with you and stayed with his girl,but okay, continue. Go forward, Exits: [west, south, east]')
            self.textUI.print_to_textUI(
                f'Your command words are: {self.show_command_words()}')

    def password(self):
        """one room is locked and needs password, when player picks up items, the password reveals"""
        print('your friends frequently whisper a name. That is our bank password. Could you guess the password? yes or no')
        roomopen = False
        """the variable of room open shows a status of room"""
        while True:
            knowpassword = input('')
            """game asks player that do you know password and goes to variable of knowpassword, the answer is yes or no , and depends on the answer some instructions execute"""
            if knowpassword == 'yes':
                if roomopen:
                    """this condition is that for a time that room had become open and again player arrived to this room"""
                    print('The school doors are already opened')
                    break
                else:
                    while True:
                        print('Enter the password')
                        """the player enter the password and it goes to password variable, if it is right the  variables of has key and roomopen will be true """
                        password = input('')
                        if password == "money":
                            roomopen = True
                            self.haskey = True
                            print(
                                'You can open school doors, where do you go? Exits: [east, south, north] ')
                            self.textUI.print_to_textUI(
                                f'Your command words are: {self.show_command_words()}')

                            break
                        if not password:
                            """if password wrong, the game asks again and again the password"""
                            break
                    break
            elif knowpassword == "no":
                self.haskey = False
                """if player enter that do not know the password,no, the roomopen variable remain false and has key is false too"""
                print(
                    'You cannot go forward, the school doors are closed. Go back and find password! where do you go? Exits: [east, north] ')
                self.textUI.print_to_textUI(
                    f'Your command words are: {self.show_command_words()}')
                break

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Go where?")
            return

        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_to_textUI(
                "You cannot go there.  police are waiting with guns in these places. Death is certain!")
            self.textUI.print_to_textUI(
                f'Your command words are: {self.show_command_words()}')
            """when the player go to a room that is closed, stops, but putting command words here allows the player to continue"""
        else:

            self.current_room = next_room
            self.textUI.print_to_textUI(
                self.current_room.get_long_description())

        if self.current_room == self.prisonDownstairs:
            self.adding()
            """when a player reaches to prison downstairs runs adding method and wants to pickup items"""
        if self.current_room == self.school:
            self.password()
            """when a player reaches to school  runs password method and wants to enter password and unlocks the door """
        if self.current_room == self.hospital:
            """when a player reaches to hospital  runs releasepeople method and wants to remove some items from list"""
            self.releasepeople()
        if self.current_room == self.road and self.haskey == True:
            """when a player reaches to road square, if the haskey password is true, it runs win method, otherwise it runs as a normal room"""
            self.win()


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
