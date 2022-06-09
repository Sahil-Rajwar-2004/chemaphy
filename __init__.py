import numpy as np
import pandas as pd
import math
import trigo
import statistics as stats


            #NOTE#
"""
    Constants
"""

class Constant:
    def __init__(self,value,units,info):
        self.value = value
        self.units = units
        self.info = info


h = Constant(6.626e-34,"joule sec","Plancl's Constant")
e = Constant(1.6e-19,"C","Charge on electron")
epsilon_0 = Constant(8.85e-12,"m^(-3) kg^(-1) s^4 A^2","permitivity in free space")
k = Constant(9e9,"N m^2 C^(-2)","Coulombs constant")
c = Constant(3e8,"m/s","speed of light in vacuum")
R = Constant(1.0973e7,"m^(-1)","Rydbergs's Constant")

pi = Constant(3.1415,None,None)
exp = Constant(2.7182,None,None)

exa = Constant(1e18,None,None)
peta = Constant(1e15,None,None)
tera = Constant(1e12,None,None)
giga = Constant(1e9,None,None)
mega = Constant(1e6,None,None)
kilo = Constant(1e3,None,None)
hecto = Constant(1e2,None,None)
deca = Constant(1e1,None,None)
one = Constant(1e0,None,None)
deci = Constant(1e-1,None,None)
centi = Constant(1e-2,None,None)
milli = Constant(1e-3,None,None)
micro = Constant(1e-6,None,None)
nano = Constant(1e-9,None,None)
pico = Constant(1e-12,None,None)
femto = Constant(1e-15,None,None)
atto = Constant(1e-18,None,None)

Mass_e = Constant(9.1e-31,"kg","Mass of electron")
Mass_p = Constant(1.67262e-27,"kg","Mass of proton")
Mass_n = Constant(1.67493e-27,"kg","Mass of neutron")

g_sun = Constant(274,"m/s^2","garvity on Sun")
g_mercury = Constant(3.7,"m/s^2","gravity on Mercury")
g_venus = Constant(8.87,"m/s^2","gravity on Venus")
g_earth = Constant(9.8,"m/s^2","gravity on Earth")
g_moon = Constant(1.62,"m/s^2","gravity on Moon")
g_mars = Constant(3.712,"m/s^2","gravity on Mars")
g_jupiter = Constant(24.79,"m/s^2","gravity on Jupiter")
g_saturn = Constant(10.44,"m/s^2","gravity on Saturn")
g_uranus = Constant(8.87,"m/s^2","gravity on Uranus")
g_neptune = Constant(11.15,"m/s^2","gravity on Neptune")
G = Constant(6.6743e-11,"m^3 kg^(-1) s^(-2)","Gravitational Constant")

mass_sun = Constant(1.989e30,"kg","Mass of Sun")
radius_sun = Constant(696340000,"m","Radius of Sun")
mass_mercury = Constant(6.39e23,"kg","Radius of Mercury")
radius_mercury = Constant(3389500,"m","Radius of Mercury")
mass_venus = Constant(4.867e24,"kg","Mass of Venus")
radius_venus = Constant(6051800,"m","Radius of Venus")
mass_earth = Constant(5.972e24,"kg","Mass of Earth")
radius_earth = Constant(6371800,"m","Radius of Earth")
mass_moon = Constant(7.347e22,"kg","Mass of Moon")
radius_moon = Constant(1737400,"m","Radius of Moon")
mass_mars = Constant(6.39e23,"kg","Mass of Mars")
radius_mars = Constant(3389500,"m","Radius of Mars")
mass_jupiter = Constant(1.898e27,"kg","Mass of Jupiter")
radius_jupiter = Constant(69911000,"m","Radius of Jupiter")
mass_saturn = Constant(5.683e26,"kg","Mass of Saturn")
radius_saturn = Constant(58232000,"m","Radius of Saturn")
mass_uranus = Constant(8.681e25,"kg","Mass of Sturn")
radius_uranus = Constant(25362000,"m","Radius of Uranus")
mass_neptune = Constant(1.024e26,"kg","Mass of Neptune")
radius_neptune = Constant(24622000,"m","Radius of Neptune")


class ModernPhysics:
    def kinetic_energy_of_electron(Z,n) -> int:
        K = (Mass_e.value*(Z**2)*(e.value**4))/(8*(epsilon_0.value**2)*(h.value**2)*(n**2))
        return f"{round(K,70)} j"

    def potential_energy_of_atom(Z,n) -> int:
        V = -(Mass_e.value*Z**2*e.value**4)/(4*epsilon_0.value**2*h.value**2*n**2)
        return f"{round(V,70)} j"

    def total_energy_of_atom(Z,n) -> int:
        E = -(Mass_e.value*Z**2*e.value**4)/(8*epsilon_0.value**2*h.value**2*n**2)
        return f"{round(E,70)} j"

    def freq(wave_len) -> int:
        f = c.value/wave_len
        return f"{f} Hz"

    def energy_of_photon(wave_len) -> int:
        E = h.value*c.value/wave_len
        return f"{E} j"

    def momentum_of_electron(Z,n) -> int:
        vel = (2.18*10**(6)*Z)/n
        return f"{vel} kgm/s^2"

    def de_Broglie_wavelength_particle(mass,vel) -> int:
        wave_len = h.value/(mass*vel)
        return wave_len

    def half_life(decay_const) -> int:
        t = 0.693/decay_const
        return f"{round(t,2)} yrs"


class ClassicalPhysics:

    """
    mass: int
    acc: int
    """

    def Force(mass,acc) -> int:
        F = mass*acc
        return f"{F} N"

    """
    mass: int
    d(distance): int
    """

    def GravitationalField(mass_obj1,mass_obj2,d) -> int:
        F = (G.value*mass_obj1*mass_obj2)/d**2
        return f"{round(F,2)} N"

    def GravitationalPotential(mass_obj1,mass_obj2,d) -> int:
        U = -(G.value*mass_obj1*mass_obj2)/d
        return f"{round(U,2)} J/kg"

    """
    gravity: int
    r(radius): int
    """

    def EscapeVelocity(gravity,r) -> int:
        """
            The minimum velocity in which a body must have in order to escape
            the gravitational pull of a particular planet or other object.

            mass_e => mass of the body escape from
            r => distace from the center of mass 
        """
        Ve = math.sqrt(2*gravity*r)
        Ve = Ve/1000
        return f"{round(Ve,2)} km/s"

    """
    mass: int
    """

    def SchwarzschildRadius(m_obj) -> int:
        r = (2*G.value*m_obj)/c.value
        return f"{round(r,3)}"

    """
    r(radius): int
    f(force): int
    angle(deg): int
    """

    def Torque(r,f,angle) -> int:
        deg = np.deg2rad(angle)
        tau = r*f*trigo.sin(deg)
        return f"{round(tau,3)} Nm"

    """
    I(current): int
    R(Resistor): int
    """

    def Ohm(I,R) -> int:
        return f"{I*R} Volt"

    """
    F(force): int
    d(distance): int
    angle(int): int
    """

    def WorkDone(F,d,angle) -> int:
        deg = np.deg2rad(angle)
        W = F*d*trigo.sin(deg)
        return f"{round(W,3)} j"

    """
    W(watt): int
    t(time): int
    """

    def Power(W,t) -> int:
        return f"{W/t} Watt"

    def AvgSpeed(total_distance,total_time) -> int:
        avg = total_distance/total_time
        return f"{round(avg,2)} dist/time"

    def AvgVelocity(total_displacment,total_time) -> int:
        avg = total_displacment/total_time
        return f"{round(avg,2)} dist/time"


class ProjectileMotion:
    def HorizontalRange(velocity,gravity,angle) -> int:
        deg = np.deg2rad(angle)
        R = (velocity**2*trigo.sin(2*deg))/gravity
        return f"{round(R,2)} m"

    def MaximumHeight(velocity,gravity,angle) -> int:
        deg = np.deg2rad(angle)
        H = (velocity**2*(trigo.sin(deg)**2))/(2*gravity)
        return f"{round(H,2)} m"

    def TimeInterval(velocity,gravity,angle) -> int:
        deg = np.deg2rad(angle)
        T = (2*velocity*trigo.sin(deg))/gravity
        return f"{round(T,2)} sec"


class AlternatingCurrent:
    def Irms2I(rms) -> int:
        i = rms*math.sqrt(2)
        return f"{round(i,2)} Ampere"
    
    def I2Irms(current) -> int:
        rms = current/math.sqrt(2)
        return f"{round(rms,2)} Ampere"

    def Vrms2V(rms) -> int:
        v = rms*math.sqrt(2)
        return f"{round(v,2)} Volts"

    def V2Vrms(volt) -> int:
        rms = volt/math.sqrt(2)
        return f"{round(rms,2)} Volts"

    def AngularFrequency(frequency) -> int:
        w = 2*pi.value*frequency
        return w

    def CapacitanceReactance(freq,C) -> int:
        Xc = 1/(2*pi.value*freq*C)
        return f"{round(Xc,2)} Ohm"

    def InductiveReactance(freq,L) -> int:
        Xl = 2*pi.value*freq*L
        return f"{round(Xl,2)} Ohm"

    def Impedance(Xc,Xl,R) -> int:
        Z = math.sqrt(R**2+(Xl-Xc)**2)
        return f"{round(Z,2)} Ohm"

    def Phase(Xc,Xl,R) -> int:
        phi = trigo.arc_tan((Xc-Xl)/R)
        return f"{round(phi,2)}"

    def PowerDissipated(v,i) -> int:
        p = i**2*v
        return f"{round(p,2)}"

    def ResonanceFrequency(L,C) -> int:
        f = 1/(2*pi.value*math.sqrt(L*C))
        return f"{round(f,2)} Hz"

    def ParallelResonanceFrequency(L,C,R) -> int:
        f = (1/(2*pi.value))*math.sqrt(1/(L*C)-(R**2/L**2))
        return f"{round(f,2)} Hz"

    def QualitativeFactor(R,L,C) -> int:
        Q = (1/R)*math.sqrt(L/C)
        return f"{round(Q,2)}"


class Statistics:
    def Factorial(num) -> int:
        """
        It is the product of less than equal to n(number).\n
        Denoted as `n!`

        for more info: <https://www.google.com/search?q=factorial>

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        `n! = n*(n-1)*(n-2)*...*1`
        """
        return math.factorial(num)

    def Permutations(n,r) -> int:
        """
        A technique to determines the number of possible arrangements in a set when the order of the arrangements matters.\n
        Denoted as `nPr` where `n` is total number of objects and `r` is selected objects for arrangements\n

        for more info: <https://www.google.com/search?q=permuation>

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        `nPr = n!/(n-r)!`
        """
        return math.factorial(n)/math.factorial(n-r)

    def Combinations(n,r) -> int:
        """
        An arrangement of objects where the order in which the objects are selected doesn't matter.\n
        Denoted as 'nCr' where `n` is total number of objects in the set and `r` number of choosing objects from the set\n

        for more info: <https://www.google.com/search?q=combination>\n

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        `nCr = n!/r!(n-r)!`
        """
        return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

    def Quartiles(args) -> list:
        """
        In statistics, a quartile is a type of quantile which divides the number of data points into four parts, or quarters, of more-or-less equal size\n
        the data must be in ascending order.\n

        for more info: <https://www.google.com/search?q=quartiles>\n

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        lower:  `(N+1)*1/2`\n
        middle: `(N+1)*1/4`\n
        upper:  `(N+1)*3/4`\n

        where `N` is number of data

        """
        rel = sorted(args,reverse = False)
        lower_Q = int((len(args)+1)*0.25)
        middle_Q = int((len(args)+1)*0.5)
        upper_Q = int((len(args)+1)*0.75)
        return f"Lower Quartile: {rel[lower_Q-1]}\nMiddle Quartile: {rel[middle_Q-1]}\nUpper Quartile: {rel[upper_Q-1]}"

    def Absolute(num) -> int:
        """
        Absolute value or Modulus Value both are functions that always gives positive number no matter what kind of integer you are giving as an input\n
        Denoted as `|x|`\n

        for more info: <https://www.google.com/search?q=absolute+value>\n

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        `|x| = {x; if x >= 0, -x; if x < 0}`
        """
        if num >= 0:
            return num
        elif num < 0:
            return num*(-1)
        else:
            return "Invalid input"

    def Mean(args) -> list:
        """
        Its gives an average value form a given datasets\n
        Dentnoted as `x̄`\n

        for more info: <https://www.google.com/search?q=mean>\n

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        `x̄ = sum of the data/total number of the data`
        """
        return f"{round(sum(args)/len(args),3)}"

    def RunningMean(args) -> list:
        """
        A moving average is a calculation to analyze data points by creating a series of averages of different subsets of the full data set.\n

        for more info: <https://www.google.com/search?q=running+mean>
        """
        avg = []
        i = 0
        size = 3
        while i < len(args)-size+1:
            w = args[i : i+size]
            s = round(sum(w)/size,2)
            avg.append(s)
            i += 1
        return avg

    def HarmonicMean(args) -> list:
        """
        It is calculated by dividing the number of observations by the reciprocal of each number in the series.\n

        for more info: <https://www.google.com/search?q=harmonic+mean>
        """
        s = 0
        for i in range(0,len(args)):
            a = 1/(args[i])
            s += a
        return f"{round(len(args)/s,3)}"

    def GeometricMean(args) -> list:
        """
        The geometric mean is a mean or average, which indicates the central tendency or typical value of a set of numbers by using the product of their values\n

        for more info: <https://www.google.com/search?q=geometric+mean>\n

        ===========================\n
        Mathematical Representation\n
        ===========================\n
        GM1 = sqrt(ab)
        GM2 = cubert(abc)
        """
        p = 1
        for i in range(0,len(args)):
            a = args[i]
            p *= a
        return f"{round(p**(1/len(args)),3)}"

    def Mode(args) -> list:
        """
        It gives the number from a given set that repeats maximum times

        for more info: <https://www.google.com/search?q=mode>
        """
        return f"{round(stats.mode(args),3)}"

    def Range(args) -> list:
        return f"{max(args)-min(args)}"

    def Product(args) -> list:
        """
        It will multiply all the elements containing in the list
        """
        p = 1
        for i in range(0,len(args)):
            p *= args[i]
        return f"{p}"

    def SquareSum(args) -> list:
        s = 0
        for i in range(0,len(args)):
            sq = args[i]**2
            s += sq
        return f"{s}"

    def StandardDeviation(args) -> list:
        mean = round(sum(args)/len(args),3)
        rep = []
        for i in range(0,len(args)):
            a = (args[i]-mean)**2
            rep.append(a)
        total = sum(rep)
        return (round(math.sqrt(total/(len(args)-1)),3))

    def Median(args) -> list:
        if len(args)%2 == 0:
            mid1 = int(len(args)/2)
            mid2 = mid1-1
            return (args[mid1]+args[mid2])/2
        else:
            mid = int(len(args)/2)
            return args[mid]

    def MeanDeviation(args) -> list:
        mean = round(sum(args)/len(args),3)
        rep = []
        for i in range(0,len(args)):
            a = abs(args[i]-mean)
            rep.append(a)
        total = sum(rep)
        return round(total/len(args),3)

    def Percentile(args:list,n:int):
        if n in args:
            b = 0
            for i in range(0,len(args)):
                if n > args[i]:
                    b += 1
                else:
                    b += 0
            return f"{((b/len(args))*100)}"
        else:
            return f"Unexpected Input! {n} is not in {args}!"

    def MedianAvgDeviation(args) -> list:
        m = sum(args)/len(args)
        rel = []
        for i in range(0,len(args)):
            a = abs(args[i]-m)
            rel.append(a)
        mid = Statistics.Median(rel)
        return f"{mid}"

    def CumSum(args) -> list:
        s = 0
        cumsum = []
        for i in range(0,len(args)):
            s += args[i]
            cumsum.append(s)
        return cumsum

    def SampleVariance(args) -> list:
        mean = round(sum(args)/len(args),3)
        rep = []
        for i in range(0,len(args)):
            a = (args[i]-mean)**2
            rep.append(a)
        total = sum(rep)
        return round(total/(len(args)-1),3)

    def PopulationVariance(args) -> list:
        mean = round(sum(args)/len(args),3)
        rep = []
        for i in range(0,len(args)):
            a = (args[i]-mean)**2
            rep.append(a)
        total = sum(rep)
        return round(total/(len(args)),3)

    def RMS(args) -> list:
        rep = []
        for i in range(0,len(args)):
            a = args[i]**2
            rep.append(a)
        total = sum(rep)
        return round(math.sqrt(total/len(args)),3)

    def LR(args,kwargs) -> list:
        if len(args) == len(kwargs):
            y = sum(kwargs)
            x = sum(args)
            xy = 0
            x2 = 0
            for i in range(0,len(args)):
                a = args[i]**2
                b = args[i]*kwargs[i]
                xy += b
                x2 += a
            N1 = y*x2-x*xy
            D1 = len(args)*x2-x**2
            intercept = round(N1/D1,3)
            N2 = len(args)*xy-x*y
            D2 = len(args)*x2-x**2
            slope = round(N2/D2,3)
            return f"Intercept: {intercept}\nSlope: {slope}\ny = {slope}x + {intercept}"
        else:
            return "Length of the both parameters should be euqal"

    def StandardError(args) -> list:
        dev = Statistics.StandardDeviation(args)
        return round(dev/math.sqrt(len(args)),3)

    def RelativeFrequency(args) -> list:
        rel = []
        freq = {}
        for item in args:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        f = list(freq.values())
        for i in range(0,len(f)):
            r = f[i]/len(args)
            rel.append(r)
        return f"{freq}\n{rel}"

    def CorrelationCoefficient(args,kwargs) -> list:
        if len(args) == len(kwargs):
            y = sum(kwargs)
            x = sum(args)
            xy = 0
            x2 = 0
            y2 = 0
            for i in range(0,len(args)):
                a = args[i]**2
                b = args[i]*kwargs[i]
                c = kwargs[i]**2
                x2 += a
                xy += b
                y2 += c
            N = len(args)*xy-x*y
            D = math.sqrt((len(args)*x2-x**2)*(len(args)*y2-y**2))
            return f"{round(N/D,3)}"
        else:
            return "Length of the both parameters should be euqal"

    def CoefficientDetermination(args,kwargs) -> list:
        if len(args) == len(kwargs):
            x = sum(args)
            y = sum(kwargs)
            x2 = 0
            y2 = 0
            xy = 0
            for i in range(0,len(args)):
                a = args[i]**2
                b = args[i]*kwargs[i]
                c = kwargs[i]**2
                x2 += a
                y2 += c
                xy += b
            N = len(args)*xy-x*y
            D = math.sqrt((len(args)*x2-x**2)*(len(args)*y2-y**2))
            return f"{round(N/D,3)}"
        else:
            return "Length of the both parameters should be euqal"

class DistanceFormula:

    """
    x,y,z: int
    """

    def Distance2d(x1,x2,y1,y2) -> int:
        d = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return f"{round(d,2)} units"

    def Distance3d(x1,x2,y1,y2,z1,z2) -> int:
        d = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
        return f"{round(d,2)} units"


class SectionFormula:

    """
    x,y,z: int
    """

    def Section2d(x1,x2,y1,y2,n,m) -> int:
        x = x1*m+x2*n
        y = y1*m+y2*n
        ratio = n+m
        return f"{x}/{ratio},{y}/{ratio}"

    def Section3d(x1,x2,y1,y2,z1,z2,n,m) -> int:
        x = x1*m+x2*n
        y = y1*m+y2*n
        z = z1*m+z2*n
        ratio = n+m
        return f"{x}/{ratio},{y}/{ratio},{z}/{ratio}"


class Area:
    def Circle(radius) -> int:
        return f"{round(pi.value*radius**2,2)} sqr units"

    def Square(sides) -> int:
        return f"{round(sides**2,2)} sqr units"

    def Rhombus(diagonal_1,diagonal_2) -> int:
        return f"{round(diagonal_1*diagonal_2*0.5,2)} units"

    def Reactangle(length,breadth) -> int:
        return f"{round(length*breadth,2)} sqr units"

    def Parallelogram(length,breadth) -> int:
        return f"{round(length*breadth,2)} sqr units"

    def Triangle(height,base) -> int:
        return f"{round(0.5*height*base,2)} sqr units"

    def Equilateral_triangle(side) -> int:
        deg = np.deg2rad(60)
        return f"{round(0.5*trigo.sin(deg)*side**2,2)} sqr units"

    def Ellipse(a,b) -> int:
        return f"{round(pi.value*a*b,2)} sqr units"

    def Trapezium(a,b,height) -> int:
        return f"{((a+b)*0.5)*height} sqr units"

    def Sector(angle,radius) -> int:
        return f"{(angle/360)*pi.value*radius**2} sqr units"
    

class Perimeter:
    def Circle(radius) -> int:
        return f"{round(2*pi.value*radius,2)} units"

    def Square(side) -> int:
        return f"{round(4*side,2)} units"

    def Rhombus(side) -> int:
        return f"{round(4*side,2)} units"

    def Rectangle(length,breadth) -> int:
        return f"{round(2*(length+breadth),2)} units"

    def Parallelogram(length,breadth) -> int:
        return f"{round(2*(length+breadth),2)}"

    def Triangle(side1,side2,side3) -> int:
        p = side1+side2+side3
        return f"{round(p,2)} units"

    def Ellipse(a,b) -> int:
        p = (2*pi.value)*math.sqrt(a**2*b**2*0.5)
        return f"{round(p,3)} units"

    def Trapezium(a,b,c,d) -> int:
        return f"{a+b+c+d} units"

    def Sector(radius,angle) -> int:
        return f"{round((2*radius)+((angle/360)*2*pi.value*radius),2)} units"


class Volume:
    def Cube(side) -> int:
        return f"{round(side**3,2)} units cube"

    def Cuboid(length,breadth,height) -> int:
        return f"{round(length*breadth*height,2)} units cube"

    def Cylinder(radius,height) -> int:
        return f"{round(pi.value*radius**2*height,2)} units cube"

    def Prism(length,breadth,Height) -> int:
        return f"{round(length*breadth*Height,2)} units cube"

    def Sphere(radius) -> int:
        return f"{round((4/3)*pi.value*radius**3,2)} units cube"

    def Pyramid(length,breadth,Height) -> int:
        return f"{round((1/3)*length*breadth*Height,2)} units cube"

    def RightCircularCone(radius,height) -> int:
        return f"{round((1/3)*pi.value*radius**2*height,2)} units cube"

    def QuadBasePyramid(length,width,height) -> int:
        return f"{round((1/3)*pi.value*length*width*height,2)} units cube"

    def Ellipsoid(x,y,z) -> int:
        return f"{round((4/3)*pi.value*x*y*z,2)} units cube"


    # NOTE! #

    """
        We are assuming the side of the polyhedron are same or
        we can say regular polyhedron
    """
    
    def Tetrahedron(side) -> int:
        return f"{round((side**3)*6*math.sqrt(2),2)} units cube"

    def Octahedron(side) -> int:
        return f"{round((math.sqrt(2)/3)*side**3,2)}"

    def Dodecahedron(side) -> int:
        return f"{round(((15+7*math.sqrt(5))/4)*side**3,2)} units cube"


class Chemistry:
    def PeriodicTable(element) -> str:
        df = pd.read_csv("https://raw.githubusercontent.com/Sahil-Rajwar-2004/Datasets/main/elements.csv")
        df.rename(columns = {"MeltingPoint":"MeltingPoint (K)","BoilingPoint":"BoilingPoint (K)"}, inplace = True)
        data = df[["Element","Symbol","AtomicNumber","AtomicMass","NumberofNeutrons","NumberofProtons","NumberofElectrons","Period","Group","Phase","MeltingPoint (K)","BoilingPoint (K)"]]
        return data[data["Element"].str.lower() == element]

    def HalfLifeZeroOrder(Ao,k) -> int:
        """
            Ao(Initial Concentration): int
            k(Rate Constant): int
        """
        t = Ao/(2*k)
        return f"{round(t,2)} yrs"

    def HalfLifeFirstOrder(k) -> int:
        """
            k(Rate Constant): int
        """
        t = 0.693/(2*k)
        return f"{round(t,2)} yrs"

    def HalfLifeThirdOrder(Ao,k) -> int:
        """
            Ao(Initial Concentration): int
            k(Rate Constant): int
        """
        t = 1/(Ao*k)
        return f"{round(t,2)} yrs"

    """
    P(Concetration on produt): int
    R(Conetration on reactant): int
    std_potential(Standard Potential): int
    """

    def NernstEquation(P,R,n,std_potential) -> int:
        E = std_potential - (0.06/n)*math.log10(R/P)
        return f"{round(E,2)} Volts"

    """
    oxdn(oxidation): int
    redn(redution): int
    """

    def StdPotential(oxdn,redn) -> int:
        E = redn-oxdn
        return f"{E} Volts"

    def MassPercent(mass_solute,mass_solution) -> int:
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
    def log_e(x) -> int:
        ln = np.log(x)
        return round(ln,3)

    def log_10(x) -> int:
        log = np.log10(x)
        return round(log,3)


class Trigonometry:

    # Degrees

    def sin_deg(angle) -> int:
        deg = np.deg2rad(angle)
        return round(trigo.sin(deg),2)

    def cos_deg(angle) -> int:
        deg = np.deg2rad(angle)
        return round(trigo.cos(deg),2)

    def tan_deg(angle) -> int:
        deg = np.deg2rad(angle)
        return round(trigo.tan(deg),2)

    def sec_deg(angle) -> int:
        deg = np.deg2rad(angle)
        return round(trigo.sec(deg),2)

    def cosec_deg(angle) -> int:
        deg = np.deg2rad(angle)
        return round(trigo.cosec(deg),2)

    def cot_deg(angle) -> int:
        deg = np.deg2rad(angle)
        return round(trigo.cot(deg),2)

    # Radians

    def sin_rad(angle) -> int:
        return round(trigo.sin(angle),2)

    def cos_rad(angle) -> int:
        return round(trigo.cos(angle),2)

    def tan_rad(angle) -> int:
        return round(trigo.tan(angle),2)

    def sec_rad(angle) -> int:
        return round(trigo.sec(angle),2)

    def cosec_rad(angle) -> int:
        return round(trigo.cosec(angle),2)

    def cot_rad(angle) -> int:
        return round(trigo.cot(angle),2)

class InversTrigonometry:
    
    def arcsine_rad(num) -> int:
        angle = trigo.arc_sin(num)
        return angle

    def arccos_rad(num) -> int:
        angle = trigo.arc_cos(num)
        return angle

    def arctan_rad(num) -> int:
        angle = trigo.arc_tan(num)
        return angle

    def arccosec_rad(num) -> int:
        angle = trigo.arc_cosec(num)
        return angle

    def arcsec_rad(num) -> int:
        angle = trigo.arc_sec(num)
        return angle

    def arccot_rad(num) -> int:
        angle = trigo.arc_cot(num)
        return angle

class Matrix:
    def Matrices(matrix:list,dimension:tuple): #--> Row,Column
        dimension = tuple(dimension)
        try:
            m = np.matrix(matrix).reshape((dimension))
            return m
        except ValueError as error:
            return error

    def Transpose(matrix) -> int:
        return matrix.T

    def Product(X,Y) -> int:
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

    def Addition(X,Y) -> int:
        try:
            return np.add(X,Y)
        except ValueError as error:
            return error

    def Substraction(X,Y) -> int:
        try:
            return np.subtract(X,Y)
        except ValueError as error:
            return error
    
    def InverseMatrix(X) -> int:
        try:
            return np.linalg.inv(X)
        except np.linalg.LinAlgError as error:
            return error

    def Determinant(X) -> int:
        try:
            return np.linalg.det(X)
        except np.linalg.LinAlgError as error:
            return error


class Sets:
    def Sets(A) -> int:
        return set(A)

    def Union(A,B) -> int:
        return set.union(A,B)

    def Intersections(A,B) -> int:
        return set.intersection(A,B)


class Vectors:
    def toVector(x1,y1,z1,x2,y2,z2) -> int:
        x = x2-x1
        y = y2-y1
        z = z2-z1
        return f"{x}i,{y}j,{z}k"

    def ScalarMagnitude(i,j,k) -> int:
        m = math.sqrt(i**2+j**2+k**2)
        return f"{round(m,2)}"

    def DotProduct(x1,y1,z1,x2,y2,z2) -> int:
        x = x1*x2
        y = y1*y2
        z = z1*z2
        return f"{x+y+z}"

    def UnitVector(i,j,k) -> int:
        mag = math.sqrt(i**2+j**2+k**2)
        return f"{i}/{round(mag,1)}i,{j}/{round(mag,1)}j,{k}/{round(mag,1)}k"

    def CrossProduct(i1,j1,k1,i2,j2,k2) -> int:
        arr = np.array([[i1],[j1],[k1],
                        [i2],[j2],[k2]])

        a = arr[1][0]*arr[5][0]-arr[4][0]*arr[2][0]
        b = arr[0][0]*arr[5][0]-arr[3][0]*arr[2][0]
        c = arr[0][0]*arr[4][0]-arr[3][0]*arr[1][0]
        return f"({a})i,-({b})j,({c})k"

    def VectorMagnitude(i1,j1,k1,i2,j2,k2) -> int:
        arr = np.array([[i1],[j1],[k1],
                        [i2],[j2],[k2]])

        i = arr[1][0]*arr[5][0]-arr[4][0]*arr[2][0]
        j = arr[0][0]*arr[5][0]-arr[3][0]*arr[2][0]
        k = arr[0][0]*arr[4][0]-arr[3][0]*arr[1][0]
        m = math.sqrt(i**2+j**2+k**2)

        return f"{round(m,2)}"
