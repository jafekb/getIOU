def xywh(bboxA, bboxB):
    """
    This function computes the intersection over union between two
    2-d boxes (usually bounding boxes in an image.

    Attributes:
        bboxA (list): defined by 4 values: [xmin, ymin, width, height].
        bboxB (list): defined by 4 values: [xmin, ymin, width, height].
        (Order is irrelevant).

    Returns:
        IOU (float): a value between 0-1 representing how much these boxes overlap.
    """

    xA, yA, wA, hA = bboxA
    areaA = wA * hA
    xB, yB, wB, hB = bboxB
    areaB = wB * hB

    overlap_xmin = max(xA, xB)
    overlap_ymin = max(yA, yB)
    overlap_xmax = min(xA + wA, xB + wB)
    overlap_ymax = min(yA + hA, yB + hB)

    W = overlap_xmax - overlap_xmin
    H = overlap_ymax - overlap_ymin

    if min(W, H) < 0:
        return 0

    intersect = W * H
    union = areaA + areaB - intersect

    return intersect / union

def xyXY(bboxA, bboxB):
    """
    Similar to the above function, this one computes the intersection over union
    between two 2-d boxes. The difference with this function is that it accepts
    bounding boxes in the form [xmin, ymin, XMAX, YMAX].

    Attributes:
        bboxA (list): defined by 4 values: [xmin, ymin, XMAX, YMAX].
        bboxB (list): defined by 4 values: [xmin, ymin, XMAX, YMAX].

    Returns:
        IOU (float): a value between 0-1 representing how much these boxes overlap.

    """
    xminA, yminA, xmaxA, ymaxA = bboxA
    widthA = xmaxA - xminA
    heightA = ymaxA - yminA
    areaA = widthA * heightA

    xminB, yminB, xmaxB, ymaxB = bboxB
    widthB = xmaxB - xminB
    heightB = ymaxB - yminB
    areaB = widthB * heightB

    xA = max(xminA, xminB)
    yA = max(yminA, yminB)
    xB = min(xmaxA, xmaxB)
    yB = min(ymaxA, ymaxB)

    W = xB - xA
    H = yB - yA 
    
    if min(W, H) < 0:
    	return 0

    intersect = W * H
    union = areaA + areaB - intersect

    iou = intersect / union

    return iou
