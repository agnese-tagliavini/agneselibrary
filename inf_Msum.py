import numpy as np
import math
from numpy.linalg import inv
from agneselib.inv_lapack import *

# generate_sum_function provides the fitting of a finite matsubara sum in order to get the extension of the sum up to infinity
# The Least-Square fitting uses the following fitting function : sum_{i=0}^{Nl} a_i (x)^{-i}
# This requires the minimization of the chisquare which has been done in a semi-analytic way (see notes by Georg Roehringer)
# generate_sum_func returns sumfit of a given single-variable function 

def generate_sum_func(iMin,wNum,Nl):        #enter the starting point of your fit->iMin, the number of points to fit-> wNum, the "order" of your fitting function (see above)->Nl  
    iMax = wNum + iMin-1
    print iMax, iMin, wNum
    # Matrix of coeff! 
    M = np.array ( [[np.sum([  1./(k**i * k**j) for k in range(iMin,iMax+1)]) for i in range(Nl)] for j in range(Nl)] )
#    print M
    
    # Inverse
    Mm1 = inv(M)
#    print "M1:", Mm1
    
    # Final coeff
    w = [np.sum([Mm1[l][0] / (float(i+iMin)**l) for l in range(Nl)]) for i in range(wNum)]
#    print w

    #Define the partial sums of the w coefficients
    
    def nu(i):
        return np.sum(w[i::])
#    print nu(0)
    
    #The finite matsubara sum is automatically fitted end returns the asymptotic value where iMin -> infinity

    def sumfit(f):
        sum1= np.sum(np.array([f(i) for i in range(-iMin,iMin)]))
        sum2= np.sum(np.array([(f(iMin+i)+f(-iMin-1-i))*nu(i) for i in range(1,wNum)]))
        return sum1+sum2
    
    return sumfit 

def generate_dblsum_func(iMin,wNum,Nl):        #enter the starting point of your fit->iMin, the number of points to fit-> wNum, the "order" of your fitting function (see above)->Nl  
    iMax = wNum + iMin - 1
    print iMax, iMin, wNum
    # Matrix of coeff! 
    M = np.array ( [[np.sum([  1./(k**i * k**j) for k in range(iMin,iMax+1)]) for i in range(Nl)] for j in range(Nl)] )
#    print M
    
    # Inverse
    Mm1 = inv(M)
#    print "M1:", Mm1
    
    # Final coeff
    w = [np.sum([Mm1[l][0] / (float(i+iMin)**l) for l in range(Nl)]) for i in range(wNum)]
#    print w
    
    #Define the partial sums of the w coefficients

    def nu(i):
        return np.sum(w[i::])
#    print nu(0)
    
    #The finite matsubara sum is automatically fitted end returns the asymptotic value where iMin -> infinity
    def dblsumfit(g):
        sum1 = np.sum(np.array([[g(j,k) for j in range(-iMin,iMin)] for k in range(-iMin,iMin)]).flatten())
#        print sum1
        def sumint(i):
            return  np.sum(np.array([(g(j,iMin+i-1)+g(j,-iMin-i) +g(iMin+i-1,j)+g(-iMin-i,j))*nu(i) for j in range(-iMin-i,iMin+i)]))
        sum2=np.sum(np.array([sumint(i) for i in range(1,wNum)]))
#        print sum2
        return sum1+sum2
    
    return dblsumfit 

def generate_invfit_func(iMin,wNum,Nl):        #enter the starting point of your fit->iMin, the number of points to fit-> wNum, the "order" of your fitting function (see above)->Nl  
    iMax = wNum + iMin  
    print iMax, iMin, wNum
    # Matrix of coeff! 
    M = np.array ( [[np.sum([  1./(k**i * k**j) for k in range(iMin,iMax)]) for i in range(Nl)] for j in range(Nl)] )
#    print M
    
    # Inverse
    Mm1 = inv(M)
#    print "M1:", Mm1
    
    # Final coeff
    w = [np.sum([Mm1[l][0] / (float(i+iMin)**l) for l in range(Nl)]) for i in range(0,wNum)]
    print w[0] 
    #The finite matrix inversion is  fitted end returns the asymptotic value where iMin -> infinity
    def invfit(g):
        
        def matrices(i):
            return np.array([[g(j,k) for j in range(-iMin-i, iMin+i)] for k in range(-iMin-i, iMin+i)])
        
        def inverse(i):
#            return faster_inverse(matrices(i))
            return inv(matrices(i))

        inv_fitted = np.sum(inverse(i)[i:i+2*iMin,i:i+2*iMin]*w[i] for i in range(0,wNum))
#        print inv_fitted.shape 
        return inv_fitted

 
    return invfit

#A = np.array([[1.,2.],[4.,5.]])
#D =np.array([[1.,2.],[4.,5.]])
#print A
#check1 = inv(D)
#check = faster_inverse(A)
#print check, check1
#Test
#def g(x):
#    return 1./(abs(x)+1)**2

#result= (math.pi**2/3-1)
#n=89
#tail=11
#sommafit = generate_sum_func(n,tail,4)

#Test1
#def h(i,j):
#    return 1./(i**4+1+j**4)

#bign = 100
#n = 100
#tail = 10
#dblsommafit = generate_dblsum_func(n,tail,5)

#result = dblsommafit(h)
#somma1 = np.sum(np.array([[h(i,j) for i in range(-bign,bign)]for j in range(-bign,bign)]))
#print result, somma1
#somma = np.sum(np.array([g(i) for i in range(-n,n)]))
#print 1-sommafit(g)/result,1-somma/result

# Print info
#print "Matrix M: "
#print M
#print "Inverse matrix: "
#print Mm1
#print "Check, product: M * M^-1"
#print np.dot( M , Mm1 )
#print "Coeff w: "
#print w
#np.savetxt( fileNameOut , w )

