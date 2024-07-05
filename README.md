# RPi_LED
The lib was created for setting and operating Digital-Pipe in Raspberry Pie 4B(or other higher versions)
you could choose your own pinner to operate your digital pipe,or using the default set pinners.

# Here is the defualt set number of a digital pipe on Respberry Pi:
                    g
                ########        BCM
              #          #      a: 4   
            a #          # f    b: 17
              #     b    #      c: 27
                ########        d: 22
              #          #      e: 5
            c #          # e    f: 6
              #     d    #      g: 13
                ########        vcc: 12   
                

### 1.if using Common Anode Digital Pipe : vcc is the volt_port
### 2.else using Common Cathode Digital Pipe : vcc is the ground_port

# How to change default set pinner?
## here is an example:
digital_pipe = CADT_PIPE(pin_vcc=18)









