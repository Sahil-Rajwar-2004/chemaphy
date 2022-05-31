import numpy as np
import pandas as pd
import math
import trigo

            #NOTE#
"""
    Z => Atomic Number of Hydrogen Like Atoms for example:
    H,He+,Li++,Be4+

    n => Shell in which atom is revolving around the nucleus
    value of n can be from minimum 1 to 2,3,4 or maximum 6 not more than that
"""

class Constants:
    def __init__(self,value,units,info):
        self.value = value
        self.units = units
        self.info = info


h = Constants(6.626*10**(-34),"joule sec","Plancl's Constants")
e = Constants(1.6*10**(-19),"C","Charge on electron")
epsilon_0 = Constants(8.85*10**(-12),"m^(-3) kg^(-1) s^4 A^2","permitivity in free space")
k = Constants(9*10**(9),"N m^2 C^(-2)","Coulombs constant")
c = Constants(3*10**(8),"m/s","speed of light in vacuum")
R = Constants(1.0973*10**(7),"m^(-1)","Rydbergs's Constants")

pi = Constants(3.1415,None,None)
exp = Constants(2.7182,None,None)

Mass_e = Constants(9.1*10**(-31),"kg","Mass of electron")
Mass_p = Constants(1.67262*10**(-27),"kg","Mass of proton")
Mass_n = Constants(1.67493*10**(-27),"kg","Mass of neutron")

g_Sun = Constants(274,"m/s^2","garvity on Sun")
g_Mercury = Constants(3.7,"m/s^2","gravity on Mercury")
g_Venus = Constants(8.87,"m/s^2","gravity on Venus")
g_Earth = Constants(9.8,"m/s^2","gravity on Earth")
g_Moon = Constants(1.62,"m/s^2","gravity on Moon")
g_Mars = Constants(3.712,"m/s^2","gravity on Mars")
g_Jupiter = Constants(24.79,"m/s^2","gravity on Jupiter")
g_Saturn = Constants(10.44,"m/s^2","gravity on Saturn")
g_Uranus = Constants(8.87,"m/s^2","gravity on Uranus")
g_Neptune = Constants(11.15,"m/s^2","gravity on Neptune")
G = Constants(6.6743*10**(-11),"m^3 kg^(-1) s^(-2)","Gravitational Constants")

Mass_Sun = Constants(1.989*10**(30),"kg","Mass of Sun")
Radius_Sun = Constants(696340000,"m","Radius of Sun")
Mass_Mercury = Constants(6.39*10**(23),"kg","Radius of Mercury")
Radius_Mercury = Constants(3389500,"m","Radius of Mercury")
Mass_Venus = Constants(4.867*10**(24),"kg","Mass of Venus")
Radius_Venus = Constants(6051800,"m","Radius of Venus")
Mass_Earth = Constants(5.972*10**(24),"kg","Mass of Earth")
Radius_Earth = Constants(6371800,"m","Radius of Earth")
Mass_Moon = Constants(7.347*10**(22),"kg","Mass of Moon")
Radius_Moon = Constants(1737400,"m","Radius of Moon")
Mass_Mars = Constants(6.39*10**(23),"kg","Mass of Mars")
Radius_Mars = Constants(3389500,"m","Radius of Mars")
Mass_Jupiter = Constants(1.898*10**(27),"kg","Mass of Jupiter")
Radius_Jupiter = Constants(69911000,"m","Radius of Jupiter")
Mass_Saturn = Constants(5.683*10**(26),"kg","Mass of Saturn")
Radius_Saturn = Constants(58232000,"m","Radius of Saturn")
Mass_Uranus = Constants(8.681*10**(25),"kg","Mass of Sturn")
Radius_Uranus = Constants(25362000,"m","Radius of Uranus")
Mass_Neptune = Constants(1.024*10**(26),"kg","Mass of Neptune")
Radius_Neptune = Constants(24622000,"m","Radius of Neptune")


class ModernPhysics:
    def kinetic_energy_of_electron(Z,n):
        K = (Mass_e.value*(Z**2)*(e.value**4))/(8*(epsilon_0.value**2)*(h.value**2)*(n**2))
        return f"{round(K,70)} j"

    def potential_energy_of_atom(Z,n):
        V = -(Mass_e.value*Z**2*e.value**4)/(4*epsilon_0.value**2*h.value**2*n**2)
        return f"{round(V,70)} j"

    def total_energy_of_atom(Z,n):
        E = -(Mass_e.value*Z**2*e.value**4)/(8*epsilon_0.value**2*h.value**2*n**2)
        return f"{round(E,70)} j"

    def freq(wave_len):
        f = c.value/wave_len
        return f"{f} Hz"

    def energy_of_photon(wave_len):
        E = h.value*c.value/wave_len
        return f"{E} j"

    def momentum_of_electron(Z,n):
        vel = (2.18*10**(6)*Z)/n
        return f"{vel} kgm/s^2"

    def de_Broglie_wavelength_particle(mass,vel):
        wave_len = h.value/(mass*vel)
        return wave_len

    def half_life(decay_const):
        t = 0.693/decay_const
        return f"{round(t,2)} yrs"


class ClassicalPhysics:
    def force(mass,acc):
        F = mass*acc
        return f"{F} N"

    """
        Gravitaional Force is force between two or more celestial bodies
    """

    def gravitational_force_obj(mass_obj1,mass_obj2,d):
        F = (G.value*mass_obj1*mass_obj2)/d**2
        return f"{round(F,2)} N"

    def escape_velocity(gravity,r):
        """
            The minimum velocity in which a body must have in order to escape
            the gravitational pull of a particular planet or other object.

            mass_e => mass of the body escape from
            r => distace from the center of mass 
        """
        Ve = math.sqrt(2*gravity*r)
        Ve = Ve/1000
        return f"{round(Ve,2)} km/s"

    def schwarzschild_radius(M_obj):
        r = (2*G.value*M_obj)/c.value
        return f"{round(r,3)}"

    def torque(r,f,angle):
        deg = np.deg2rad(angle)
        tau = r*f*trigo.sin(deg)
        return f"{round(tau,3)} Nm"

    def ohm(I,R):
        return f"{I*R} Volt"

    def work_done(F,d,angle):
        deg = np.deg2rad(angle)
        W = F*d*trigo.sin(deg)
        return f"{round(W,3)} j"

    def power(W,t):
        return f"{W/t} Watt"


class ProjectileMotion:
    def horizontal_range(velocity,gravity,angle):
        deg = np.deg2rad(angle)
        R = (velocity**2*trigo.sin(2*deg))/gravity
        return f"{round(R,2)} m"

    def maximum_height(velocity,gravity,angle):
        deg = np.deg2rad(angle)
        H = (velocity**2*(trigo.sin(deg)**2))/(2*gravity)
        return f"{round(H,2)} m"

    def time_interval(velocity,gravity,angle):
        deg = np.deg2rad(angle)
        T = (2*velocity*trigo.sin(deg))/gravity
        return f"{round(T,2)} sec"


class Area:
    def circle(radius):
        return f"{round(Constants.pi*radius**2,2)} sqr units"

    def square(sides):
        return f"{round(sides**2,2)} sqr units"

    def rhombus(diagonal_1,diagonal_2):
        return f"{round(diagonal_1*diagonal_2*0.5,2)} units"

    def reactangle(length,breadth):
        return f"{round(length*breadth,2)} sqr units"

    def parallelogram(length,breadth):
        return f"{round(length*breadth,2)} sqr units"

    def triangle(height,base):
        return f"{round(0.5*height*base,2)} sqr units"

    def equilateral_triangle(side):
        deg = np.deg2rad(60)
        return f"{round(0.5*trigo.sin(deg)*side**2,2)} sqr units"

    def ellipse(a,b):
        return f"{round(Constants.pi*a*b,2)} sqr units"

    def trapezium(a,b,height):
        return f"{((a+b)*0.5)*height} sqr units"

    def sector(angle,radius):
        return f"{(angle/360)*Constants.pi*radius**2} sqr units"
    

class Perimeter:
    def circle(radius):
        return f"{round(2*Constants.pi*radius,2)} units"

    def square(side):
        return f"{round(4*side,2)} units"

    def rhombus(side):
        return f"{round(4*side,2)} units"

    def rectangle(length,breadth):
        return f"{round(2*(length+breadth),2)} units"

    def parallelogram(length,breadth):
        return f"{round(2*(length+breadth),2)}"

    def triangle(side1,side2,side3):
        p = side1+side2+side3
        return f"{round(p,2)} units"

    def ellipse(a,b):
        p = (2*Constants.pi)*math.sqrt(a**2*b**2*0.5)
        return f"{round(p,3)} units"

    def trapezium(a,b,c,d):
        return f"{a+b+c+d} units"

    def sector(radius,angle):
        return f"{round((2*radius)+((angle/360)*2*Constants.pi*radius),2)} units"


class Volume:
    def cube(side):
        return f"{round(side**3,2)} units cube"

    def cuboid(length,breadth,height):
        return f"{round(length*breadth*height,2)} units cube"

    def cylinder(radius,height):
        return f"{round(Constants.pi*radius**2*height,2)} units cube"

    def prism(length,breadth,Height):
        return f"{round(length*breadth*Height,2)} units cube"

    def sphere(radius):
        return f"{round((4/3)*Constants.pi*radius**3,2)} units cube"

    def pyramid(length,breadth,Height):
        return f"{round((1/3)*length*breadth*Height,2)} units cube"

    def right_circular_cone(radius,height):
        return f"{round((1/3)*Constants.pi*radius**2*height,2)} units cube"

    def quad_base_pyramid(length,width,height):
        return f"{round((1/3)*Constants.pi*length*width*height,2)} units cube"

    def ellipsoid(x,y,z):
        return f"{round((4/3)*Constants.pi*x*y*z,2)} units cube"


    # NOTE! #

    """
        We are assuming the side of the polyhedron are same or
        we can say regular polyhedron
    """
    
    def tetrahedron(side):
        return f"{round((side**3)*6*math.sqrt(2),2)} units cube"

    def octahedron(side):
        return f"{round((math.sqrt(2)/3)*side**3,2)}"

    def dodecahedron(side):
        return f"{round(((15+7*math.sqrt(5))/4)*side**3,2)} units cube"


class Chemistry:
    def periodic_table(element):
        df = pd.read_csv("https://raw.githubusercontent.com/Sahil-Rajwar-2004/Datasets/main/elements.csv")
        df.rename(columns = {"MeltingPoint":"MeltingPoint (K)","BoilingPoint":"BoilingPoint (K)"}, inplace = True)
        data = df[["Element","Symbol","AtomicNumber","AtomicMass","NumberofNeutrons","NumberofProtons","NumberofElectrons","Period","Group","Phase","MeltingPoint (K)","BoilingPoint (K)"]]
        return data[data["Element"].str.lower() == element]

    def half_life_0_order(Ao,k):
        """
            Ao => Initial Concentration
            k => Rate Constant
        """
        t = Ao/(2*k)
        return f"{round(t,2)} yrs"

    def half_life_I_order(k):
        """
            k => Rate Constant
        """
        t = 0.693/(2*k)
        return f"{round(t,2)} yrs"

    def half_life_II_order(Ao,k):
        """
            Ao => Initial Concentration
            k => Rate Constant
        """
        t = 1/(Ao*k)
        return f"{round(t,2)} yrs"

    # def nernst_equation(P,R.n)

    def mass_percent(mass_solute,mass_solution):
        M = (mass_solute/mass_solution)*100
        return M


class LogicGates:

            #TRUTH TABLE#

    """
        AND =>  A | B | y = a.b
                0 | 0 | 0
                0 | 1 | 0
                1 | 0 | 0
                1 | 1 | 1

        OR =>   a | b | y = a+b
                0 | 0 | 0
                0 | 1 | 1
                1 | 0 | 1
                1 | 1 | 1
                
        XOR =>  a | b | y = a(+)b
                0 | 0 | 0
                0 | 1 | 1
                1 | 0 | 1
                1 | 1 | 0

        NAND => a | b | y = bar(a.b)
                0 | 0 | 1
                0 | 1 | 1
                1 | 0 | 1
                1 | 1 | 0

        NOR =>  a | b | y = bar(a+b)
                0 | 0 | 1
                0 | 1 | 0
                1 | 0 | 0
                1 | 1 | 0

        XNOR => a | b | y = a(+)b
                0 | 0 | 1
                0 | 1 | 0
                1 | 0 | 0
                1 | 1 | 1

        NOT =>  a | y = bar(a)
                0 | 1
                1 | 0
    """

    def AND(a,b):
        if a == 1 and b == 1:
            return True
        else:
            return False

    def OR(a,b):
        if a == 1 or b == 1:
            return True
        else:
            return False

    def XOR(a,b):
        if a != b:
            return True
        else:
            return False

    def NAND(a,b):
        if a == 1 and b == 1:
            return False
        else:
            return True

    def NOR(a,b):
        if a == 0 and b == 0:
            return True
        elif a == 1 and b == 0:
            return False
        elif a == 0 and b == 1:
            return False
        elif a == 1 and b == 1:
            return False

    def XNOR(a,b):
        if a == b:
            return True
        else:
            return False

    def NOT(a):
        not_gate = not a
        return not_gate


class LogarithmicFunction:
    def log_e(x):
        ln = np.log(x)
        return round(ln,3)

    def log_10(x):
        log = np.log10(x)
        return round(log,3)


class Trigonometry:

    # Degrees

    def sin_deg(angle):
        deg = np.deg2rad(angle)
        return round(trigo.sin(deg),2)

    def cos_deg(angle):
        deg = np.deg2rad(angle)
        return round(trigo.cos(deg),2)

    def tan_deg(angle):
        deg = np.deg2rad(angle)
        return round(trigo.tan(deg),2)

    def sec_deg(angle):
        deg = np.deg2rad(angle)
        return round(trigo.sec(deg),2)

    def cosec_deg(angle):
        deg = np.deg2rad(angle)
        return round(trigo.cosec(deg),2)

    def cot_deg(angle):
        deg = np.deg2rad(angle)
        return round(trigo.cot(deg),2)

    # Radians

    def sin_rad(angle):
        return round(trigo.sin(angle),2)

    def cos_rad(angle):
        return round(trigo.cos(angle),2)

    def tan_rad(angle):
        return round(trigo.tan(angle),2)

    def sec_rad(angle):
        return round(trigo.sec(angle),2)

    def cosec_rad(angle):
        return round(trigo.cosec(angle),2)

    def cot_rad(angle):
        return round(trigo.cot(angle),2)

class InversTrigonometry:
    
    def arcsine_rad(num):
        angle = trigo.arc_sin(num)
        return angle

    def arccos_rad(num):
        angle = trigo.arc_cos(num)
        return angle

    def arctan_rad(num):
        angle = trigo.arc_tan(num)
        return angle

    def arccosec_rad(num):
        angle = trigo.arc_cosec(num)
        return angle

    def arcsec_rad(num):
        angle = trigo.arc_sec(num)
        return angle

    def arccot_rad(num):
        angle = trigo.arc_cot(num)
        return angle

class Matrix:
    def matrices(matrix,dimension): #--> Row,Column
        dimension = tuple(dimension)
        try:
            m = np.matrix(matrix).reshape((dimension))
            return m
        except ValueError as error:
            return error

    def transpose(matrix):
        return matrix.T

    def product(X,Y):
        # Note! #

        """
            The number of columns of a first matrix,
            should be equal to the number of rows
            of a second matrix.
        """
        return np.dot(X,Y)


    # NOTE #

    """
        For addition, subtractions the number of rows and columns
        for matrices should be equal!
        e.g => [[1,2,3],        [[9,8,7,6,5],
                [4,5,6]]         [34,56,87,98],
                                 [12,26,31,65]]

                (2,3)                (3,4)

        And for Determinant and Invverse of a matrices the number of
        rows and columns should be same!
        e.g => [[1,2,3],    [[0,9,8],
                [4,5,6],     [7,6,5],
                [7,8,9]]     [4,3,2]]
                     
                (3,3)           (3,3)
    """

    def addition(X,Y):
        try:
            return np.add(X,Y)
        except ValueError as error:
            return error

    def substraction(X,Y):
        try:
            return np.subtract(X,Y)
        except ValueError as error:
            return error
    
    def inverse_matrix(X):
        try:
            return np.linalg.inv(X)
        except np.linalg.LinAlgError as error:
            return error

    def determinant(X):
        try:
            return np.linalg.det(X)
        except np.linalg.LinAlgError as error:
            return error


