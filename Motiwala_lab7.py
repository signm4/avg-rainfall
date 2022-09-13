#Name: Muhammed Motiwala
#Program: lab7
#Status: Complete

def main():
    rainfall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    monthNames = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        
    for i in range(len(monthNames)):
        rainfall[i] = float(input("enter the amount of rainfall for " + monthNames[i] + " :"))

    total = 0
    for value in rainfall:
        total += value
    print("Total rainfall: ", total)

    average = total / len(rainfall)
    print("Average rainfall: ", average)

    print('the minimum rainfall is', str(monthNames[rainfall.index(min(rainfall))]))
    print('the maximum rainfall is', str(monthNames[rainfall.index(max(rainfall))]))    
main()
