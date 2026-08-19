def alti_FL (FL,QNH,T_sol):
  hauteur_standard_fl = float(FL)*100*0.3048
  pression_fl_standard=1013.25 * (1-(0.0065*hauteur_standard_fl/288.15))**5.25588
  h = (T_sol+273.15)/0.0065 * (1-(pression_fl_standard/QNH )**0.190263)
  return(h)