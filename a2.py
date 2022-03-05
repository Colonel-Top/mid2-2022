run_again = "y"
while(run_again == "y"):
    day = input("Day: ")
    while(day != "m" and day != "t"):
        day = input("Day")
    payload = int(input("payload: "))
    while (payload < 25 or payload > 1000):
        payload = int(input("payload"))
    a_car = int(input("number of v at A: "))
    b_car = a_car * 1.1
    c_car = a_car * 0.9

    J_ROAD_A = 1.5
    J_ROAD_B = 0.9
    J_ROAD_C = 1.4
    if day == "t":
        J_ROAD_A = 1.3
        J_ROAD_B = 0.8
        J_ROAD_C = 1.2

    #Calculate Payload
    P = 1+(payload*0.002)
    t_a = J_ROAD_A * P * a_car
    t_b = J_ROAD_B * P * b_car
    t_c = J_ROAD_C * P * c_car

    print("Drive Time for road A:",t_a,"minutes")
    print("Drive Time for road B:",t_b,"minutes")
    print("Drive Time for road C:",t_c,"minutes")

    t_a /= 60
    t_b /= 60
    t_c /= 60
    #avg_speed = ((200/t_a) + (300/t_b) + (150/t_c))/3
    avg_speed = 650/(t_a+t_b+t_c)
    print("Average speed:",avg_speed,"km/hr")
    run_again = input("Do you want to run again ? (Enter y for yes")

