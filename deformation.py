"""
AUTO HAIR PROCESS:
input: a image, output:
step 1: classify the input image as one of few hair spatial distrubution classes (from global classifier)
step 2: generate accurate hair mask and coarsely direction map (from novel deep neural network)
step 3: image-based search bot obtain best matching candidates
step 4: deform the candidate and refined using boundary correspondences with direction map 
step 5: generate 3D hair strands

This class is only for deform selected candidate 
1. compute boundary correspondences between hair region of input image and rendered image of a candidate
2. coresspondence interpoloated to entire hair region (using globally smooth warping function)
3. compute deformation based on corresponences
"""
import numpy
class deformation:
  """
  input: few best matched candidates
  output: deformed candidate with closest matching direction map
  """
  def __init__(self, candidates, image, LAMBDA = 10):
    self._candidates = candidates                      # dimension: n x h x w x d, where n is number of candidates, h is x coordinate, w is y coordinate, d is z coordinate 5 < n < 50
    self._img = image                                  # input image
    self._LAMBDA = LAMBDA
    
  def M(self):
    pass
  
  def P_M(self):
    pass
  
  def Ep(self, P_H):
    """
    energy terms
    Ep(P_i^H) = || P_i^H - P_M(i)^I||^2 + lambda_n(1 - n_i^H * n_M(i)^I)^2
    """
    EP = []
    EP = 
    return EP
  
  def Ee(self):
     """
    energy terms
    Ep(P_i^H, P(i+1)^H) = || P_i^H - P(i+1)^H|| - ||P_M(i)^I - PM(i + 1)^I ||
    """
    EE =[]
    return EE
  def boundary_match(self, H):
    """
    one of candidate
    @param： H： h x w x d
    @return： MH， DH （same dimension as input image）MH is mask， DH is direction map
    """
    pass
  
  def interpolate(self):
    pass
  def deform(self):
    pass
