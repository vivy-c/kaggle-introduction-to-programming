# run : python3 /Users/vivycahyani/Desktop/Belajar/kaggle-certification/kaggle-introduction-to-programming/4-lists.py

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
# The list has ten entries
print(len(flowers_list))

# The list has ten entries
print(len(flowers_list))

print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])


print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

flowers_list.remove("globe thistle")
print(flowers_list)

flowers_list.append("snapdragon")
print(flowers_list)

hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])

print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))

print("Total books sold in one week:", sum(hardcover_sales))

print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)