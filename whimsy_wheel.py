import random
import time

fortunes = [
    "🌸 Today brings a little magic.",
    "🍀 Luck is quietly on your side.",
    "🌙 Trust your intuition today.",
    "🦊 Adventure is closer than you think.",
    "☕ A cozy moment is waiting for you.",
    "🌈 Good things are coming your way."
]

colors = [
    "💜 Lavender",
    "💙 Sky Blue",
    "💚 Sage Green",
    "🩷 Cherry Blossom Pink",
    "💛 Golden Yellow",
    "🤍 Moon White"
]

animals = [
    "🦊 Fox",
    "🐈 Cat",
    "🦉 Owl",
    "🦋 Butterfly",
    "🐇 Rabbit",
    "🐎 Horse"
]

drinks = [
    "☕ Hot Chocolate",
    "🍵 Matcha Latte",
    "🧋 Bubble Tea",
    "🥛 Strawberry Milk",
    "🍋 Lemonade",
    "🧃 Apple Juice"
]

flowers = [
    "🌹 Rose",
    "🌸 Cherry Blossom",
    "🌼 Daisy",
    "🌻 Sunflower",
    "🌷 Tulip",
    "🌺 Hibiscus"
]

desserts = [
    "🍰 Cheesecake",
    "🍪 Chocolate Chip Cookie",
    "🧁 Cupcake",
    "🍫 Brownie",
    "🍩 Donut",
    "🍦 Ice Cream"
]

book_moods = [
    "📖 Fantasy Adventure",
    "💕 Romance",
    "🕵️ Mystery",
    "🚀 Sci-Fi",
    "🌿 Cozy Fiction",
    "👻 Thriller"
]


def spin_wheel():

    print("\n🎡 Spinning", end="")

    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print("\n")

    print("✨" * 20)
    print("🌸 YOUR MAGICAL RESULTS 🌸")
    print("✨" * 20)

    print("🍀 Lucky Color   :", random.choice(colors))
    print("🔢 Lucky Number  :", random.randint(1, 99))
    print("🦊 Lucky Animal  :", random.choice(animals))
    print("☕ Lucky Drink   :", random.choice(drinks))
    print("🌼 Lucky Flower  :", random.choice(flowers))
    print("🍰 Lucky Dessert :", random.choice(desserts))
    print("📚 Book Mood     :", random.choice(book_moods))
    print("🌙 Fortune       :", random.choice(fortunes))

    print("✨" * 20)


print("✨" * 20)
print("      🌸 WHIMSY WHEEL 🌸")
print("✨" * 20)

print("\nWelcome, traveler!")
print("Spin the magical wheel to discover today's whimsy.\n")

while True:

    input("🎡 Press ENTER to spin the wheel...")

    spin_wheel()

    again = input("\nWould you like to spin again? (yes/no): ").lower()

    if again != "yes":
        print("\n🌙 Thank you for visiting Whimsy Wheel!")
        print("✨ May your day be filled with a little magic. ✨")
        break