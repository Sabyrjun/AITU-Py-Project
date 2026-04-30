"""
def analyze_number(n):
    even_odd = "Even" if n % 2 == 0 else "Odd"
    if n > 0:
        pos_neg = "Positive"
    elif n < 0:
        pos_neg = "Negative"
    else:
        pos_neg = "Zero"
    return (even_odd, pos_neg, n ** 2)
"""
#2
"""
def find_max(*numbers):
    return max(numbers) if numbers else None
"""
#3
"""
nums = [5, 12, 7, 18, 20]
result = list(map(lambda x: x**2, filter(lambda x: x > 10, nums)))
"""
#4
"""
students = [("Ali", 85), ("Dina", 92), ("Mira", 78)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
"""
#5
"""
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def is_recommended(self):
        return self.rating >= 8

    def display_info(self):
        print(f"Title: {self.title}, Rating: {self.rating}")
"""
#6
"""
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def restock(self, amount):
        self.quantity += amount

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough quantity available")
"""
#7
"""
class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration for song in self.songs)

    def longest_song(self):
        if not self.songs:
            return None
        return max(self.songs, key=lambda song: song.duration)

    def show_playlist(self):
        for song in self.songs:
            print(f"{song.title} ({song.duration} min)")
"""






