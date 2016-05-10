# This module allows you to move from one mixed notation of the vertex into another stepping through an intermediate translation to the purely fermionic notation
# Here the notation implemented:
# PH, XPH, PP 
# PH, XPH, PP (shifted in order to get the 'vertex structure' in the middle 

#------------Imports---------------------

from mymath import *

#-------- Initialize the two dictionaries ------------------

toferm ={ };
fromferm ={ };

#-------- Purely fermionic-> Identity-------------------------

toferm['Ferm'] = lambda (i,j,k):(i,j,k)

fromferm['Ferm'] = lambda (i,j,k):(i,j,k)

#-------- PP shifted-------------------------

toferm['PP_shift'] = lambda (i,j,k):(j+myceil_div2(i),-j+myfloor_div2(i)-1,k+myceil_div2(i))

fromferm['PP_shift'] = lambda (i,j,k):(i+j+1,i-myceil_div2(i+j+1),k-myceil_div2(i+j+1))


#-------- PH shifted-------------------------

toferm['PH_shift'] = lambda (i,j,k):(j-myfloor_div2(i),k+myceil_div2(i),j+myceil_div2(i))

fromferm['PH_shift'] = lambda (i,j,k):(k-i,i+myfloor_div2(k-i),j-myceil_div2(k-i))


#-------- XPH shifted-------------------------

toferm['XPH_shift'] = lambda (i,j,k):(j-myfloor_div2(i),k+myceil_div2(i), k-myfloor_div2(i))

fromferm['XPH_shift'] = lambda (i,j,k):(j-k,i+myfloor_div2(j-k),j-myceil_div2(j-k))


#-------- PP georg -> time reversal symmetry assumed-------------------------

toferm['PP_georg'] = lambda (i,j,k):(i-k-1,k,j)

fromferm['PP_georg'] = lambda (i,j,k):(i+j+1,k,j)


#-------- PH georg -> time reversal symmetry assumed-------------------------

toferm['PH_georg'] = lambda (i,j,k):(i+k,j,k)

fromferm['PH_georg'] = lambda (i,j,k):(i-k,j,k)

#--------------- TRANSLATION FUNCTION -----------------------------

def translate( notout, notin ):
    return lambda (i,j,k): fromferm[notout]((toferm[notin]((i,j,k))))

#------------------- Define useful objects--------------------------

PPtoPH = translate('PH_shift','PP_shift')
PHtoPP = translate('PP_shift','PH_shift')

PPtoXPH = translate('XPH_shift','PP_shift')
XPHtoPP = translate('PP_shift', 'XPH_shift')

PHtoXPH = translate('XPH_shift','PH_shift')
XPHtoPH = translate('PH_shift','XPH_shift')

PPtoPPg = translate('PP_georg','PP_shift')
PPgtoPP = translate('PP_shift','PP_georg')

PHtoPHg = translate('PH_georg','PH_shift')
PHgtoPH = translate('PH_shift','PH_georg')

PFtoPH = translate('PH_shift','Ferm')
PHtoPF = translate('Ferm','PH_shift')

PFtoPP = translate('PP_shift','Ferm')
PPtoPF = translate('Ferm','PP_shift')

PFtoXPH = translate('XPH_shift','Ferm')
XPHtoPF = translate('Ferm','XPH_shift')

PFtoPHg = translate('PH_georg','Ferm')
PHgtoPF = translate('Ferm','PH_georg')

PFtoPPg = translate('PP_georg','Ferm')
PPgtoPF = translate('Ferm','PP_georg')

PHtoPH = translate('PH_shift','PH_shift')
XPHtoXPH = translate('XPH_shift','XPH_shift')
PPtoPP = translate('PP_shift','PP_shift')
PPgtoPPg = translate('PP_georg','PP_georg')
PHgtoPHg = translate('PH_georg','PH_georg')

#print PPgtoPP((0,-114,0))
#print PPgtoPPg((0,0,0))
#print PHgtoPH((39,40,40)), PPgtoPP((0,20,40))
#print PPtoPP((1,2,3)), PHtoPH((1,2,3)), XPHtoXPH((1,2,3))
