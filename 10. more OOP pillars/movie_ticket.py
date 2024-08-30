class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self.__show_list.append(show)
        
        # Initialize seats for the show as a 2D list with all seats free
        self.__seats[show_id] = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print(f"Error: Show ID {show_id} not found.")
            return
        
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Error: Seat at row {row + 1}, col {col + 1} is invalid.")
            elif self.__seats[show_id][row][col] == 'Free':
                self.__seats[show_id][row][col] = 'Booked'
            else:
                print(f"Error: Seat at row {row + 1}, col {col + 1} is already booked.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows are currently running.")
        else:
            print(f"Shows running in Hall {self.__hall_no}:")
            for show in self.__show_list:
                show_id, movie_name, time = show
                print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f"Error: Show ID {show_id} not found.")
            return

        print(f"Available seats for show {show_id}:")
        available_seats = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == 'Free':
                    available_seats.append((row, col))

        if not available_seats:
            print("No available seats.")
        else:
            for row, col in available_seats:
                print(f"Row {row + 1}, Col {col + 1}")

    def __repr__(self):
        return f"Hall(hall_no={self.__hall_no}, rows={self.__rows}, cols={self.__cols}, shows={len(self.__show_list)})"

class Counter:
    @staticmethod
    def view_all_shows():
        for hall in Star_Cinema.get_hall_list():
            hall.view_show_list()

    @staticmethod
    def view_available_seats(hall_no, show_id):
        for hall in Star_Cinema.get_hall_list():
            if hall._Hall__hall_no == hall_no:
                hall.view_available_seats(show_id)
                return
        print(f"Error: Hall {hall_no} not found.")

    @staticmethod
    def book_tickets(hall_no, show_id, seat_list):
        for hall in Star_Cinema.get_hall_list():
            if hall._Hall__hall_no == hall_no:
                hall.book_seats(show_id, seat_list)
                return
        print(f"Error: Hall {hall_no} not found.")

# Creating Hall objects
hall1 = Hall(4, 4, 1)
hall2 = Hall(5, 5, 2)

# Adding shows to Hall 1
hall1.entry_show("S1", "Movie A", "12:00 PM")
hall1.entry_show("S2", "Movie B", "03:00 PM")

# Adding a show to Hall 2
hall2.entry_show("S3", "Movie C", "06:00 PM")

# Counter viewing all shows
print("Viewing all shows:")
Counter.view_all_shows()
print()

# Counter viewing available seats for a show
print("Viewing available seats for Hall 1, Show S1:")
Counter.view_available_seats(1, "S1")
print()

# Counter booking tickets for a show
print("Booking seats for Hall 1, Show S1:")
Counter.book_tickets(1, "S1", [(0, 0), (1, 1), (2, 2)])
print()

# Attempting to book a seat that is already booked
print("Attempting to book a seat that is already booked:")
Counter.book_tickets(1, "S1", [(0, 0)])
print()

# Attempting to book an invalid seat
print("Attempting to book an invalid seat:")
Counter.book_tickets(1, "S1", [(10, 0)])
print()

# Viewing available seats after booking
print("Viewing available seats for Hall 1, Show S1 after booking:")
Counter.view_available_seats(1, "S1")
print()

# Printing the hall_list to verify the insertion, shows, and seat bookings
print("Final hall list with shows and seat bookings:")
for hall in Star_Cinema.get_hall_list():
    print(hall)
    print(f"Show List: {hall._Hall__show_list}")
    for show_id, seats in hall._Hall__seats.items():
        print(f"Seats for show {show_id}:")
        for row in seats:
            print(' '.join(row))
    print()
