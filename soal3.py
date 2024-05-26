def rabbits_meet(pos1, vel1, pos2, vel2, jumps):
    for i in range(jumps):
        pos1 += vel1
        pos2 += vel2
        if pos1 == pos2:
            return "YES"
    return "NO"

pos_rabbit1 = int(input("Position rabbit 1: "))
vel_rabbit1 = int(input("Velocity rabbit 1: "))
pos_rabbit2 = int(input("Position rabbit 2: "))
vel_rabbit2 = int(input("Velocity rabbit 2: "))
jumps = int(input("jumps: "))

result = rabbits_meet(pos_rabbit1, vel_rabbit1, pos_rabbit2, vel_rabbit2, jumps)
print("Result:", result)
