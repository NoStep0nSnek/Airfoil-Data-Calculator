# see: https://aviation.stackexchange.com/questions/24180/what-is-the-maximum-theoretical-lift-of-a-plane-as-a-function-of-engine-power-an
# see: https://aviation.stackexchange.com/questions/21390/what-is-the-most-simple-plane-lift-equation-that-gives-realistic-solutions/21432#21432

'''
Nomenclature:
cL
 lift coefficient (normally between 0 and 1.5)
π
 3.14159…

AR
 aspect ratio of the wing (ratio of span to mean chord)
ϵ
 the wing's Oswald factor (use 0.8 when in doubt)
cD0
 zero-lift drag coefficient (use 0.02 when in doubt)
'''
import math

def calc_lift_force(Lift_Coefficient, Density, Velocity, Surface_Area):
    L = Lift_Coefficient * Density * (((Velocity**2)*2) / 2) * Surface_Area
    return L
def calc_drag_force(zero_lift_DC, Lift_Coefficient, Aspect_Ratio, Oswald_Factor, Density, Velocity, Surface_Area):
    D = (zero_lift_DC + ((Lift_Coefficient**2)/math.pi*Aspect_Ratio*Oswald_Factor)*Density*(((Velocity**2)*2) / 2)*Surface_Area)
    return D

#def render_airfoil():

'''
def render_graph(buffer_arr, x_increment, y_increment, x_lower, y_lower, x_max, y_max, x_name, y_name):
    width = x_max - x_lower
    height = y_max - y_lower
    pixels = [' '] * (height+1) * (width+1)
    #draws x values
    for i in range(x_lower, x_max, x_increment):
        pixels[(height-1) * width + i] = (i + 48)

    #draws y values
    for i in range(y_lower, y_max, y_increment):
        pixels[(i*width)] = (i + 48)
    
    # plots points
    for i in range(0,len(buffer_arr),1):

        
    for z in pixels:
        print(z, end = '')
        if z % width == 0:
            print("")
'''

def tween(lb, ub, increment): # linear tween
    buffer_arr = []

    for i in range(lb, ub+1, increment):
        buffer_arr.append(i)

    return buffer_arr

AOA = 5
#WING_CAMBER = 
LIFT_COEFFICIENT = 2 * math.pi * math.radians(AOA)
OSWALD_FACTOR = .8
ZERO_LIFT_DRAG_COEFFICIENT = 0.02
ASPECT_RATIO = 7.32
PLAN_AREA = 8 # M^3
#WETTED_AREA
ATMOSPHERIC_DENSITY = 1.225 
VELOCITY = 25 # 50 M/S is roughly 110 MPH

lift_force = calc_lift_force(LIFT_COEFFICIENT, ATMOSPHERIC_DENSITY, VELOCITY, PLAN_AREA)
drag_force = calc_drag_force(ZERO_LIFT_DRAG_COEFFICIENT, LIFT_COEFFICIENT, ASPECT_RATIO, OSWALD_FACTOR, ATMOSPHERIC_DENSITY, VELOCITY, PLAN_AREA)

print("Lift Force: ", lift_force)
print("Drag Force: ", drag_force)
