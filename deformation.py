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
import math

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
  
  def norm(self, x, y, p):
    return np.linalg.norm(x)**p - np.linalg.norm(y)**p
  
  def render(self, H):
    pass
  def sample(self, M_H, M_I):
    pass
  
  def Ep(self, P_iH, P_Mi_I, ni_H, n_Mi_H):
    """
    energy terms
    Ep(P_i^H) = || P_i^H - P_M(i)^I||^2 + lambda_n(1 - n_i^H * n_M(i)^I)^2
    """

    return self.norm(P_iH, P_Mi_I, 2) + self._LAMBDA * math.pow((1 - ni_H * n_Mi_H), 2)
  
  def Ee(self, P_iH1, P_iH2, P_Mi_H, P_Mi2_H):
     """
    energy terms
    Ep(P_i^H, P(i+1)^H) = || P_i^H - P(i+1)^H|| - ||P_M(i)^I - PM(i + 1)^I ||
    """      
    return self.norm(P_iH1, P_iH2, 1) - self.norm(P_Mi_H, P_Mi2_H)
  def outwardNormal(self, N):
    pass
  def boundary_match(self, H):
    """
    one of candidate
    @param： H： h x w x d
    @return： MH， DH （same dimension as input image）MH is mask， DH is direction map
    """
    # get mask and direction map, M_H = n x h x w, D_H = n x h x w x c, where c is RGB channel
    M_H, D_H = self.render(H)
    # get random sampled points from M_H and M_I
    P_H, P_I = self.sample(M_H, M_I)
    
    ni_H = self.outwardNormal(P_H)
    nj_I = self.outwardNormal(P_I)
    
    pmi = sys.maxsize
    P_M = []
    argmin = 0
    
    for i in range(len(PH)):
      EP_i = self.Ep(P_H[i], P_M[i], ni_H[i], ni_H[i])
      EE_i = self.Ed(P_H[i], P_H[i + 1], P_M[i], P_M[i - 1]])     
      P_M.append(EP_i + EE_i)
      
    return max(0, min(P_M))

