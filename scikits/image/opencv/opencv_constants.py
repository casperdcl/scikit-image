
#############################################
# Image Processing Constants 
############################################


CV_BLUR_NO_SCALE = 0
CV_BLUR = 1
CV_GAUSSIAN = 2
CV_MEDIAN = 3
CV_BILATERAL = 4

CV_TERMCRIT_NUMBER = 1
CV_TERMCRIT_ITER = 1
CV_TERMCRIT_EPS = 2

CV_INTER_NN = 0
CV_INTER_LINEAR = 1
CV_INTER_CUBIC = 2
CV_INTER_AREA = 3

CV_WARP_FILL_OUTLIERS = 8
CV_WARP_INVERSE_MAP = 16

#########################
# Calibration Constants #
#########################
CV_CALIB_USE_INTRINSIC_GUESS = 1
CV_CALIB_FIX_ASPECT_RATIO = 2
CV_CALIB_FIX_PRINCIPAL_POINT = 4
CV_CALIB_ZERO_TANGENT_DIST = 8
CV_CALIB_CB_ADAPTIVE_THRESH = 1
CV_CALIB_CB_NORMALIZE_IMAGE = 2
CV_CALIB_CB_FILTER_QUADS = 4

####################
# cvMat TypeValues #
####################
CV_CN_MAX = 4
CV_CN_SHIFT = 3
CV_DEPTH_MAX = (1 << CV_CN_SHIFT)

CV_8U = 0
CV_8S = 1
CV_16U = 2
CV_16S = 3
CV_32S = 4
CV_32F = 5
CV_64F = 6
CV_USRTYPE1 = 7

def _CV_MAKETYPE(depth,cn):
    return ((depth) + (((cn)-1) << CV_CN_SHIFT))

CV_8UC1 = _CV_MAKETYPE(CV_8U,1)
CV_8UC2 = _CV_MAKETYPE(CV_8U,2)
CV_8UC3 = _CV_MAKETYPE(CV_8U,3)
CV_8UC4 = _CV_MAKETYPE(CV_8U,4)

CV_8SC1 = _CV_MAKETYPE(CV_8S,1)
CV_8SC2 = _CV_MAKETYPE(CV_8S,2)
CV_8SC3 = _CV_MAKETYPE(CV_8S,3)
CV_8SC4 = _CV_MAKETYPE(CV_8S,4)

CV_16UC1 = _CV_MAKETYPE(CV_16U,1)
CV_16UC2 = _CV_MAKETYPE(CV_16U,2)
CV_16UC3 = _CV_MAKETYPE(CV_16U,3)
CV_16UC4 = _CV_MAKETYPE(CV_16U,4)

CV_16SC1 = _CV_MAKETYPE(CV_16S,1)
CV_16SC2 = _CV_MAKETYPE(CV_16S,2)
CV_16SC3 = _CV_MAKETYPE(CV_16S,3)
CV_16SC4 = _CV_MAKETYPE(CV_16S,4)

CV_32SC1 = _CV_MAKETYPE(CV_32S,1)
CV_32SC2 = _CV_MAKETYPE(CV_32S,2)
CV_32SC3 = _CV_MAKETYPE(CV_32S,3)
CV_32SC4 = _CV_MAKETYPE(CV_32S,4)

CV_32FC1 = _CV_MAKETYPE(CV_32F,1)
CV_32FC2 = _CV_MAKETYPE(CV_32F,2)
CV_32FC3 = _CV_MAKETYPE(CV_32F,3)
CV_32FC4 = _CV_MAKETYPE(CV_32F,4)

CV_64FC1 = _CV_MAKETYPE(CV_64F,1)
CV_64FC2 = _CV_MAKETYPE(CV_64F,2)
CV_64FC3 = _CV_MAKETYPE(CV_64F,3)
CV_64FC4 = _CV_MAKETYPE(CV_64F,4)



