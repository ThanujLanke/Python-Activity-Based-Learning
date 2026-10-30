#  c-1 Progressive Electricity Billing
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 3.0
elif units <= 300:
    bill = (100 * 3.0) + ((units - 100) * 5.0)
else:
    bill = (100 * 3.0) + (200 * 5.0) + ((units - 300) * 8.0)

print("Total Electricity Bill: Rs.", bill)
## flow diagram 
``` mermaid

               START
            |
            v
     Input units consumed
            |
            v
       Is units <= 100?
         /        \
       YES         NO
        |           |
        v           v
  bill = units*3  Is units <= 300?
                    /       \
                  YES        NO
                   |          |
                   v          v
          bill = 300 +    bill = 300 +
          (units-100)*5   1000 +
                          (units-300)*8
                   |          |
                   v          v
             Print Total Electricity Bill
                       |
                       v
                      STOP
```
