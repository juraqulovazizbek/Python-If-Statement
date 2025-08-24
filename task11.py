oy = int(input("Oy raqami: "))

if oy in (12, 1, 2):
    print("Qish")

if oy in (3, 4, 5):
    print("Bahor")

if oy in (6, 7, 8):
    print("Yoz")

if oy in (9, 10, 11):
    print("Kuz")

if oy < 1 or oy > 12:
    print("Bunday oy yo'q")
