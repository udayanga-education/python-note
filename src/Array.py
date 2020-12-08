# Step 1 Print
arr = [10, 20, 30, 40, 50]

print (arr[0])  # First
print (arr[1])  # Second
print (arr[2])  # Third
print (arr[-1])  # Last
print (arr[-2])  # Second from last

print ("====================================================")

# Step 2 Add element
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print (brands)

count = len(brands)
print (count)

brands.append("Intel")
print (brands)

# Step 3 Delete element
print ("====================================================")
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print (brands)
del brands[1]
print (brands)

brands.remove("Coke")
print (brands)

brands.pop(2)
print (brands)

# Step 4 Modify element
print ("====================================================")
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print (brands)
brands[1] = "Udayanga"
print (brands)

brands[-1] = "Senanayake"
print (brands)

# Step 5 Concatenating
print ("====================================================")
concat = [1, 2, 3]
print (concat)

concat + [4, 5, 6]
print (concat)

concat = concat + [4, 5, 6]
print concat

# Step 6 Repeating item
print ("====================================================")
repeat = ["a"]
print repeat
repeat = repeat * 5
print repeat

# Step 7 Slicing array
print ("====================================================")
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print brands

print brands[1:4]
print brands[:3]
print brands[-3:]
print brands[-3:-1]

# Step 7 multi dimension array
print ("====================================================")
mltd = [[1, 2], [3, 4], [5, 6], [7, 8]]

print mltd
print mltd[0]
print mltd[3]
print mltd[2][1]
print mltd[3][0]

