"""
L.Higgins 11-vi-18
This is a piece of code to use the equation from 'Gardea-Torresday L Environ Sci Technol 34:4392.'. User inputs the ratio between
the metallic FCC nanoparticles coordination number, N, and the coordination number of the standard foil, N_{foil}. It then takes
the average bond length, d. Both of these values are collected by using EXAFS modelling for the nanoparticles compared to the foil.
The equation is then solved using a numeric method (see: sympy.solve), yielding three solutions (since it is a cubic eqn.). Take
the third solution as the average nanoparticle radius, R.  N.B. This can only work when using a 1st shell EXAFS fitting!

I've designed this to be user friendly, ctrl-c will always break.
"""
try:
    from sympy.solvers import solve
    from sympy import Symbol
except:
    print('//WARNING// Please install the Sympy module: https://docs.sympy.org/latest/install.html ')

try:
    import numpy as np
    import sys
except:
    print('//WARNING// Code requires numpy and sys to be installed')

continuing=True

def inp(txt):
    if sys.version_info[0] == 3:
        return input(txt)
    elif sys.version_info[0] == 2:
        return raw_input(txt)
    else:
        print('FCC requires python > 2')

def get_N():
# Asks the user to give the ratio between the coordination numbers in a user-friendly style.
    N = Symbol('N')
    try:
        N = float(inp('Please input N/N_foil: \n'))
        if N>0 and N<1:
            return N
        else:
            print('N must be a ratio between 0 and 1 exclusive, try again:\n')
            return get_N()
    except ValueError:
        print('N/Nfoil must be a float, try again:\n')
        return get_N()
    except KeyboardInterrupt:
        print('\n  --   Exiting because of keyboard Interuption  --   \n')
        sys.exit()


def get_d():
# Asks the user to give the average 1st shell bond length in a user-friendly style.
    N = Symbol('d')
    try:
        d = float(inp('Please input d e.g. Au ~ 2.85: '))
    except ValueError:
        print('d must be a decimal number, try again:')
        return get_d()
    except KeyboardInterrupt:
        print('\n  --   Exiting because of keyboard Interuption  --   \n')
        sys.exit()
    return d

def cont():
# Asks the user whether they want to continue in a user-friendly style.
    try:
        poss_ans = ['y','Y','n','N']
        var = str(inp('Would you like to continue? y/n \n'))
        if var in poss_ans:
            if var.lower() == 'n':
                return False
            elif var.lower() == 'y':
                return True
        else:
            print('please enter y/Y or n/N, try again:\n')
            return cont()
    except KeyboardInterrupt:
        print('\n  --   Exiting because of keyboard Interuption  --   \n')
        sys.exit()

def find_F0(N,d):
# Numeric solution of the Gardea equation using sympy.solve - no user involvement
    R = Symbol('R')
    F = (R**3 * (N-1)) + (0.75 * d * R**2) - (0.0625 * d**3)
    sol = solve(F,R,cubic=True)
    print('The solutions to F0 are: \n', sol)

while continuing:
# Continues until user breaks with either ctrl-c or 'n'.
    N = get_N()
    print('you entered: ', N)
    d = get_d()
    print('you entered:',  d)
    find_F0(N,d)
    continuing = cont()

print('         Thanks for using the FCC minimum tool!           \n #please cite#\n #"Gardea-Torresday L, Tiemann KJ, Gamez G, et. al.#\n #(2000); Environ Sci Technol 34:4392."#')
sys.exit()
