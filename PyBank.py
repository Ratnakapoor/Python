# Declare a csv file and Read the csv file 

import os
import csv
    
csv_path = os.path.join("budget_data.csv")

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",") 
    
    csv_header = next(csv_reader)
    sorted1 = sorted(csv_reader, key=lambda row: int(row[1]))
    greatest_loss = sorted1[0]
    greatest_profit = sorted1[len(sorted1)-1]
    
    data = [row for row in sorted1]  
      
    for row in data:
        total_mth_cnt = sum(1 for row in data ) 
        total_pl_sum += int(row[1]) 
              
    for row in data: 
              
        if int(row[1]) >= 1:
            profit += int(row[1])
        else:
            loss += int(row[1])
        
    average_change =  ( total_pl_sum / total_mth_cnt ) 
    
    print(f"Total Months : {str(total_mth_cnt)}")
    print(f"Total : $ {str(total_pl_sum)}")
    print(f"Average Change: $ {str(average_change)}")
    print(f"Greatest Increase in Profit : $ {str(greatest_profit)}")
    print(f"Greatest Decrease in Profit : $ {str(greatest_loss)}")                    
    
    line1 = "Total Months : " + str(total_mth_cnt) + '\n' 
    line2 = "Total :  $" +  str(total_pl_sum) + '\n'
    line3 = "Average Change: $ " + str(average_change) + '\n'
    line4 = "Greatest Increase in Profit : $ " + str(greatest_profit) + '\n'
    line5 = "Greatest Decrease in Profit : $ " + str(greatest_loss) + '\n'
    
       
file = open("Profit_Loss.txt", "w")
file.write(line1)
file.write(line2)
file.write(line3)
file.write(line4)
file.write(line5)
file.close() 
    
