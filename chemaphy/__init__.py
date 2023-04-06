from urllib.error import HTTPError
import numpy as np
import pandas as pd
import math
import trigo
import random
import sympy
import statistics as stats
from matplotlib import pyplot as plt
from matplotlib import style
from .about import (
    author,
    version,
    authorEmail,
    homepage
)

__author__ = author
__version__ = version
__email__ = authorEmail
__homepage__ = homepage


            #NOTE#
"""
    Constants
"""

class Constant:
    def __init__(self,value,units,info):
        self.value = value
        self.units = units
        self.info = info


h = Constant(6.626e-34,"joule sec","Planck's Constant")
e = Constant(1.6e-19,"C","Charge on electron")
epsilon0 = Constant(8.85e-12,"m^(-3) kg^(-1) s^4 A^2","permitivity in free space")
k = Constant(9e9,"N m^2 C^(-2)","Coulombs constant")
c = Constant(3e8,"m/s","speed of light in vacuum")
R = Constant(1.0973e7,"m^(-1)","Rydbergs's Constant")
gasConstant = Constant(8.3145,"J mol^(-1) K^(-1)","Gas Constant")

pi = Constant(3.14159265358979,None,None)
exp = Constant(2.71828182845904,None,None)
inf = Constant(np.inf,None,"Infinity")
NAN = NULL = NaN = nan = null = Constant(np.nan,None,"NaN")
NONE = none = Constant(None,None,None)

class Bool:
    false = FALSE = 0
    true = TRUE = 1

googol = Constant(1e100,None,None)

ang = Constant(1e-10,"m","Angstrom Measuring unit `1A = 10^(-10)m`")
tredecillion = Constant(1e42,None,None)
duodecillion = Constant(1e39,None,None)
undecillion = Constant(1e36,None,None)
decillion = Constant(1e33,None,None)
nonillion = Constant(1e30,None,None)
octillion = Constant(1e27,None,None)
septillion = Constant(1e24,None,None)
sextillion = Constant(1e21,None,None)
quintillion = exa = Constant(1e18,None,None)
quadrillion = peta = Constant(1e15,None,None)
trillion = tera = Constant(1e12,None,None)
billion = giga = Constant(1e9,None,None)
tenCrore = Constant(1e8,None,None)
crore = Constant(1e7,None,None)
tenLakh = million = mega = Constant(1e6,None,None)
lakh = hundredThousand = Constant(1e5,None,None)
tenThousand = Constant(1e4,None,None)
thousand = kilo = Constant(1e3,None,None)
hundred = hecto = Constant(1e2,None,None)
ten = deca = Constant(1e1,None,None)
one = Constant(1e0,None,None)
zero = Constant(0e0,None,None)
oneTenth = deci = Constant(1e-1,None,None)
oneHundredth = centi = Constant(1e-2,None,None)
oneThousandth = milli = Constant(1e-3,None,None)
oneMillionth = micro = Constant(1e-6,None,None)
oneBillionth = nano = Constant(1e-9,None,None)
oneTrillionth = pico = Constant(1e-12,None,None)
oneQuadrillionth = femto = Constant(1e-15,None,None)
oneQuintillionth = atto = Constant(1e-18,None,None)

massElectron = Constant(9.1e-31,"kg","Mass of electron")
electronAmu = Constant(0.00054858,"amu","Mass of electron")
massProton = Constant(1.67262e-27,"kg","Mass of proton")
protonAmu = Constant(1.007825,"amu","Mass of proton")
massNeutron = Constant(1.67493e-27,"kg","Mass of neutron")
neutronAmu = Constant(1.008665,"amu","Mass of neutron")

gSun = Constant(274,"m/s^2","garvity on Sun")
gMercury = Constant(3.7,"m/s^2","gravity on Mercury")
gVenus = Constant(8.87,"m/s^2","gravity on Venus")
gEarth = Constant(9.8,"m/s^2","gravity on Earth")
gMoon = Constant(1.62,"m/s^2","gravity on Moon")
gMars = Constant(3.712,"m/s^2","gravity on Mars")
gJupiter = Constant(24.79,"m/s^2","gravity on Jupiter")
gSaturn = Constant(10.44,"m/s^2","gravity on Saturn")
gUranus = Constant(8.87,"m/s^2","gravity on Uranus")
gNeptune = Constant(11.15,"m/s^2","gravity on Neptune")
G = Constant(6.6743e-11,"m^3 kg^(-1) s^(-2)","Gravitational Constant")

massSun = Constant(1.989e30,"kg","Mass of Sun")
radiusSun = Constant(696340000,"m","Radius of Sun")
massMercury = Constant(6.39e23,"kg","Radius of Mercury")
radiusMercury = Constant(3389500,"m","Radius of Mercury")
massVenus = Constant(4.867e24,"kg","Mass of Venus")
radiusVenus = Constant(6051800,"m","Radius of Venus")
massEarth = Constant(5.972e24,"kg","Mass of Earth")
radiusEarth = Constant(6371800,"m","Radius of Earth")
massMoon = Constant(7.347e22,"kg","Mass of Moon")
radiusMoon = Constant(1737400,"m","Radius of Moon")
massMars = Constant(6.39e23,"kg","Mass of Mars")
radiusMars = Constant(3389500,"m","Radius of Mars")
massJupiter = Constant(1.898e27,"kg","Mass of Jupiter")
radiusJupiter = Constant(69911000,"m","Radius of Jupiter")
massSaturn = Constant(5.683e26,"kg","Mass of Saturn")
radiusSaturn = Constant(58232000,"m","Radius of Saturn")
massUranus = Constant(8.681e25,"kg","Mass of Sturn")
radiusUranus = Constant(25362000,"m","Radius of Uranus")
massNeptune = Constant(1.024e26,"kg","Mass of Neptune")
radiusNeptune = Constant(24622000,"m","Radius of Neptune")


class Any:
    Any = [int,float,bool,str]

class Calculus:
    def differentiate(function:str,wrt:str = "x"):
        return sympy.diff(function,sympy.Symbol(wrt))

    def integrate(function:str,wrt:str = "x"):
        return sympy.integrate(function,sympy.Symbol(wrt))

    def example_derivative():
        functions = ["x^2","cos(x)","log(x)","1","x"]
        res = {}
        for i in range(0,len(functions)):
            ans = sympy.diff(functions[i],sympy.Symbol("x"))
            res[functions[i]] = ans
        return res

    def example_integrate():
        functions = ["x^2","cos(x)","log(x)","1","x"]
        res = {}
        for i in range(0,len(functions)):
            ans = sympy.integrate(functions[i],sympy.Symbol("x"))
            res[functions[i]] = ans
        return res


class Mathematics:
    def power(base:int,exponent:int):
        return base**exponent

    def add(args:list):
        s = 0
        for i in range(0,len(args)):
            s+=args[i]
        return s

    def arithmeticProgression(start:int,step:int,length:int):
        res = []
        for i in range(0,length):
            res.append(start+i*step)
        return res

    def sumArithmeticProgression(start:int,step:int,length:int):
        return length/2*(2*start+(length-1)*step)

    def geometricProgression(start:int,ratio:int,length:int):
        res = []
        for i in range(0,length):
            res.append(start*ratio**i)
        return res

    def sumGeometricProgression(start:int,ratio:int,length:int):
        if ratio > 1:
            return start*(ratio**length-1)/(ratio-1)
        else:
            return start*(1-ratio**length)/(ratio-1)


class ModernPhysics:
    data = pd.read_csv("https://raw.githubusercontent.com/Sahil-Rajwar-2004/Datasets/main/elements.csv")
    def kinetic_energy_of_electron(Z:int,n:int):
        K = (massElectron.value*(Z**2)*(e.value**4))/(8*(epsilon0.value**2)*(h.value**2)*(n**2))
        return K

    def potential_energy_of_atom(Z:int,n:int):
        V = -(massElectron.value*Z**2*e.value**4)/(4*epsilon0.value**2*h.value**2*n**2)
        return V

    def total_energy_of_atom(Z:int,n:int):
        E = -(massElectron.value*Z**2*e.value**4)/(8*epsilon0.value**2*h.value**2*n**2)
        return E

    def freq(wave_len:int):
        f = c.value/wave_len
        return f

    def energy_of_photon(wave_len:int):
        E = h.value*c.value/wave_len
        return E

    def momentum_of_electron(Z:int,n:int):
        vel = (2.18*10**(6)*Z)/n
        return vel

    def de_Broglie_wavelength_particle(mass:int,vel:int):
        wave_len = h.value/(mass*vel)
        return wave_len

    def half_life(decay_const:int):
        t = 0.693/decay_const
        return t

    def binding_energy(element:str):
        elements = list(ModernPhysics.data["Element"].str.lower())
        protons = list(ModernPhysics.data["NumberofProtons"])
        neutrons = list(ModernPhysics.data["NumberofNeutrons"])
        atm_mass = list(ModernPhysics.data["AtomicMass"])
        pos = elements.index(element)
        return (protons[pos]*protonAmu.value+neutrons[pos]*neutronAmu.value-atm_mass[pos])*931.5

    def binding_energy_per_nucleon(element:str):
        elements = list(ModernPhysics.data["Element"].str.lower())
        protons = list(ModernPhysics.data["NumberofProtons"])
        neutrons = list(ModernPhysics.data["NumberofNeutrons"])
        atm_mass = list(ModernPhysics.data["AtomicMass"])
        pos = elements.index(element)
        return ((protons[pos]*protonAmu.value+neutrons[pos]*neutronAmu.value-atm_mass[pos])*931.5)/(protons[pos]+neutrons[pos])


class ClassicalPhysics:
    """
    mass: int
    acc: int
    """

    def force(mass:int,acc:int):
        F = mass*acc
        return F

    """
    mass: int
    d(distance): int
    """

    def gravitational_field(mass_obj1:(int|float),mass_obj2:(int|float),d:(int|float)):
        F = (G.value*mass_obj1*mass_obj2)/d**2
        return F

    def gravitational_potential(mass_obj1:(int|float),mass_obj2:(int|float),d:(int|float)):
        U = -(G.value*mass_obj1*mass_obj2)/d
        return U

    """
    gravity: int
    r(radius): int
    """

    def escape_velocity(gravity:(int|float),r:(int|float)):
        """
            The minimum velocity in which a body must have in order to escape
            the gravitational pull of a particular planet or other object.

            mass_e => mass of the body escape from
            r => distace from the center of mass 
        """
        Ve = math.sqrt(2*gravity*r)
        Ve = Ve/1000
        return Ve

    """
    mass: int
    """

    def schwarzschild_radius(m_obj:(int|float)):
        r = (2*G.value*m_obj)/c.value
        return r

    """
    r(radius): int
    f(force): int
    angle(deg): int
    """

    def torque(r:(int|float),f:(int|float),angle:(int|float)):
        deg = np.deg2rad(angle)
        tau = r*f*trigo.sin(deg)
        return tau

    """
    I(current): int
    R(Resistor): int
    """

    def ohm(I:(int|float),R:(int|float)):
        return I*R

    def work_done(F:(int|float),d:(int|float),angle:(int|float)):
        deg = np.deg2rad(angle)
        W = F*d*trigo.sin(deg)
        return W

    """
    W(watt): int
    t(time): int
    """

    def power(W:(int|float),t:(int|float)):
        return W/t

    def avg_speed(total_distance:(int|float),total_time:(int|float)):
        avg = total_distance/total_time
        return avg

    def avg_velocity(total_displacment:(int|float),total_time:(int|float)):
        avg = total_displacment/total_time
        return avg


class ProjectileMotion:
    def horizontal_range(velocity:(int|float),gravity:(int|float),angle:(int|float)):
        deg = np.deg2rad(angle)
        R = (velocity**2*trigo.sin(2*deg))/gravity
        return R

    def maximum_height(velocity:(int|float),gravity:(int|float),angle:(int|float)):
        deg = np.deg2rad(angle)
        H = (velocity**2*(trigo.sin(deg)**2))/(2*gravity)
        return H

    def time_interval(velocity:(int|float),gravity:(int|float),angle:(int|float)):
        deg = np.deg2rad(angle)
        T = (2*velocity*trigo.sin(deg))/gravity
        return T


class AlternatingCurrent:
    def irms2i(rms:(int|float)):
        i = rms*math.sqrt(2)
        return i
    
    def i2irms(current:(int|float)):
        rms = current/math.sqrt(2)
        return rms

    def vrms2v(rms:(int|float)):
        v = rms*math.sqrt(2)
        return v

    def v2vrms(volt:(int|float)):
        rms = volt/math.sqrt(2)
        return rms

    def angular_frequency(frequency:(int|float)):
        w = 2*pi.value*frequency
        return w

    def capacitance_reactance(freq:(int|float),C:(int|float)):
        Xc = 1/(2*pi.value*freq*C)
        return Xc

    def inductive_reactance(freq:(int|float),L:(int|float)):
        Xl = 2*pi.value*freq*L
        return Xl

    def impedance(Xc:(int|float),Xl:(int|float),R:(int|float)):
        Z = math.sqrt(R**2+(Xl-Xc)**2)
        return Z

    def phase(Xc:(int|float),Xl:(int|float),R:(int|float)):
        phi = trigo.arc_tan((Xc-Xl)/R)
        return phi

    def power_dissipated(v:(int|float),i:(int|float)):
        p = i**2*v
        return p

    def resonancefrequency(L:(int|float),C:(int|float)):
        f = 1/(2*pi.value*math.sqrt(L*C))
        return f

    def parallel_resonance_frequency(L:(int|float),C:(int|float),R:(int|float)):
        f = (1/(2*pi.value))*math.sqrt(1/(L*C)-(R**2/L**2))
        return f

    def qualitative_factor(R:(int|float),L:(int|float),C:(int|float)):
        Q = (1/R)*math.sqrt(L/C)
        return Q


class Algo:
    def fibonacci_series(number:int) -> int:
        seq = [0,1]
        if number <= 0:
            raise ValueError("numbe must be x > 0")
        elif number == 1:
            return seq[0]
        elif number == 2:
            return seq[1]
        else:
            for i in range(2,number):
                next_int = seq[i-1]+seq[i-2]
                seq.append(next_int)
        return seq


    def prime(lower_limit:int, upper_limit:int):
        if type(lower_limit) == type(upper_limit) == int:
            primes = []
            for i in range(lower_limit, upper_limit):
                if i == 0 or i == 1:
                    continue
                else:
                    for j in range(2, int(i/2)+1):
                        if i % j == 0:
                            break
                    else:
                        primes.append(i)
            return primes
        else:
            return "Number should be integer only"

    def sort(args:(list|np.ndarray)):
        n = len(args)
        for i in range(n):
            for j in range(0,n-i-1):
                if args[j]>args[j+1]:
                    args[j],args[j+1] = args[j+1],args[j]
        return args

    def length(args:(list|np.ndarray)):
        count = 0
        for _ in range(0,len(args)):
            count += 1
        return count

    def duplicates(nums):
        repeat = {}
        sort = sorted(nums,reverse = False)
        for i in sort:
            if sort.count(i) >= 1:
                repeat.update({i:sort.count(i)})
        return repeat
    
    def swap(x:Any,y:Any) -> Any:
        x,y = y,x
        return [x,y]


class Sort:
    def bubble_sort(array:list) -> list:
        for i in range(len(array)):
            for j in range(0,len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j],array[j+1] = array[j+1],array[j]
        return array

    def quick_sort(array:list) -> list:
        if len(array) <= 1:
            return array
        flag = array[len(array)//2]
        left = [x for x in array if x < flag]
        mid = [x for x in array if x == flag]
        right = [x for x in array if x > flag]
        return Sort.quick_sort(left)+mid+Sort.quick_sort(right)
    
    def insertion_sort(array:list) -> list:
        for i in range(1,len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        return array

    def merge_sort(array:list) -> list:
        if len(array) > 1:
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            Sort.merge_sort(left)
            Sort.merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

        return array
    
    def selection_sort(array:list) -> list:
        for i in range(len(array)):
            min_val = i
            for j in range(i+1,len(array)):
                if(array[j] < array[min_val]):
                    min_val = j
            array[i],array[min_val] = array[min_val],array[i]
        return array


class Search:
    def linear_search(array:list,target:int) -> int:
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1
    
    def binary_search(array:list,target:int) -> int:
        start = 0
        end = len(array)-1
        while start <= end:
            mid = (start+end)//2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                start = mid + 1
            elif array[mid] > target:
                end = mid - 1
        return -1


class Statistics:
    def error(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        if len(args) == len(kwargs):
            rel = []
            for i in range(0,len(args)):
                x = args[i]-kwargs[i]
                rel.append(x)
            return rel
        else:
            return "length of args and kwargs are not equal"

    def add(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        if len(args) == len(kwargs):
            res = []
            for i in range(0,len(args)):
                x = args[i]+kwargs[i]
                res.append(x)
            return res
        else:
            return "length of args and kwargs are not equal"

    def multiply(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        if len(args) == len(kwargs):
            res = []
            for i in range(0,len(args)):
                x = args[i]*kwargs[i]
                res.append(x)
            return res
        else:
            return "length of args and kwargs are not equal"

    def divide(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        if len(args) == len(kwargs):
            res = []
            for i in range(0,len(args)):
                try:
                    x = args[i]/kwargs[i]
                    res.append(x)
                except ZeroDivisionError:
                    res.append(np.inf)
            return res
        else:
            return "length of args and kwargs are not equal"

    def min_max(args:(int|float)):
        sorting = sorted(args, reverse = False)
        return [sorting[0],sorting[len(sorting)-1]]

    def count(args) -> list:
        return len(args)

    def random_sampling_list(args:(list|np.ndarray),sample=1):
        rel = []
        for _ in range(0,sample):
            random.shuffle(args)
            rel.append(args[0])
            args.remove(args[0])
        return rel

    def random_sampling_data(data:pd.core.frame.DataFrame,fraction:float):
        return data.sample(frac = fraction)

    def factorial(num:(int|float)):
        r"""
        It is the product of less than equal to n(number).
        Denoted as `n!`

        for more info: <https://www.google.com/search?q=factorial>

        ===========================
        Mathematical Representation
        ===========================
        `n! = n*(n-1)*(n-2)*...*1`
        """
        if num == 0:
            return 1
        return num*Statistics.factorial(num-1)

    def permutations(n:(int|float),r:(int|float)):
        r"""
        A technique to determines the number of possible arrangements in a set when the order of the arrangements matters.
        Denoted as `nPr` where `n` is total number of objects and `r` is selected objects for arrangements

        for more info: <https://www.google.com/search?q=permuation>

        ===========================
        Mathematical Representation
        ===========================
        `nPr = n!/(n-r)!`
        """
        return Statistics.factorial(n)/Statistics.factorial(n-r)

    def combinations(n:(int|float),r:(int|float)):
        r"""
        An arrangement of objects where the order in which the objects are selected doesn't matter.
        Denoted as 'nCr' where `n` is total number of objects in the set and `r` number of choosing objects from the set

        for more info: <https://www.google.com/search?q=combination>

        ===========================
        Mathematical Representation
        ===========================
        `nCr = n!/r!(n-r)!`
        """
        return Statistics.factorial(n)/(Statistics.factorial(r)*Statistics.factorial(n-r))

    def quartiles(args:(list|np.ndarray)):
        r"""
        In statistics, a quartile is a type of quantile which divides the number of data points into four parts, or quarters, of more-or-less equal size
        the data must be in ascending order.

        for more info: <https://www.google.com/search?q=quartiles>
        """
        rel = sorted(args,reverse = False)
        if len(args)%2 == 0:
            part = int(len(args)/2)
            rel1 = rel[0:part]
            rel2 = rel[part:len(rel)]
            Q1 = Statistics.median(rel1)
            Q2 = Statistics.median(rel)
            Q3 = Statistics.median(rel2)
            return [Q1,Q2,Q3]
        else:
            part = int(len(args)/2)
            rel1 = rel[0:part]
            rel2 = rel[part+1:len(rel)]
            Q1 = Statistics.median(rel1)
            Q2 = Statistics.median(rel)
            Q3 = Statistics.median(rel2)
            return [Q1,Q2,Q3]

    def iqr(args:(list|np.ndarray)):
        q = Statistics.quartiles(args)
        iqr = q[len(q)-1]-q[0]
        return iqr

    def outliers(args:(list|np.ndarray)):
        q = Statistics.quartiles(args)
        iqr = Statistics.iqr(args)
        args_range = [q[0]-1.5*iqr,q[len(q)-1]+1.5*iqr]
        out = []
        for i in range(0,len(args)):
            if args[i]>=args_range[0]:
                if args[i]<=args_range[1]:
                    pass
                else:
                    out.append(args[i])
            else:
                out.append(args[i])
        if out == []:
            return None
        else:
            return out

    def absolute(num:(int|float)):
        r"""
        Absolute value or Modulus Value both are functions that always gives positive number no matter what kind of integer you are giving as an input
        Denoted as `|x|`

        for more info: <https://www.google.com/search?q=absolute+value>

        ===========================
        Mathematical Representation
        ===========================
        `|x| = {x; if x >= 0, -x; if x < 0}`
        """
        if num >= 0:
            return num
        elif num < 0:
            return num*(-1)
        else:
            return "Invalid input"

    def mean(args:(list|np.ndarray)):
        r"""
        Its gives an average value form a given datasets
        Dentnoted as `x̄`

        for more info: <https://www.google.com/search?q=mean>

        ===========================
        Mathematical Representation
        ===========================
        `x̄ = sum of the data/total number of the data`
        """
        return sum(args)/len(args)

    def harmonic_mean(args:(list|np.ndarray)):
        r"""
        It is calculated by dividing the number of observations by the reciprocal of each number in the series.

        for more info: <https://www.google.com/search?q=harmonic+mean>
        """
        s = 0
        for i in range(0,len(args)):
            if args[i] != 0:
                a = 1/(args[i])
                s += a
            else:
                return "Harmonic mean is not defined for 0s vlaues"
        return len(args)/s

    def geometric_mean(args:(list|np.ndarray)):
        r"""
        The geometric mean is a mean or average, which indicates the central tendency or typical value of a set of numbers by using the product of their values

        for more info: <https://www.google.com/search?q=geometric+mean>

        ===========================
        Mathematical Representation
        ===========================
        GM1 = sqrt(ab)
        GM2 = cubert(abc)
        """
        p = 1
        for i in range(0,len(args)):
            a = args[i]
            p *= a
        return p**(1/len(args))

    def mode(args:(list|np.ndarray)):
        r"""
        It gives the number from a given set that repeats maximum times

        for more info: <https://www.google.com/search?q=mode>
        """
        return stats.mode(args)

    def range(args:(list|np.ndarray)):
        return max(args)-min(args)

    def product(args:(list|np.ndarray)):
        """
        It will multiply all the elements containing in the list
        """
        p = 1
        for i in range(0,len(args)):
            p *= args[i]
        return p

    def square_sum(args:(list|np.ndarray)):
        s = 0
        for i in range(0,len(args)):
            sq = args[i]**2
            s += sq
        return s

    def standard_deviation(args:(list|np.ndarray),kind:str = "s"):
        """
        `s = sample`
        `p = population`
        """
        mean = sum(args)/len(args)
        rep = []
        for i in range(0,len(args)):
            a = (args[i]-mean)**2
            rep.append(a)
        total = sum(rep)
        if kind == "s":
            d = len(args)-1
        elif kind == "p":
            d = len(args)
        else: 
            return f"invalid input! expected from `s` or `p` but got: {kind}"
        return math.sqrt(total/d)

    def zscore(args:(list|np.ndarray),num:int):
        m = Statistics.mean(args)
        dev = Statistics.standard_deviation(args)
        a = num-m
        return a/dev

    def median(args:(list|np.ndarray)):
        rel = sorted(args, reverse = False)
        if len(rel)%2 == 0:
            mid1 = int(len(rel)/2)
            mid2 = mid1-1
            return (rel[mid1]+rel[mid2])/2
        else:
            mid = int(len(rel)/2)
            return rel[mid]

    def mean_deviation(args:(list|np.ndarray)):
        mean = sum(args)/len(args)
        rep = []
        for i in range(0,len(args)):
            a = abs(args[i]-mean)
            rep.append(a)
        total = sum(rep)
        return total/len(args)

    def percentile(args:(list|np.ndarray),n:int):
        if n in args:
            b = 0
            for i in range(0,len(args)):
                if n > args[i]:
                    b += 1
            return (b/len(args))*100
        else:
            return f"Unexpected Input! {n} is not in {args}!"

    def median_avg_deviation(args:(list|np.ndarray)):
        m = sum(args)/len(args)
        rel = []    
        for i in range(0,len(args)):
            a = abs(args[i]-m)
            rel.append(a)
        mid = Statistics.median(rel)
        return mid

    def cum_sum(args:(list|np.ndarray)):
        s = 0
        cumsum = []
        for i in range(0,len(args)):
            s += args[i]
            cumsum.append(s)
        return cumsum

    def variance(args:(list|np.ndarray),kind:str = "s"):
        mean = sum(args)/len(args)
        rep = []
        for i in range(0,len(args)):
            a = (args[i]-mean)**2
            rep.append(a)
        total = sum(rep)
        if kind == "s":
            d = len(args)-1
        elif kind == "p":
            d = len(args)
        else:
            return f"invalid input! expected from `s` or `p` but got: {kind}"
        return total/d

    def root_mean_squared(args:(list|np.ndarray)):
        rep = []
        for i in range(0,len(args)):
            a = args[i]**2
            rep.append(a)
        total = sum(rep)
        return math.sqrt(total/len(args))

    def lr(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        r"""
        genral equation of a line `y = mx+b`
        >>> from chemaphy import Statistics
        >>> x = [33, 68, 21, 46, 88, 45, 27, 6, 81, 74]
        >>> y = [32, 68, 21, 46, 88, 45, 27, 5, 81, 74]
        >>> print(Statistics.LR(x,y))
        >>> [1.0084861955000073, -0.6149749599503529]
        [slope,intercept]
        """
        if len(args) == len(kwargs):
            x,y,xy,x2 = sum(args),sum(kwargs),0,0
            for i in range(0,len(args)):
                a = args[i]**2
                b = args[i]*kwargs[i]
                xy += b
                x2 += a
            N1 = y*x2-x*xy
            D1 = len(args)*x2-x**2
            intercept = N1/D1
            N2 = len(args)*xy-x*y
            D2 = len(args)*x2-x**2
            slope = N2/D2
            return [slope,intercept]
        else:
            return "Length of actual and predicted values should be equal"

    def standard_error(args:(list|np.ndarray)):
        dev = Statistics.standard_deviation(args)
        return dev/math.sqrt(len(args))

    def relative_frequency(args:(list|np.ndarray)):
        rel,freq = [],{}
        for item in args:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
            f = list(freq.values())
            for i in range(0,len(f)):
                r = f[i]/len(args)
                rel.append(r)
        return [freq,rel]

    def moving_avg(array:(list|np.ndarray),steps:int):
        r"""
        A moving average is a calculation to analyze data points by creating a series of averages of different subsets of the full data set.
        By Default size will be 2 or you may change the value of size

        for more info: <https://www.google.com/search?q=running+mean>
        """
        if steps <= 0:
            raise ValueError("Steps should be greater than the 0!")
        if len(array) < steps:
            raise ValueError("array must have at least as many elements as the number of steps!")
        moving_avg = []
        for i in range(steps,len(array)+1):
            win = array[i-steps:i]
            avg = round(sum(win)/steps,3)
            moving_avg.append(avg)
        return moving_avg

    def exp_moving_avg(array:(list|np.ndarray),alpha:float):
        if alpha <= 0 or alpha > 1:
            raise ValueError("smoothing factor alpha must be between 0 and 1!")
        ema = [array[0]]
        for i in range(1,len(array)):
            ema.append(round(alpha*array[i]+(1-alpha)*ema[-1],3))
        return ema

    def correlation_coefficient(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        if len(args) == len(kwargs):
            x,y,xy,x2,y2 = sum(args),sum(kwargs),0,0,0
            for i in range(0,len(args)):
                a = args[i]**2
                b = args[i]*kwargs[i]
                c = kwargs[i]**2
                x2 += a
                xy += b
                y2 += c
            N = len(args)*xy-x*y
            D = math.sqrt((len(args)*x2-x**2)*(len(args)*y2-y**2))
            return N/D
        else:
            return "Length of actual and predicted values should be equal"

    def coefficient_determination(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
        if len(args) == len(kwargs):
            x,y,x2,y2,xy = sum(args),sum(kwargs),0,0,0
            for i in range(0,len(args)):
                a = args[i]**2
                b = args[i]*kwargs[i]
                c = kwargs[i]**2
                x2 += a
                y2 += c
                xy += b
            N = len(args)*xy-x*y
            D = math.sqrt((len(args)*x2-x**2)*(len(args)*y2-y**2))
            return N/D
        else:
            return "Length of actual and predicted values should be equal"

    def mean_squared_error(actual:(list|np.ndarray),predicted:(list|np.ndarray)):
        r"""
        The measure of how close a fitted line is to data points. For every data point,
        you take the distance vertically from the point to the corresponding y value on the curve fit (the error),
        and square the value\n

        for more info: <https://www.google.com/search?q=mean+squared+error>

        ===========================
        Mathematical Representation
        ===========================
        `(1/n)/summation((observed-predicted)^2)`

        `n` number of data points
        `observed` oberserved data points
        `predicted` predicte data points
        """
        if len(actual) == len(predicted):
            errors = []
            for i in range(0,len(actual)):
                a = (actual[i]-predicted[i])**2
                errors.append(a)
            return sum(errors)/len(actual)
        else:
            return "Length of actual and predicted values should be equal"

    def root_mean_squared_error(actual:(list|np.ndarray),predicted:(list|np.ndarray)):
        if len(actual) == len(predicted):
            return math.sqrt(Statistics.mean_squared_error(actual,predicted))
        else:
            return "Length of actual and predicted values should be equal"

    def cost_function(actual:(list|np.ndarray), predicted:(list|np.ndarray)):
        if len(actual) == len(predicted):
            errors = []
            for i in range(0,len(actual)):
                a = (actual[i]-predicted[i])**2
                errors.append(a)
            return sum(errors)/(2*len(actual))
        else:
            return "Length of actual and predicted values should be equal"

    def mean_absolute_error(actual:(list|np.ndarray),predicted:(list|np.ndarray)):
        if len(actual) == len(predicted):
            errors = []
            for i in range(0,len(actual)):
                a = Statistics.Absolute(actual[i]-predicted[i])
                errors.append(a)
            return sum(errors)/len(actual)
        else:
            return "Length of actual and predicted values should be equal"

    def mean_error(actual:(list|np.ndarray),predicted:(list|np.ndarray)):
        if len(actual) == len(predicted):
            errors = []
            for i in range(0,len(actual)):
                x = actual[i] - predicted[i]
                errors.append(x)
            return Statistics.Mean(errors)
        else:
            return "Length of actual and predicted values should be equal"

    def accuracy(actual:(list|np.ndarray),predicted:(list|np.ndarray)):
        if len(actual) == len(predicted):
            rel_actual,rel_predicted,score = [],[],0
            for i in range(0,len(actual)):
                rel_actual.append(round(actual[i],0))
                rel_predicted.append(round(predicted[i],0))
            for j in range(0,len(actual)):
                if rel_actual[j] == rel_predicted[j]:
                    score += 1
            return score/len(actual)
        else:
            return "Length of actual and predicted values should be equal"

    def intercept(x:(list|np.ndarray),y:(list|np.ndarray)):
        r"""
        genral equation of line is represented by `y = mx+b` where
        `m` is slope of a line while
        `b` is the intercept of a line at an axis

        example: `y = 3x+2`
        `m = 3` and `b = 2`
        graph -> "https://github.com/Sahil-Rajwar-2004/Samples/blob/main/graph.PNG"
        """
        if len(x) == len(y):
            X,Y,XY,X2 = 0,0,0,0
            for i in range(0,len(x)):
                Y += y[i]
                X += x[i]
                XY += (x[i]*y[i])
                X2 += x[i]**2
            N = Y*X2-X*XY
            D = len(x)*X2-X**2
        return N/D

    def slope(x:(list|np.ndarray),y:(list|np.ndarray)):
        if len(x) == len(y):
            X,Y,XY,X2 = 0,0,0,0
            for i in range(0,len(x)):
                Y += y[i]
                X += x[i]
                XY += x[i]*y[i]
                X2 += x[i]**2
            N = len(x)*XY-X*Y
            D = len(x)*X2-X**2
        return N/D

    def confusion_matrix(actual:np.ndarray,predicted:np.ndarray):
        if len(actual) == len(predicted):
            y_true = np.array(actual)
            y_pred = np.array(predicted)
            n_classes = np.max([y_true,y_pred])+1
            y_true_onehot = np.eye(n_classes)[y_true]
            y_pred_onehot = np.eye(n_classes)[y_pred]
            conf_matrix = np.dot(y_true_onehot.T,y_pred_onehot)
            return conf_matrix
        else:
            return "actual and predicted size should be equal"
        return "An Error Occured!"


class LoadData:
    def load_data(file:str,ext:str = "csv"):
        try:
            if file.lower() != "student_mat":
                return pd.read_csv(f"https://raw.githubusercontent.com/Sahil-Rajwar-2004/Datasets/main/{file}.{ext}")
            else:
                return pd.read_csv(f"https://raw.githubusercontent.com/Sahil-Rajwar-2004/Datasets/main/{file}.{ext}",sep = ";")
        except HTTPError as error:
            return f"{error} | {file}.{ext} not found! | try to change the extension .{ext} or filename"

    def data_name():
        return ["amazon",
                "apple",
                "binance_coin",
                "bitcoin",
                "breast_cancer",
                "colgate",
                "cwg_players_participated",
                "cwg_players_won_medal",
                "doge_coin",
                "ds_salaries",
                "elements",
                "employees_info",
                "ethereum_coin",
                "google",
                "iris",
                "meta",
                "microsoft",
                "music",
                "netflix",
                "programming_lang_data",
                "quikr_cars",
                "student_mat",
                "tesla",
                "tic_tac_toe",
                "tips",
                "trumiles",
                "weather",
                "weight_height",
                "winequality-red"]


class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)


class HashList:
    rel = []
    def add(key,value):
        x = []
        x.append(key)
        x.append(value)
        HashList.rel.append(x)
        x = []

    def remove(_value=None,_index:int=None):
        if _value is not None and _index is not None:
            return "can't use _value and _index at the same time"
        elif _value is not None:
            if _value in HashList.rel:
                HashList.rel.remove(_value)
            else:
                return f"{_value} not found in HashList"
        elif _index is not None:
            if _index in HashList.rel:
                HashList.rel.remove(HashList.rel[_index])
            else:
                return f"{_index} value not found in HashList"

    def show():
        return HashList.rel

    def delete():
        HashList.rel = []


class BinaryConverter:
    def str2binary(args) -> str:
        l = []
        words = list(args)
        print(words)
        for i in range(0,len(words)):
            to_num = ord(words[i])
            to_bin = int(bin(to_num)[2:])
            l.append(to_bin)
        return l

    def str2hexadecimal(args) -> str:
        l = []
        words = list(args)
        print(words)
        for j in range(0,len(words)):
            to_num = ord(words[j])
            to_bin = hex(to_num)[2:]
            l.append(to_bin)
        return l

    def str2octadecimal(args) -> str:
        l = []
        words = list(args)
        print(words)
        for k in range(0,len(words)):
            to_num = ord(words[k])
            to_bin = int(oct(to_num)[2:])
            l.append(to_bin)
        return l

    def int2binary(args) -> (list|int):
        if type(args) == list:
            b = []
            for i in range(0,len(args)):
                item = bin(args[i])
                b.append(item[2:])
            return b
        elif type(args) == int:
            return bin(args)[2:]
        else:
            return "argument should be integer or list"

    def int2hexadecimal(args) -> (list|int):
        if type(args) == list:
            h = []
            for j in range(0,len(args)):
                item = hex(args[j])
                h.append(item[2:])
            return h
        elif type(args) == int:
            return hex(args)[2:]
        else:
            return "argument should be integer or list"

    def int2octadecimal(args) -> (list|int):
        if type(args) == list:
            o = []
            for k in range(0,len(args)):
                item = oct(args[k])
                o.append(item[2:])
            return o
        elif type(args) == int:
            return oct(args)[2:]
        else:
            return "argument should be integer or list"


class Length:
    def km2cm(km:(int|float)):
        return km*1e5

    def km2m(km:(int|float)):
        return km*1e3

    def km2mm(km:(int|float)):
        return km*1e6

    def km2um(km:(int|float)):
        return km*1e9

    def km2nm(km:(int|float)):
        return km*1e12

    def km2miles(km:(int|float)):
        return km/1.609

    def km2yard(km:(int|float)):
        return km*1093.61

    def km2ft(km:(int|float)):
        return km*3280.84

    def km2inch(km:(int|float)):
        return km*39370.1
    
    def km2nautical_miles(km:(int|float)):
        return km/1.852

    def m2km(m:(int|float)):
        return m/1e3

    def m2cm(m:(int|float)):
        return m*1e2
    
    def m2mm(m:(int|float)):
        return m*1e3

    def m2um(m:(int|float)):
        return m*1e6

    def m2nm(m:(int|float)):
        return m*1e9

    def m2miles(m:(int|float)):
        return m/1609

    def m2yard(m:(int|float)):
        return m*1.094

    def m2ft(m:(int|float)):
        return m*3.281

    def m2inch(m:(int|float)):
        return m*39.37

    def m2nautical_miles(m:(int|float)):
        return m/1852

    def cm2km(cm:(int|float)):
        return cm*1e-5

    def cm2m(cm:(int|float)):
        return cm*1e2

    def cm2mm(cm:(int|float)):
        return cm*1e0

    def cm2um(cm:(int|float)):
        return cm*1e4

    def cm2nm(cm:(int|float)):
        return cm*1e7

    def cm2miles(cm:(int|float)):
        return cm/160900

    def cm2yard(cm:(int|float)):
        return cm/91.44

    def cm2ft(cm:(int|float)):
        return cm/30.48

    def cm2inch(cm:(int|float)):
        return cm/2.54

    def cm2nautical_miles(cm:(int|float)):
        return cm*1e-5

    def mm2km(mm:(int|float)):
        return mm/1e6

    def mm2m(mm:(int|float)):
        return mm/1e3

    def mm2cm(mm:(int|float)):
        return mm/1e0

    def mm2um(mm:(int|float)):
        return mm/1e3

    def mm2nm(mm:(int|float)):
        return mm*1e6

    def mm2km(mm:(int|float)):
        return mm/1e6

    def mm2miles(mm:(int|float)):
        return mm/1.609e6

    def mm2yard(mm:(int|float)):
        return mm/914.4

    def mm2ft(mm:(int|float)):
        return mm/304.8

    def mm2inch(mm:(int|float)):
        return mm/25.4

    def mm2km(mm:(int|float)):
        return mm/1.852e6

    def um2km(um:(int|float)):
        return um/1e9

    def um2m(um:(int|float)):
        return um/1e6

    def um2cm(um:(int|float)):
        return um/1e4

    def um2mm(um:(int|float)):
        return um/1e3

    def um2nm(um:(int|float)):
        return um*1e3

    def um2miles(um:(int|float)):
        return um/1.609e9

    def um2yard(um:(int|float)):
        return um/914400

    def um2ft(um:(int|float)):
        return um/304800

    def um2inch(um:(int|float)):
        return um/25400

    def um2nautical_miles(um:(int|float)):
        return um/1.852e9

    def nm2km(nm:(int|float)):
        return nm/1e12

    def nm2m(nm:(int|float)):
        return nm/1e9

    def nm2cm(nm:(int|float)):
        return nm/1e7

    def nm2mm(nm:(int|float)):
        return nm/1e6

    def nm2um(nm:(int|float)):
        return nm/1e3

    def nm2miles(nm:(int|float)):
        return nm/1.609e12

    def nm2yard(nm:(int|float)):
        return nm/9.144e8

    def nm2ft(nm:(int|float)):
        return nm/3.048e8

    def nm2inch(nm:(int|float)):
        return nm/2.54e7

    def nm2nuatical_miles(nm:(int|float)):
        return nm/1.852e12

    def miles2km(miles:(int|float)):
        return miles*1.609

    def miles2m(miles:(int|float)):
        return miles*1609

    def miles2cm(miles:(int|float)):
        return miles*160900

    def miles2mm(miles:(int|float)):
        return miles*1.609e6

    def miles2um(miles:(int|float)):
        return miles*1.609e9

    def miles2nm(miles:(int|float)):
        return miles*1.609e12

    def miles2yard(miles:(int|float)):
        return miles*1760

    def miles2ft(miles:(int|float)):
        return miles*5280

    def miles2inch(miles:(int|float)):
        return miles*63360

    def miles2nautical_miles(miles:(int|float)):
        return miles/1.151

    def yard2km(yard:(int|float)):
        return yard/1094

    def yard2m(yard:(int|float)):
        return yard/1.094
    
    def yard2cm(yard:(int|float)):
        return yard/10.94

    def yard2mm(yard:(int|float)):
        return yard/109.4

    def yard2um(yard:(int|float)):
        return yard*914400

    def yard2nm(yard:(int|float)):
        return yard*9.144e8

    def yard2miles(yard:(int|float)):
        return yard/1760

    def yard2ft(yard:(int|float)):
        return yard*3

    def yard2inch(yard:(int|float)):
        return yard*36

    def yard2nautical_miles(yard:(int|float)):
        return yard/2025

    def ft2km(ft:(int|float)):
        return ft/3281

    def ft2m(ft:(int|float)):
        return ft/3.281

    def ft2cm(ft:(int|float)):
        return ft*30.48

    def ft2mm(ft:(int|float)):
        return ft*304.8

    def ft2um(ft:(int|float)):
        return ft*304800

    def ft2nm(ft:(int|float)):
        return ft*3.048e8

    def ft2miles(ft:(int|float)):
        return ft/5280

    def ft2yard(ft:(int|float)):
        return ft/3

    def ft2inch(ft:(int|float)):
        return ft*12

    def ft2nautical_miles(ft:(int|float)):
        return ft/6076

    def inch2km(inch:(int|float)):
        return inch/39370

    def inch2m(inch:(int|float)):
        return inch/39.37

    def inch2cm(inch:(int|float)):
        return inch*2.54

    def inch2mm(inch:(int|float)):
        return inch*25.4

    def inch2um(inch:(int|float)):
        return inch*25400

    def inch2nm(inch:(int|float)):
        return inch*2.54e7

    def inch2miles(inch:(int|float)):
        return inch/63360

    def inch2yard(inch:(int|float)):
        return inch/36

    def inch2ft(inch:(int|float)):
        return inch/12

    def inch2nautical_miles(inch:(int|float)):
        return inch/72910

    def nautical_miles2km(nautical_miles:(int|float)):
        return nautical_miles*1.852
    
    def nautical_miles2m(nautical_miles:(int|float)):
        return nautical_miles*1852

    def nautical_miles2cm(nautical_miles:(int|float)):
        return nautical_miles*185200

    def nautical_miles2mm(nautical_miles:(int|float)):
        return nautical_miles*1.852e6

    def nautical_miles2um(nautical_miles:(int|float)):
        return nautical_miles*1.852e9

    def nautical_miles2nm(nautical_miles:(int|float)):
        return nautical_miles*1.852e12

    def nautical_miles2miles(nautical_miles:(int|float)):
        return nautical_miles*1.151

    def nautical_miles2yard(nautical_miles:(int|float)):
        return nautical_miles*2025

    def nautical_miles2ft(nautical_miles:(int|float)):
        return nautical_miles*6076

    def nautical_miles2inch(nautical_miles:(int|float)):
        return nautical_miles*72910


class Pressure:
    def bar2pascal(bar:(int|float)):
        return bar*1e5

    def bar2psi(bar:(int|float)):
        return bar*14.504

    def bar2atm(bar:(int|float)):
        return bar/1.013

    def bar2torr(bar:(int|float)):
        return bar*750.1

    def pascal2bar(pascal:(int|float)):
        return pascal/1e5

    def pascal2psi(pascal:(int|float)):
        return pascal/6895

    def pascal2atm(pascal:(int|float)):
        return pascal/101300

    def pascal2torr(pascal:(int|float)):
        return pascal*133.3

    def psi2bar(psi:(int|float)):
        return psi/14.504

    def psi2pascal(psi:(int|float)):
        return psi*6895

    def psi2atm(psi:(int|float)):
        return psi/14.696

    def psi2torr(psi:(int|float)):
        return psi*51.715

    def atm2bar(atm:(int|float)):
        return atm*1.013

    def atm2pascal(atm:(int|float)):
        return atm*101300

    def atm2psi(atm:(int|float)):
        return atm*14.696

    def atm2torr(atm:(int|float)):
        return atm*760

    def torr2bar(torr:(int|float)):
        return torr/750.1

    def torr2pascal(torr:(int|float)):
        return torr*133.3

    def torr2psi(torr:(int|float)):
        return torr/51.715

    def torr2atm(torr:(int|float)):
        return torr/760


class Angle:
    def deg2rad(deg:(int|float)):
        return deg*math.pi/180

    def deg2grad(deg:(int|float)):
        return deg*200/180

    def deg2mili_rad(deg:(int|float)):
        return deg*1000*math.pi/180

    def deg2min_arc(deg:(int|float)):
        return deg*60

    def deg2sec_arc(deg:(int|float)):
        return deg*3600

    def rad2deg(rad:(int|float)):
        return rad*180/math.pi

    def rad2grad(rad:(int|float)):
        return rad*200/math.pi

    def rad2mili_rad(rad:(int|float)):
        return rad*1000

    def rad2min_arc(rad:(int|float)):
        return rad*10800/math.pi

    def rad2sec_arc(rad:(int|float)):
        return rad*648000/math.pi

    def grad2deg(grad:(int|float)):
        return grad*180/200

    def grad2rad(grad:(int|float)):
        return grad*math.pi/200

    def grad2mili_rad(grad:(int|float)):
        return grad*1000*math.pi/200

    def grad2min_arc(grad:(int|float)):
        return grad*54

    def grad2sec_arc(grad:(int|float)):
        return grad*3240

    def mili_rad2deg(mili_rad:(int|float)):
        return mili_rad*180/math.pi*1000

    def mili_rad2rad(mili_rad:(int|float)):
        return mili_rad/1000

    def mili_grad(mili_rad:(int|float)):
        return mili_rad*200/1000*math.pi

    def mili_rad2min_arc(mili_rad:(int|float)):
        return mili_rad*10800/1000*math.pi

    def mili_rad2sec_arc(mili_rad:(int|float)):
        return mili_rad*648000/1000*math.pi

    def min_arc2deg(min_arc:(int|float)):
        return min_arc/60

    def min_arc2rad(min_arc:(int|float)):
        return min_arc*math.pi/10800

    def min_arc2grad(min_arc:(int|float)):
        return min_arc/54

    def min_arc2mili_rad(min_arc:(int|float)):
        return min_arc*1000*math.pi/10800

    def min_arc2sec_arc(min_arc:(int|float)):
        return min_arc*60

    def sec_arc2deg(sec_arc:(int|float)):
        return sec_arc/3600

    def sec_arc2rad(sec_arc:(int|float)):
        return sec_arc*math.pi/648000

    def sec_arc2grad(sec_arc:(int|float)):
        return sec_arc/3240

    def sec_arc2mili_rad(sec_arc:(int|float)):
        return sec_arc*1000*math.pi/648000

    def sec_arc2min_arc(sec_arc:(int|float)):
        return sec_arc/60


class Time:
    def nanoseconds2microseconds(nsec:(int|float)):
        return nsec/1e3

    def nanoseconds2miliseconds(nsec:(int|float)):
        return nsec/1e6

    def nanoseconds2seconds(nsec:(int|float)):
        return nsec/1e9

    def nanoseconds2minutes(nsec:(int|float)):
        return nsec/6e10

    def nanoseconds2hours(nsec:(int|float)):
        return nsec/3.6e12

    def nanoseconds2days(nsec:(int|float)):
        return nsec/8.64e13

    def nanoseconds2weeks(nsec:(int|float)):
        return nsec/6.048e14

    def nanoseconds2months(nsec:(int|float)):
        return nsec/2.628e15

    def nanoseconds2years(nsec:(int|float)):
        return nsec/3.154e16

    def nanoseconds2decades(nsec:(int|float)):
        return nsec/3.154e17

    def nanoseconds2century(nsec:(int|float)):
        return nsec/3.154e18

    def microseconds2nanoseconds(usec:(int|float)):
        return usec*1e3

    def microseconds2miliseconds(usec:(int|float)):
        return usec/1e3

    def microseconds2seconds(usec:(int|float)):
        return usec/1e6

    def microseconds2minutes(usec:(int|float)):
        return usec/6e7

    def microseconds2hours(usec:(int|float)):
        return usec/3.6e9

    def microseconds2days(usec:(int|float)):
        return usec/8.64e10

    def microseconds2weeks(usec:(int|float)):
        return usec/6.048e11

    def microseconds2months(usec:(int|float)):
        return usec/2.628e12

    def microseconds2years(usec:(int|float)):
        return usec/3.154e13

    def microseconds2decades(usec:(int|float)):
        return usec/3.154e14

    def microseconds2century(usec:(int|float)):
        return usec/3.154e15

    def miliseconds2nanoseconds(msec:(int|float)):
        return msec*1e6

    def miliseconds2microseconds(msec:(int|float)):
        return msec*1e3

    def miliseconds2seconds(msec:(int|float)):
        return msec/1e3

    def miliseconds2minutes(msec:(int|float)):
        return msec/6e4

    def miliseconds2hours(msec:(int|float)):
        return msec/3.6e6

    def miliseconds2days(msec:(int|float)):
        return msec/8.64e7

    def miliseconds2weeks(msec:(int|float)):
        return msec/6.048e8

    def miliseconds2months(msec:(int|float)):
        return msec/2.628e9

    def miliseconds2years(msec:(int|float)):
        return msec/3.154e10

    def miliseconds2decades(msec:(int|float)):
        return msec/3.154e11

    def miliseconds2century(msec:(int|float)):
        return msec/3.154e12

    def seconds2nanoseconds(sec:(int|float)):
        return sec*1e9

    def seconds2microseconds(sec:(int|float)):
        return sec*1e6
    
    def seconds2miliseconds(sec:(int|float)):
        return sec*1e3

    def seconds2minuntes(sec:(int|float)):
        return sec/60

    def seconds2hours(sec:(int|float)):
        return sec/3600

    def seconds2days(sec:(int|float)):
        return sec/86400

    def seconds2weeks(sec:(int|float)):
        return sec/604800

    def seconds2months(sec:(int|float)):
        return sec/2.628e6

    def seconds2years(sec:(int|float)):
        return sec/3.154e7

    def seconds2decade(sec:(int|float)):
        return sec/3.154e8

    def seconds2century(sec:(int|float)):
        return sec/3.154e9

    def minutes2nanoseconds(min:(int|float)):
        return min*6e10

    def minutes2microseconds(min:(int|float)):
        return min*6e7

    def minutes2miliseconds(min:(int|float)):
        return min*6e4

    def minutes2seconds(min:(int|float)):
        return min*60

    def minutes2hours(min:(int|float)):
        return min/60

    def minutes2days(min:(int|float)):
        return min/1440

    def minutes2weeks(min:(int|float)):
        return min/10080

    def minutes2months(min:(int|float)):
        return min/43800

    def minutes2years(min:(int|float)):
        return min/525600

    def minutes2decade(min:(int|float)):
        return min/5.256e6

    def minutes2century(min:(int|float)):
        return min/5.256e7

    def hours2nanoseconds(hr:(int|float)):
        return hr*3.6e12

    def hours2microseconds(hr:(int|float)):
        return hr*3.6e9

    def hours2miliseconds(hr:(int|float)):
        return hr*3.6e6

    def hours2seconds(hr:(int|float)):
        return hr*3600

    def hours2hours(hr:(int|float)):
        return hr*60

    def hours2days(hr:(int|float)):
        return hr/24

    def hours2weeks(hr:(int|float)):
        return hr/168

    def hours2months(hr:(int|float)):
        return hr/730

    def hours2years(hr:(int|float)):
        return hr/8760

    def hours2decades(hr:(int|float)):
        return hr/87600

    def hours2century(hr:(int|float)):
        return hr/876000

    def days2nanoseconds(days:(int|float)):
        return days*8.63e13

    def days2microseconds(days:(int|float)):
        return days*8.63e10

    def days2miliseconds(days:(int|float)):
        return days*8.63e7

    def days2seconds(days:(int|float)):
        return days*86400

    def days2minutes(days:(int|float)):
        return days*1440

    def days2hours(days:(int|float)):
        return days*24

    def days2weeks(days:(int|float)):
        return days/7

    def days2months(days:(int|float)):
        return days/30.417

    def days2years(days:(int|float)):
        return days/365

    def days2decades(days:(int|float)):
        return days*3650

    def days2century(days:(int|float)):
        return days*36500

    def weeks2nanoseconds(weeks:(int|float)):
        return weeks*6.048e14

    def weeks2microseconds(weeks:(int|float)):
        return weeks*6.048e11

    def weeks2miliseconds(weeks:(int|float)):
        return weeks*6.048e8

    def weeks2seconds(weeks:(int|float)):
        return weeks*604800

    def weeks2minutes(weeks:(int|float)):
        return weeks*10080

    def weeks2hours(weeks:(int|float)):
        return weeks*168

    def weeks2days(weeks:(int|float)):
        return weeks*7

    def weeks2months(weeks:(int|float)):
        return weeks/4.345

    def weeks2years(weeks:(int|float)):
        return weeks/52.143

    def weeks2decades(weeks:(int|float)):
        return weeks/521.4

    def weeks2century(weeks:(int|float)):
        return weeks/5214

    def months2nanoseconds(months:(int|float)):
        return months*2.628e15

    def months2microseconds(months:(int|float)):
        return months*2.628e12

    def months2miliseconds(months:(int|float)):
        return months*2.628e9
    
    def months2seconds(months:(int|float)):
        return months*2.628e6

    def months2minutes(months:(int|float)):
        return months*43800

    def months2hours(months:(int|float)):
        return months*730

    def months2days(months:(int|float)):
        return months*30.417

    def months2weeks(months:(int|float)):
        return months*4.345

    def months2years(months:(int|float)):
        return months/12

    def months2decades(months:(int|float)):
        return months/120

    def months2century(months:(int|float)):
        return months/1200

    def years2nanoseconds(yrs:(int|float)):
        return yrs*3.154e16

    def years2microseconds(yrs:(int|float)):
        return yrs*3.154e13

    def years2miliseconds(yrs:(int|float)):
        return yrs*3.154e10

    def years2seconds(yrs:(int|float)):
        return yrs*3.154e7

    def years2minutes(yrs:(int|float)):
        return yrs*525600

    def years2hours(yrs:(int|float)):
        return yrs*8760

    def years2days(yrs:(int|float)):
        return yrs*365

    def years2weeks(yrs:(int|float)):
        return yrs*52.143

    def years2months(yrs:(int|float)):
        return yrs*12

    def years2decades(yrs:(int|float)):
        return yrs/10

    def years2century(yrs:(int|float)):
        return yrs/100

    def decades2nanoseconds(decades:(int|float)):
        return decades*3.154e17

    def decades2microseconds(decades:(int|float)):
        return decades*3.154e14

    def decades2miliseconds(decades:(int|float)):
        return decades*3.154e11

    def decades2seconds(decades:(int|float)):
        return decades*3.154e8

    def decades2minutes(decades:(int|float)):
        return decades*5.256e6

    def decades2hours(decades:(int|float)):
        return decades*87600

    def decades2days(decades:(int|float)):
        return decades*3650

    def decades2weeks(decades:(int|float)):
        return decades*521.4

    def decades2months(decades:(int|float)):
        return decades*120

    def decades2years(decades:(int|float)):
        return decades*10

    def decades2century(decades:(int|float)):
        return decades/10
    
    def century2nanoseconds(century:(int|float)):
        return century*3.154e18

    def century2microseconds(century:(int|float)):
        return century*3.154e15

    def century2miliseconds(century:(int|float)):
        return century*3.154e12

    def century2seconds(century:(int|float)):
        return century*3.154e9

    def century2minutes(century:(int|float)):
        return century*5.256e7

    def century2hours(century:(int|float)):
        return century*876000

    def century2days(century:(int|float)):
        return century*36500

    def century2weeks(century:(int|float)):
        return century*5214

    def century2months(century:(int|float)):
        return century*1200

    def century2years(century:(int|float)):
        return century*100

    def century2decades(century:(int|float)):
        return century*10


class Temperature:
    def c2k(celcius:(int|float)):
        if celcius >= -273.15 and celcius <= 1.417e32:
            k = celcius+273.15
            return k
        else:
            raise ValueError("Temperature below -273.15 and above 1.417*10^32 Celcius is not possible")

    def c2f(celcius:(int|float)):
        if celcius >= -273.15 and celcius <= 1.417e32:
            f = round((celcius*1.8)+32,2)
            return f
        else:
            raise ValueError("Temperature below -273.15 and above 1.417*10^32 celcius is not possible")

    def k2c(kelvin:(int|float)):
        if kelvin >= 0 and kelvin <= 1.417e32:
            c = kelvin-273.15
            return c
        else:
            raise ValueError("Temperature below 0 and above 1.417*10^32 kelvin is not possible")

    def k2f(kelvin:(int|float)):
        if kelvin >= 0 and kelvin <= 1.417e32:
            f = ((kelvin-273.15)*1.8)+32
            return f
        else:
            raise ValueError("Temperature below 0 and above 1.417*10^32 kelvin is not possible")

    def f2c(fahrenheit:(int|float)):
        if fahrenheit >= -459.67 and fahrenheit <= 2.55e32:
            c = round((fahrenheit-32)*0.55,2)
            return c
        else:
            raise ValueError("Temperature below -459.67 and above 2.55*10^(32) fahrenheit is not possible")

    def f2k(fahrenheit:(int|float)):
        if fahrenheit >= -459.67 and fahrenheit <= 2.55e32:
            k = ((fahrenheit-32)*5/9)+273.15
            return k
        else:
            raise ValueError("Temperature below -459.67 and above 2.55*10^(32) fahrenheit is not possible")


class DistanceFormula:
    def Distance2d(x1:(int|float),x2:(int|float),y1:(int|float),y2:(int|float)):
        d = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return d

    def Distance3d(x1:(int|float),x2:(int|float),y1:(int|float),y2:(int|float),z1:(int|float),z2:(int|float)):
        d = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
        return d


class SectionFormula:
    def intSection2d(x1:(int|float),x2:(int|float),y1:(int|float),y2:(int|float),m:(int|float),n:(int|float)):
        x = x2*m+x1*n
        y = y2*m+y*n
        ratio = m+n
        return [x/ratio,y/ratio]

    def intSection3d(x1:(int|float),x2:(int|float),y1:(int|float),y2:(int|float),z1:(int|float),z2:(int|float),m:(int|float),n:(int|float)):
        x = x2*m+x1*n
        y = y2*m+y1*n
        z = z2*m+z1*n
        ratio = m+n
        return [x/ratio,y/ratio,z/ratio]

    def extSection2d(x1:(int|float),x2:(int|float),y1:(int|float),y2:(int|float),n:(int|float),m:(int|float)):
        x = x2*m-x1*n
        y = y2*m-y1*n
        ratio = m-n
        return [x/ratio,y/ratio]

    def extSection3d(x1:(int|float),x2:(int|float),y1:(int|float),y2:(int|float),z1:(int|float),z2:(int|float),m:(int|float),n:(int|float)):
        x = x2*m-x1*n
        y = y2*m-y1*n
        z = z2*m-z1*n
        ratio = m-n
        return [x/ratio,y/ratio,z/ratio]


class Area:
    def Circle(radius:(int|float)):
        return pi.value*radius**2

    def Square(sides:(int|float)):
        return sides**2

    def Rhombus(diagonal_1,diagonal_2:(int|float)):
        return diagonal_1*diagonal_2*0.5

    def Reactangle(length,breadth:(int|float)):
        return length*breadth

    def Parallelogram(length,breadth:(int|float)):
        return length*breadth

    def Triangle(height,base:(int|float)):
        return 0.5*height*base

    def Equilateral_triangle(side:(int|float)):
        deg = np.deg2rad(60)
        return 0.5*trigo.sin(deg)*side**2

    def Ellipse(a,b:(int|float)):
        return pi.value*a*b

    def Trapezium(a,b,height:(int|float)):
        return ((a+b)*0.5)*height

    def Sector(angle,radius:(int|float)):
        return (angle/360)*pi.value*radius**2
    

class Perimeter:
    def Circle(radius:(int|float)):
        return 2*pi.value*radius

    def Square(side:(int|float)):
        return 4*side

    def Rhombus(side:(int|float)):
        return 4*side

    def Rectangle(length,breadth:(int|float)):
        return 2*(length+breadth)

    def Parallelogram(length,breadth:(int|float)):
        return 2*(length+breadth)

    def Triangle(side1,side2,side3:(int|float)):
        p = side1+side2+side3
        return p

    def Ellipse(a,b:(int|float)):
        p = (2*pi.value)*math.sqrt(a**2*b**2*0.5)
        return p

    def Trapezium(a,b,c,d:(int|float)):
        return a+b+c+d

    def Sector(radius,angle:(int|float)):
        return (2*radius)+((angle/360)*2*pi.value*radius)


class Graphs:
    def plot(x,y,xlabel=None,ylabel=None,title=None,xs=6.4,ys=4.8,yscale="linear",xscale="linear",marker="None",style_="classic",size=8):
        plt.figure(figsize = (xs,ys))
        style.use(style_)
        plt.yscale(yscale)
        plt.xscale(xscale)
        plt.plot(x,y, marker = marker, markersize = size)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    def scatter(x:np.ndarray|list,y:np.ndarray|list,xlabel=None,ylabel=None,title=None,xs=6.4,ys=4.8,yscale="linear",xscale="linear",marker="o",style_="classic",size=8):
        plt.figure(figsize = (xs,ys))
        style.use(style_)
        plt.yscale(yscale)
        plt.xscale(xscale)
        plt.scatter(x,y, marker = marker, markersize = size)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    def pie(x:np.ndarray|list,labels:list,shadow=False,radius=1,a=0,b=0,labeldistance=1.1,title=None):
        plt.title(title)
        plt.pie(x,labels = labels,shadow=shadow,center=(a,b),labeldistance=labeldistance,radius=radius)
        plt.show()


class Volume:
    def Cube(side:(int|float)):
        return side**3

    def Cuboid(length:(int|float),breadth:(int|float),height:(int|float)):
        return length*breadth*height

    def Cylinder(radius:(int|float),height:(int|float)):
        return pi.value*radius**2*height

    def Prism(length:(int|float),breadth:(int|float),Height:(int|float)):
        return length*breadth*Height

    def Sphere(radius:(int|float)):
        return (4/3)*pi.value*radius**3

    def Pyramid(length:(int|float),breadth:(int|float),Height:(int|float)):
        return (1/3)*length*breadth*Height

    def RightCircularCone(radius:(int|float),height:(int|float)):
        return (1/3)*pi.value*radius**2*height

    def QuadBasePyramid(length:(int|float),width:(int|float),height:(int|float)):
        return (1/3)*pi.value*length*width*height

    def Ellipsoid(x,y,z:(int|float)):
        return (4/3)*pi.value*x*y*z


    # NOTE! #

    """
        We are assuming the side of the polyhedron are same or
        we can say regular polyhedron
    """
    
    def Tetrahedron(side:(int|float)):
        return (side**3)*6*math.sqrt(2)

    def Octahedron(side:(int|float)):
        return (math.sqrt(2)/3)*side**3

    def Dodecahedron(side:(int|float)):
        return ((15+7*math.sqrt(5))/4)*side**3


class PeriodicTable:
    data = pd.read_csv("https://raw.githubusercontent.com/Sahil-Rajwar-2004/Datasets/main/elements.csv")
    def table():
        return ("""

                 1  2  3   4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
            1    H                                                   He
            2    Li Be                                B  C  N  O  F  Ne
            3    Na Mg                                Al Si P  S  Cl Ar
            4    K  Ca Sc  Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
            5    Rb Sr Y   Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
            6    Cs Be La- Hf Ta W  Re Os Ir Pt Au Hg Tl Pd Bi Po At Rn
            7    Fr Ra Ac- Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

                          -Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                          -Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr

                """)

    def spdf():
        return ("""
                1s
                2s 2p
                3s 3p 3d
                4s 4p 4d 4f
                5s 5p 5d 5f
                6s 6p 6d
                7s 7p

                s orbital can have -> [1 to 2] electrons
                p orbital can have -> [1 to 6] electrons
                d orbital can have -> [1 to 10] electrons
                f orbital can have -> [1 to 14] electrons

                """)


    def symbol(symbol_:str):
        position = PeriodicTable.data.index[PeriodicTable.data["Symbol"].str.lower() == symbol_.lower()].tolist()[0]
        return PeriodicTable.data.iloc[position]

    def element(element_name:str):
        position = PeriodicTable.data.index[PeriodicTable.data["Element"].str.lower() == element_name.lower()].tolist()[0]
        return PeriodicTable.data.iloc[position]

    def atomic_number(atomic_number:int):
        return PeriodicTable.data.iloc[atomic_number-1]


class Chemistry:
    def half_life_zero_order(Ao:(int|float),k:(int|float),order=0):
        """
            Ao(Initial Concentration): int
            k(Rate Constant): int
        """
        if order==0:
            return Ao/(2*k)
        elif order==1:
            Ao=0.693
            return Ao/(2*k)
        elif order==3:
            return 1/(Ao*k)
        else:
            return "undefined order!"
        return "Something Went Wrong!"

    def nernst_equation(P:(int|float),R:(int|float),n:(int|float),std_potential:(int|float)):
        E = std_potential - (0.06/n)*math.log10(R/P)
        return E

    def std_potential(oxidation:(int|float),reduction:(int|float)):
        E = reduction-oxidation
        return E

    def mass_percent(mass_solute:(int|float),mass_solution:(int|float)):
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

    def OR(input1:(True|False),input2:(True|False)):
        if type(input1) == bool and type(input2) == bool:
            return input1 or input2
        else:
            return f"inputs|parameters should be either {True} or {False}"

    def AND(input1:(True|False),input2:(True|False)):
        if type(input1) == bool and type(input2) == bool:
            return input1 and input2
        else:
            return f"inputs|parameters should be either {True} or {False}"

    def NOT(_input:(True|False)):
        if type(_input) == bool:
            return not _input
        else:
            return f"inputs|parameters should be either {True} or {False}"

    def NOR(input1:(True|False),input2:(True|False)):
        if type(input1) == bool and type(input2) == bool:
            return not(input1 or input2)
        else:
            return f"inputs|parameters should be either {True} or {False}"

    def NAND(input1:(True|False),input2:(True|False)):
        if type(input1) == bool and type(input2) == bool:
            return not(input1 and input2)
        else:
            return f"inputs|parameters should be either {True} or {False}"

    def XOR(input1:(True|False),input2:(True|False)):
        if type(input1) == bool and type(input2) == bool:
            return input1^input2
        else:
            return f"inputs|parameters should be either {True} or {False}"

    def XNOR(input1:(True|False),input2:(True|False)):
        if type(input1) == bool and type(input2) == bool:
            return not(input1^input2)
        else:
            return f"inputs|parameters should be either {True} or {False}"


class Bits:
    def flip_bits(number:int):
        toList = list(bin(number)[2:])
        rel = []
        for i in range(0,len(toList)):
            if toList[i] == "1":
                rel.append("0")
            elif toList[i] == "0":  
                rel.append("1")
            else:
                return "An Error Occured"
        calc = [int(i) for i in rel]
        total = 0
        for i in range(0,len(calc)):
            n = len(calc)-i-1
            x = calc[i]*2**n
            total+=x
        return total

    def num2bin(arg:int):
        return int(bin(arg)[2:])

    def bin2num(arg:int):
        toStrBinList = list(str(arg)) #<-- NameError was found in v-2.5.2 and fixed in v-2.5.3
        toBinList = [int(toStrBinList[i]) for i in range(0,len(toStrBinList))]
        nums,total = [],0
        for i in range(0,len(toBinList)):
            if (toBinList[i] == 1)|(toBinList[i] == 0):
                n = len(toBinList)-i-1
                x = toBinList[i]*2**n
                nums.append(x)
                total+=nums[i]
            else:
                return f"bits currupted! expected from 0s and 1s but got {toBinList[i]}"
        return total

    def XOR(x:int,y:int):
        return x^y

    def leftShift(number:int,left:int):
        if left > 0:
            total = 0
            if number < 0:
                y = abs(number)
            else:
                y = number
            binNumber = bin(y)[2:]
            binList = list(binNumber)
            rel = [int(binList[i]) for i in range(0,len(binList))]
            for _ in range(0,left):
                rel.append(0)
            for j in range(0,len(rel)):
                n = len(rel)-j-1
                x = rel[j]*2**n
                total+=x
            if number < 0:
                return -total
            else:
                return total
        else:
            return f"shift must be positive, {left}"

    def rightShift(number:int,right:int):
        try:
            return number>>right
        except Exception as e:
            return e

    def bitwiseComplement(integer:int):
        return ~integer


class LogFunction:
    def loge(x:(int|float)):
        ln = np.log(x)
        return ln

    def log10(x:(int|float)):
        log = np.log10(x)
        return log


class Trigonometry:
    # Degrees

    def sin_deg(angle:(int|float)):
        deg = np.deg2rad(angle)
        return round(trigo.sin(deg),2)

    def cos_deg(angle:(int|float)):
        deg = np.deg2rad(angle)
        return round(trigo.cos(deg),2)

    def tan_deg(angle:(int|float)):
        deg = np.deg2rad(angle)
        return round(trigo.tan(deg),2)

    def sec_deg(angle:(int|float)):
        deg = np.deg2rad(angle)
        return round(trigo.sec(deg),2)

    def cosec_deg(angle:(int|float)):
        deg = np.deg2rad(angle)
        return round(trigo.cosec(deg),2)

    def cot_deg(angle:(int|float)):
        deg = np.deg2rad(angle)
        return round(trigo.cot(deg),2)

    # Radians

    def sin_rad(angle:(int|float)):
        return round(trigo.sin(angle),2)

    def cos_rad(angle:(int|float)):
        return round(trigo.cos(angle),2)

    def tan_rad(angle:(int|float)):
        return round(trigo.tan(angle),2)

    def sec_rad(angle:(int|float)):
        return round(trigo.sec(angle),2)

    def cosec_rad(angle:(int|float)):
        return round(trigo.cosec(angle),2)

    def cot_rad(angle:(int|float)):
        return round(trigo.cot(angle),2)


class InversTrigonometry:
    def arcsine_rad(num:(int|float)):
        angle = trigo.arc_sin(num)
        return angle

    def arccos_rad(num:(int|float)):
        angle = trigo.arc_cos(num)
        return angle

    def arctan_rad(num:(int|float)):
        angle = trigo.arc_tan(num)
        return angle

    def arccosec_rad(num:(int|float)):
        angle = trigo.arc_cosec(num)
        return angle

    def arcsec_rad(num:(int|float)):
        angle = trigo.arc_sec(num)
        return angle

    def arccot_rad(num:(int|float)):
        angle = trigo.arc_cot(num)
        return angle

class Matrix:
    def matrices(matrix:list,dimension:tuple): #--> Row,Column
        dimension = tuple(dimension)
        try:
            m = np.matrix(matrix).reshape((dimension))
            return m
        except ValueError as error:
            return error

    def transpose(matrix:np.matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[0 for j in range(rows)] for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = transposed[i][j]
        return transposed

    def product(X:np.matrix,Y:np.matrix):
        # Note! #
        """
            The number of columns of a first matrix,
            should be equal to the number of rows
            of a second matrix.
        """
        if len(X[0]) != len(Y):
            return "Error: invalid matrix dimensions for multiplication!"
        result = [[0 for _ in range(len(Y[0]))] for _ in range(len())]
        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] += X[i][k]*Y[k][j]
        return result

    # NOTE #

    """
        For addition, subtractions the number of rows and columns
        for matrices should be equal!
        e.g => [[1,2,3],        [[9,8,7,6,5],
                [4,5,6]]         [34,56,87,98],
                                 [12,26,31,65]]

                (2,3)                (3,4)

        And for Determinant and Inverse of a matrices, the number of
        rows and columns should be same!
        e.g => [[1,2,3],    [[0,9,8],
                [4,5,6],     [7,6,5],
                [7,8,9]]     [4,3,2]]
                     
                (3,3)           (3,3)
    """

    def dimension(matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows>0 else 0
        return (rows,cols)

    def add(matrix1,matrix2):
        if Matrix.dimension(matrix1) == Matrix.dimension(matrix2):
            matrix = []
            for i in range(0,len(matrix1)):
                matrix.append([])
                for j in range(0,len(matrix1[0])):
                    matrix[i].append(matrix1[i][j]+matrix2[i][j])
            return matrix

    def subtract(matrix1,matrix2):
        if Matrix.dimension(matrix1) == Matrix.dimension(matrix2):
            matrix = []
            for i in range(0,len(matrix1)):
                matrix.append([])
                for j in range(0,len(matrix1[0])):
                    matrix[i].append(matrix1[i][j]-matrix2[i][j])
            return matrix

    def inverse(matrix):
        # check if matrix is square
        if len(matrix) != len(matrix[0]):
            return None
        n = len(matrix)
        # create identity matrix of same size as input matrix
        identity = [[int(i == j) for j in range(n)] for i in range(n)]
        # convert input matrix to augmented matrix by appending identity matrix
        augmented = [matrix[i] + identity[i] for i in range(n)]
        # perform row operations to transform augmented matrix into row-echelon form
        for i in range(n):
            # find row with largest absolute value in current column
            max_row = max(range(i, n), key=lambda r: abs(augmented[r][i]))
            # swap current row with max row (if necessary)
            if i != max_row:
                augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
            # divide current row by current pivot element to make it equal to 1
            pivot = augmented[i][i]
            if pivot == 0:
                return None
            augmented[i] = [elem/pivot for elem in augmented[i]]
            # use current row to eliminate pivot elements in rows below it
            for j in range(i+1, n):
                factor = augmented[j][i]
                augmented[j] = [elem - factor*augmented[i][k] for k, elem in enumerate(augmented[j])]
        # perform back-substitution to transform row-echelon form into reduced row-echelon form
        for i in range(n-1, 0, -1):
            for j in range(i):
                factor = augmented[j][i]
                augmented[j] = [elem - factor*augmented[i][k] for k, elem in enumerate(augmented[j])]
        # extract inverse matrix from augmented matrix
        inv = [row[n:] for row in augmented]
        return inv

    def determinant(matrix:np.ndarray):
        if len(matrix) != len(matrix[0]):
            return None
        n = len(matrix)
        if n==2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        det = 0
        for i in range(n):
            submatrix = [row[:i]+row[i+1:] for row in matrix[1:]]
            det += ((-1)**i)*matrix[0][i]*Matrix.determinant(submatrix)
        return det

class Sets:
    def set(A:list) -> list:
        res = []
        for item in A:
            if item not in res:
                res.append(item)
        return res

    def union(A:list,B:list) -> list:
        A = Sets.set(A)
        B = Sets.set(B)
        for i in B:
            if i not in A:
                A.append(i)
        return Sort.quick_sort(A)

    def intersect(A:list,B:list) -> list:
        res = []
        A = Sets.set(A)
        B = Sets.set(B)
        for i in B:
            if i in A:
                res.append(i)
        if len(res) == 0:
            return None
        return Sort.quick_sort(res)
    
    def subset(A:list,B:list) -> bool:
        A = Sets.set(A)
        B = Sets.set(B)
        for i in A:
            if i not in B:
                return False
        return True
    
    def belongsto(A:list,number:int,idx:bool = False) -> (int|bool):
        A = Sets.set(A)
        if number in A:
            if not idx:
                return True
            else:
                return A.index(number)
        return False

    def multiply(A:list,B:list) -> list:
        A = Sets.set(A)
        B = Sets.set(B)
        res = []
        for i in A:
            for j in B:
                res.append([i,j])
        return res


class Vectors:
    def vector(i,j,k,c=0):
        return [i,j,k,c]

    def magnitude(vec:list|np.ndarray):
        if len(vec)==3:
            total=0
            for i in range(0,len(vec)):
                x = vec[i]**2
                total+=x
            return math.sqrt(total)
        else:
            return "vector can't have 4th dimension"

    def cross_product(vec1:list|np.ndarray,vec2:list|np.ndarray):
        if len(vec1) == len(vec2) == 3:
            mat = [[1,1,1]]
            mat.append(vec1)
            mat.append(vec2)
            x = mat[0][0]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
            y = -mat[0][1]*(mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0])
            z = mat[0][2]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])
            return [x,y,z]
        else:
            return "size should be 3x3"
        return "length of vectors are not equal!"

    def unit_vector(i:(int|float),j:(int|float),k:(int|float)):
        mag = math.sqrt(i**2+j**2+k**2)
        return i/mag,j/mag,k/mag

    def dot_product(vec1:list|np.ndarray,vec2:list|np.ndarray):
        if len(vec1) == len(vec2) == 3:
            total = 0
            for i in range(0,len(vec1)):
                x = vec1[i]*vec2[i]
                total+=x
            return total
        else:
            return "directions should be in 3rd dimensional space"
        return "length of vectors are not equal"



