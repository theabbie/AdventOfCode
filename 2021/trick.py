xrange = (94, 151)
yrange = (-156, -103)

accepted = set()
maxInit = (float('-inf'), float('-inf'))
maxY = float('-inf')

xmaxvel = xrange[1] + 10
yminvel = yrange[0] - 5

vels = [(xvel, yvel) for xvel in range(xmaxvel) for yvel in range(yminvel, 700)]

for vel in vels:
    xvel, yvel = vel
    ymax = 0
    x = 0
    y = 0
    while y >= yrange[0]:
        x += xvel
        y += yvel
        ymax = max(ymax, y)
        if x >= xrange[0] and x <= xrange[1] and y >= yrange[0] and y <= yrange[1]:
            accepted.add(vel)
            if vel[1] > maxInit[1]:
                maxInit = vel
                maxY = max(maxY, ymax)
            break
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1

print(maxY, len(accepted))