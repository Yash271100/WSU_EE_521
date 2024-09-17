import numpy as np
import pdb
import itertools as itt

# # Runing Code:

# Writing Recursive functions:
class HW1_1b():

    
    def __init__(self):
        self.count = 1;
        self.Flag=1;

    
    def UpdateCheck(self ,g1, g2, epsilon_1, epsilon_2):
        if g1 <= epsilon_1 and g1 >= -epsilon_1 and g2 <= epsilon_2 and g2 >= -epsilon_2:
            return False;
        else:
            return True;


    def g(self,_x_1,_x_2):
        G = 2*(_x_1)**2 + (_x_1)*(_x_2) - _x_1-2;
        return G
    # g = 2*(x_1)^2 + (x_1)*(x_2) - x_1-2;
    def del_g(self,_x_1,_x_2):
        G_x_1 = 4*_x_1 + _x_2; G_x_2 = _x_1;
        return G_x_1, G_x_2
    # g_x_1 = 4*x_1 + x_2; g_x_2 = x_1;
    
    def h(self,_x_1,_x_2):
        H = (_x_1)**2 - _x_2;
        return H
    # h = (x_1)^2 - x_2;
    def del_h(self,_x_1,_x_2):
        H_x_1 = 2*_x_1; H_x_2 = -1;
        return H_x_1, H_x_2
    # h_x_1 = 2*x_1; h_x_2 = -1;
    

    
    # Jacobian:
    def Jacob(self, x_1, x_2):
        J = np.zeros([2,2]);
        J[0,0],J[0,1]=self.del_g(x_1,x_2)
        J[1,0],J[1,1]=self.del_h(x_1,x_2)
        return J
    
    # Update Step:
    def UpdateStep(self, J, _x_1, _x_2, g1, g2):
        J_1 = np.linalg.inv(J);
        _x = np.zeros(2); F = np.zeros(2);
        _x[0] = _x_1; _x[1] = _x_2;
        F[0] = g1; F[1] = g2;
        x = _x - np.matmul(J_1,(F));
        return x[0], x[1]
    
    def Solve(self, _x_1, _x_2, epsilon_1, epsilon_2):
        # Checking for Update:
        # print(self.count)
        x1 = _x_1; x2 = _x_2;
        g1 = self.g(_x_1, _x_2); g2 = self.h(_x_1, _x_2);
        if self.UpdateCheck(g1, g2, epsilon_1, epsilon_2):
            J = self.Jacob(x1, x2);
            x1,x2=self.UpdateStep(J, x1, x2, g1, g2);
            self.count+=1;
            if self.UpdateCheck(g1, g2, epsilon_1, epsilon_2):
                self.Solve(x1, x2, epsilon_1, epsilon_2);
        else:
            self.Flag=0;
            return print(f"Converged!!! Final x1 = {x1} & Final x2 = {x2}. The solution converged after {self.count} iterations")


pr=HW1_1b()
# Initialization:
x_1 = 0.9; x_2 = 1.1;
epsilon_1 = 1e-4; epsilon_2 = 1e-4;
pr.Solve(x_1, x_2, epsilon_1, epsilon_2)
