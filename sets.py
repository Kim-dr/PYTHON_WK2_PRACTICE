set1 = set(map(int, input("Enter integers for Set 1 (separated by spaces): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (separated by spaces): ").split()))

combine_elements= set1 & set2
print("Common elements in both sets:",combine_elements)