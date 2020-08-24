# -*- coding: utf-8 -*-
#
import math
import numpy as np
import quaternion
import module.MMathC as MMathC

from utils.MLogger import MLogger # noqa

logger = MLogger(__name__)


class MRect():

    def __init__(self, x=0, y=0, width=0, height=0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def x(self):
        return int(self.__x)

    def y(self):
        return int(self.__y)

    def width(self):
        return int(self.__width)

    def height(self):
        return int(self.__height)

    def __str__(self):
        return "MRect({0}, {1}, {2}, {3})".format(self.__x, self.__y, self.__width, self.__height)


class MVector2D():

    def __init__(self, x=0, y=0):
        if isinstance(x, MVector2D):
            # クラスの場合
            self.__data = x.__data
        elif isinstance(x, np.ndarray):
            # arrayそのものの場合
            self.__data = np.array([x[0], x[1]], dtype=np.float64)
        else:
            self.__data = np.array([x, y], dtype=np.float64)

    def length(self):
        return MMathC.length(self.__data)

    def lengthSquared(self):
        return MMathC.lengthSquared(self.__data)

    def normalized(self):
        normv = MMathC.normalized(self.__data)
        return MVector3D(normv[0], normv[1], normv[2])

    def normalize(self):
        self.effective()
        self.__data = MMathC.normalized(self.__data)
        
    def effective(self):
        self.__data[np.isnan(self.__data)] = 0
        self.__data[np.isinf(self.__data)] = 0

        return self
            
    def data(self):
        return self.__data

    def __str__(self):
        return "MVector2D({0}, {1})".format(self.__data[0], self.__data[1])

    def __lt__(self, other):
        return np.all(self.__data < other.__data)

    def __le__(self, other):
        return np.all(self.__data <= other.__data)

    def __eq__(self, other):
        return np.all(self.__data == other.__data)

    def __ne__(self, other):
        return np.any(self.__data != other.__data)

    def __gt__(self, other):
        return np.all(self.__data > other.__data)

    def __ge__(self, other):
        return np.all(self.__data >= other.__data)

    def __add__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.add_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.add_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.add_int(self.__data, other)
        else:
            v = MMathC.add_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __sub__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.sub_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.sub_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.sub_int(self.__data, other)
        else:
            v = MMathC.sub_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __mul__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.mul_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.mul_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.mul_int(self.__data, other)
        else:
            v = MMathC.mul_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __truediv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.truediv_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.truediv_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.truediv_int(self.__data, other)
        else:
            v = MMathC.truediv_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __floordiv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.floordiv_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.floordiv_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.floordiv_int(self.__data, other)
        else:
            v = MMathC.floordiv_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __mod__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.mod_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.mod_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.mod_int(self.__data, other)
        else:
            v = MMathC.mod_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __pow__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.pow_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.pow_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.pow_int(self.__data, other)
        else:
            v = MMathC.pow_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __lshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.lshift_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.lshift_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.lshift_int(self.__data, other)
        else:
            v = MMathC.lshift_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __rshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.rshift_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.rshift_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.rshift_int(self.__data, other)
        else:
            v = MMathC.rshift_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __and__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.and_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.and_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.and_int(self.__data, other)
        else:
            v = MMathC.and_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __dataor__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.dataor_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.dataor_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.dataor_int(self.__data, other)
        else:
            v = MMathC.dataor_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __or__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.or_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.or_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.or_int(self.__data, other)
        else:
            v = MMathC.or_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __neg__(self):
        return self.__class__(-self.__data[0], -self.__data[1])

    def __pos__(self):
        return self.__class__(+self.__data[0], +self.__data[1])

    def __invert__(self):
        return self.__class__(~self.__data[0], ~self.__data[1])
    
    def x(self):
        return self.__data[0]

    def y(self):
        return self.__data[1]
    
    def setX(self, x):
        self.__data[0] = x

    def setY(self, y):
        self.__data[1] = y

    def to_log(self):
        return "x: {0}, y: {1}".format(round(self.__data[0], 5), round(self.__data[1], 5))


class MVector3D():

    def __init__(self, x=0.0, y=0.0, z=0.0):
        if isinstance(x, MVector3D):
            # クラスの場合
            self.__data = x.__data
        elif isinstance(x, np.ndarray):
            # arrayそのものの場合
            self.__data = np.array([x[0], x[1], x[2]], dtype=np.float64)
        else:
            self.__data = np.array([x, y, z], dtype=np.float64)

    def copy(self):
        return MVector3D(self.x(), self.y(), self.z())

    def length(self):
        return MMathC.length(self.__data)

    def lengthSquared(self):
        return MMathC.lengthSquared(self.__data)

    def normalized(self):
        normv = MMathC.normalized(self.__data)
        return MVector3D(normv[0], normv[1], normv[2])

    def normalize(self):
        self.effective()
        self.__data = MMathC.normalized(self.__data)
    
    def distanceToPoint(self, v):
        return self.__sub__(v).length()
    
    def project(self, modelView, projection, viewport):
        tmp = MVector4D(self.x(), self.y(), self.z(), 1)
        tmp = projection * modelView * tmp
        if is_almost_null(tmp.w()):
            tmp.setW(1)

        tmp /= tmp.w()
        tmp = tmp * 0.5 + MVector4D(0.5, 0.5, 0.5, 0.5)
        tmp.setX(tmp.x() * viewport.width() + viewport.x())
        tmp.setY(tmp.y() * viewport.height() + viewport.y())

        tmp.effective()

        return tmp.toVector3D()

    def unproject(self, modelView, projection, viewport):
        inverse = (projection * modelView).inverted()

        tmp = MVector4D(self.x(), self.y(), self.z(), 1)
        tmp.setX((tmp.x() - viewport.x()) / viewport.width())
        tmp.setY((tmp.y() - viewport.y()) / viewport.height())
        tmp = tmp * 2 - MVector4D(1, 1, 1, 1)
        tmp.effective()

        obj = inverse * tmp
        if is_almost_null(obj.w()):
            obj.setW(1)

        obj /= obj.w()
        obj.effective()
        
        return obj.toVector3D()
        
    def toVector4D(self):
        return MVector4D(self.__data[0], self.__data[1], self.__data[2], 0)

    def is_almost_null(self):
        return (is_almost_null(self.__data[0]) and is_almost_null(self.__data[1]) and is_almost_null(self.__data[2]))
    
    def effective(self):
        self.__data[np.isnan(self.__data)] = 0
        self.__data[np.isinf(self.__data)] = 0

        return self
                
    def abs(self):
        self.setX(abs(get_effective_value(self.x())))
        self.setY(abs(get_effective_value(self.y())))
        self.setZ(abs(get_effective_value(self.z())))

        return self
                
    def one(self):
        self.effective()
        self.setX(1 if is_almost_null(self.x()) else self.x())
        self.setY(1 if is_almost_null(self.y()) else self.y())
        self.setZ(1 if is_almost_null(self.z()) else self.z())

        return self
    
    def non_zero(self):
        self.effective()
        self.setX(0.0001 if is_almost_null(self.x()) else self.x())
        self.setY(0.0001 if is_almost_null(self.y()) else self.y())
        self.setZ(0.0001 if is_almost_null(self.z()) else self.z())

        return self
    
    def isnan(self):
        self.__data = self.data().astype(np.float64)
        return np.isnan(self.data()).any()
                
    @classmethod
    def crossProduct(cls, v1, v2):
        crossv = MMathC.cross(v1.__data, v2.__data)
        return MVector3D(crossv[0], crossv[1], crossv[2])

    @classmethod
    def dotProduct(cls, v1, v2):
        dotv = MMathC.dot(v1.__data, v2.__data)
        return dotv
    
    def data(self):
        return self.__data
    
    def to_log(self):
        return "x: {0}, y: {1} z: {2}".format(round(self.__data[0], 5), round(self.__data[1], 5), round(self.__data[2], 5))

    def __str__(self):
        return "MVector3D({0}, {1}, {2})".format(self.__data[0], self.__data[1], self.__data[2])

    def __lt__(self, other):
        return np.all(self.__data < other.__data)

    def __le__(self, other):
        return np.all(self.__data <= other.__data)

    def __eq__(self, other):
        return np.all(self.__data == other.__data)

    def __ne__(self, other):
        return np.any(self.__data != other.__data)

    def __gt__(self, other):
        return np.all(self.__data > other.__data)

    def __ge__(self, other):
        return np.all(self.__data >= other.__data)

    def __add__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.add_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.add_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.add_int(self.__data, other)
        else:
            v = MMathC.add_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __sub__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.sub_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.sub_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.sub_int(self.__data, other)
        else:
            v = MMathC.sub_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __mul__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.mul_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.mul_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.mul_int(self.__data, other)
        else:
            v = MMathC.mul_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __truediv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.truediv_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.truediv_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.truediv_int(self.__data, other)
        else:
            v = MMathC.truediv_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __floordiv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.floordiv_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.floordiv_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.floordiv_int(self.__data, other)
        else:
            v = MMathC.floordiv_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __mod__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.mod_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.mod_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.mod_int(self.__data, other)
        else:
            v = MMathC.mod_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __pow__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.pow_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.pow_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.pow_int(self.__data, other)
        else:
            v = MMathC.pow_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __lshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.lshift_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.lshift_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.lshift_int(self.__data, other)
        else:
            v = MMathC.lshift_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __rshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.rshift_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.rshift_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.rshift_int(self.__data, other)
        else:
            v = MMathC.rshift_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __and__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.and_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.and_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.and_int(self.__data, other)
        else:
            v = MMathC.and_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __dataor__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.dataor_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.dataor_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.dataor_int(self.__data, other)
        else:
            v = MMathC.dataor_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __or__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.or_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.or_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.or_int(self.__data, other)
        else:
            v = MMathC.or_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __neg__(self):
        return self.__class__(-self.__data[0], -self.__data[1], -self.__data[2])

    def __pos__(self):
        return self.__class__(+self.__data[0], +self.__data[1], +self.__data[2])

    def __invert__(self):
        return self.__class__(~self.__data[0], ~self.__data[1], ~self.__data[2])
    
    def x(self):
        return self.__data[0]

    def y(self):
        return self.__data[1]

    def z(self):
        return self.__data[2]
    
    def setX(self, x):
        self.__data[0] = x

    def setY(self, y):
        self.__data[1] = y

    def setZ(self, z):
        self.__data[2] = z


class MVector4D():

    def __init__(self, x=0, y=0, z=0, w=0):
        if isinstance(x, MVector4D):
            # クラスの場合
            self.__data = x.__data
        elif isinstance(x, np.ndarray):
            # 行列そのものの場合
            self.__data = np.array([x[0], x[1], x[2], x[3]], dtype=np.float64)
        else:
            self.__data = np.array([x, y, z, w], dtype=np.float64)
    
    def length(self):
        return MMathC.length(self.__data)

    def lengthSquared(self):
        return MMathC.lengthSquared(self.__data)

    def normalized(self):
        normv = MMathC.normalized(self.__data)
        return MVector3D(normv[0], normv[1], normv[2])

    def normalize(self):
        self.effective()
        self.__data = MMathC.normalized(self.__data)
    
    def toVector3D(self):
        return MVector3D(self.__data[0], self.__data[1], self.__data[2])

    def is_almost_null(self):
        return (is_almost_null(self.__data[0]) and is_almost_null(self.__data[1]) and is_almost_null(self.__data[2]) and is_almost_null(self.__data[3]))
                   
    def effective(self):
        self.__data[np.isnan(self.__data)] = 0
        self.__data[np.isinf(self.__data)] = 0
                                
    @classmethod
    def dotProduct(cls, v1, v2):
        dotv = np.dot(v1.__data, v2.__data)
        return dotv
    
    def data(self):
        return self.__data

    def __str__(self):
        return "MVector4D({0}, {1}, {2}, {3})".format(self.__data[0], self.__data[1], self.__data[2], self.__data[3])

    def __lt__(self, other):
        return np.all(self.__data < other.__data)

    def __le__(self, other):
        return np.all(self.__data <= other.__data)

    def __eq__(self, other):
        return np.all(self.__data == other.__data)

    def __ne__(self, other):
        return np.any(self.__data != other.__data)

    def __gt__(self, other):
        return np.all(self.__data > other.__data)

    def __ge__(self, other):
        return np.all(self.__data >= other.__data)

    def __add__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.add_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.add_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.add_int(self.__data, other)
        else:
            v = MMathC.add_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __sub__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.sub_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.sub_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.sub_int(self.__data, other)
        else:
            v = MMathC.sub_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __mul__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.mul_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.mul_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.mul_int(self.__data, other)
        else:
            v = MMathC.mul_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __truediv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.truediv_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.truediv_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.truediv_int(self.__data, other)
        else:
            v = MMathC.truediv_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __floordiv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.floordiv_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.floordiv_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.floordiv_int(self.__data, other)
        else:
            v = MMathC.floordiv_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __mod__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.mod_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.mod_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.mod_int(self.__data, other)
        else:
            v = MMathC.mod_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __pow__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.pow_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.pow_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.pow_int(self.__data, other)
        else:
            v = MMathC.pow_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __lshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.lshift_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.lshift_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.lshift_int(self.__data, other)
        else:
            v = MMathC.lshift_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __rshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.rshift_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.rshift_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.rshift_int(self.__data, other)
        else:
            v = MMathC.rshift_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __and__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.and_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.and_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.and_int(self.__data, other)
        else:
            v = MMathC.and_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __dataor__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.dataor_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.dataor_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.dataor_int(self.__data, other)
        else:
            v = MMathC.dataor_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __or__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = MMathC.or_array(self.__data, other.__data)
        elif isinstance(other, np.ndarray):
            v = MMathC.or_array(self.__data, other)
        elif isinstance(other, int):
            v = MMathC.or_int(self.__data, other)
        else:
            v = MMathC.or_float(self.__data, other)
        v2 = self.__class__(v)
        v2.effective()
        return v2

    def __neg__(self):
        return self.__class__(-self.__data[0], -self.__data[1], -self.__data[2], -self.__data[3])

    def __pos__(self):
        return self.__class__(+self.__data[0], +self.__data[1], +self.__data[2], +self.__data[3])

    def __invert__(self):
        return self.__class__(~self.__data[0], ~self.__data[1], ~self.__data[2], ~self.__data[3])
    
    def x(self):
        return self.__data[0]

    def y(self):
        return self.__data[1]

    def z(self):
        return self.__data[2]
    
    def w(self):
        return self.__data[3]
    
    def setX(self, x):
        self.__data[0] = x

    def setY(self, y):
        self.__data[1] = y

    def setZ(self, z):
        self.__data[2] = z

    def setW(self, w):
        self.__data[3] = w


class MQuaternion():

    def __init__(self, w=1, x=0, y=0, z=0):
        if isinstance(w, MQuaternion):
            # クラスの場合
            self.__data = w.__data
        elif isinstance(w, np.quaternion):
            # quaternionの場合
            self.__data = w
        elif isinstance(w, np.ndarray):
            # arrayそのものの場合
            self.__data = np.quaternion(w[0], w[1], w[2], w[3])
        else:
            self.__data = np.quaternion(w, x, y, z)

    def copy(self):
        return MQuaternion(self.scalar(), self.x(), self.y(), self.z())
    
    def __str__(self):
        return "MQuaternion({0}, {1}, {2}, {3})".format(self.__data.w, self.__data.x, self.__data.y, self.__data.z)

    def inverted(self):
        v = self.__data.inverse()
        return self.__class__(v.w, v.x, v.y, v.z)

    def length(self):
        return self.__data.abs()

    def lengthSquared(self):
        return self.__data.abs()**2

    def normalized(self):
        self.effective()
        v = self.__data.normalized()
        return MQuaternion(v.w, v.x, v.y, v.z)

    def normalize(self):
        self.__data = self.__data.normalized()

    def effective(self):
        self.__data.components[np.isnan(self.__data.components)] = 0
        self.__data.components[np.isinf(self.__data.components)] = 0
        # Scalarは1がデフォルトとなる
        self.setScalar(1 if self.scalar() == 0 else self.scalar())

    def toMatrix4x4(self):
        m = MMathC.toMatrix4x4_MQuaternion(self.__data.components)
        mat = MMatrix4x4(m)

        return mat
    
    def toVector4D(self):
        return MVector4D(self.__data.x, self.__data.y, self.__data.z, self.__data.w)

    def toEulerAngles4MMD(self):
        # MMDの表記に合わせたオイラー角
        euler = self.toEulerAngles()

        return MVector3D(euler.x(), -euler.y(), -euler.z())

    # http://www.j3d.org/matrix_faq/matrfaq_latest.html#Q37
    def toEulerAngles(self):
        v = MVector3D(MMathC.toEulerAngles(self.__data.components))

        return v
    
    # 角度に変換
    def toDegree(self):
        return MMathC.toDegree(self.__data.components)

    # 自分ともうひとつの値vとのtheta（変位量）を返す
    def calcTheata(self, v):
        return MMathC.calcTheata_MQuaternion(self.__data.components, v.__data.components)
    
    @classmethod
    def dotProduct(cls, v1, v2):
        return MMathC.dotProduct_MQuaternion(v1.__data.components, v2.__data.components)
    
    @classmethod
    def fromAxisAndAngle(cls, vec3: MVector3D, angle: float):
        return MQuaternion(MMathC.fromAxisAndAngle(vec3.data(), angle)).normalized()

    @classmethod
    def fromAxisAndQuaternion(cls, vec3: MVector3D, qq):
        qq.normalize()
        return MQuaternion(MMathC.fromAxisAndQuaternion(vec3.data(), qq.__data.components)).normalized()

    @classmethod
    def fromDirection(cls, direction, up):
        if direction.is_almost_null():
            return MQuaternion()

        zAxis = direction.normalized()
        xAxis = MVector3D.crossProduct(up, zAxis)
        if (is_almost_null(xAxis.lengthSquared())):
            # collinear or invalid up vector derive shortest arc to new direction
            return MQuaternion.rotationTo(MVector3D(0.0, 0.0, 1.0), zAxis)
        
        xAxis.normalize()
        yAxis = MVector3D.crossProduct(zAxis, xAxis)
        return MQuaternion.fromAxes(xAxis, yAxis, zAxis)
    
    @classmethod
    def fromAxes(cls, xAxis, yAxis, zAxis):
        rot3x3 = np.array([[xAxis.x(), yAxis.x(), zAxis.x()], [xAxis.y(), yAxis.y(), zAxis.y()], [xAxis.z(), yAxis.z(), zAxis.z()]], dtype=np.float64)
        return MQuaternion.fromRotationMatrix(rot3x3)
    
    @classmethod
    def fromRotationMatrix(cls, rot3x3):
        scalar = 0
        axis = np.zeros(3)

        trace = rot3x3[0][0] + rot3x3[1][1] + rot3x3[2][2]
        if trace > 0.00000001:
            s = 2.0 * math.sqrt(trace + 1.0)
            scalar = 0.25 * s
            axis[0] = (rot3x3[2][1] - rot3x3[1][2]) / s
            axis[1] = (rot3x3[0][2] - rot3x3[2][0]) / s
            axis[2] = (rot3x3[1][0] - rot3x3[0][1]) / s
        else:
            s_next = np.array([1, 2, 0], dtype=np.int8)
            i = 0
            if rot3x3[1][1] > rot3x3[0][0]:
                i = 1
            if rot3x3[2][2] > rot3x3[i][i]:
                i = 2

            j = s_next[i]
            k = s_next[j]

            s = 2.0 * math.sqrt(rot3x3[i][i] - rot3x3[j][j] - rot3x3[k][k] + 1.0)
            axis[i] = 0.25 * s

            scalar = (rot3x3[k][j] - rot3x3[j][k]) / s
            axis[j] = (rot3x3[j][i] + rot3x3[i][j]) / s
            axis[k] = (rot3x3[k][i] + rot3x3[i][k]) / s

        return MQuaternion(scalar, axis[0], axis[1], axis[2])

    @classmethod
    def rotationTo(cls, fromv, tov):
        v0 = fromv.normalized()
        v1 = tov.normalized()
        d = MVector3D.dotProduct(v0, v1) + 1.0

        # if dest vector is close to the inverse of source vector, ANY axis of rotation is valid
        if is_almost_null(d):
            axis = MVector3D.crossProduct(MVector3D(1.0, 0.0, 0.0), v0)
            if is_almost_null(axis.lengthSquared()):
                axis = MVector3D.crossProduct(MVector3D(0.0, 1.0, 0.0), v0)
            axis.normalize()
            # same as MQuaternion.fromAxisAndAngle(axis, 180.0)
            return MQuaternion(0.0, axis.x(), axis.y(), axis.z()).normalized()

        d = math.sqrt(2.0 * d)
        axis = MVector3D.crossProduct(v0, v1) / d
        return MQuaternion(d * 0.5, axis.x(), axis.y(), axis.z()).normalized()
    
    @classmethod
    def fromEulerAngles(cls, pitch, yaw, roll):
        pitch = math.radians(pitch)
        yaw = math.radians(yaw)
        roll = math.radians(roll)

        pitch *= 0.5
        yaw *= 0.5
        roll *= 0.5

        c1 = math.cos(yaw)
        s1 = math.sin(yaw)
        c2 = math.cos(roll)
        s2 = math.sin(roll)
        c3 = math.cos(pitch)
        s3 = math.sin(pitch)
        c1c2 = c1 * c2
        s1s2 = s1 * s2
        w = c1c2 * c3 + s1s2 * s3
        x = c1c2 * s3 + s1s2 * c3
        y = s1 * c2 * c3 - c1 * s2 * s3
        z = c1 * s2 * c3 - s1 * c2 * s3

        return MQuaternion(w, x, y, z)
    
    @classmethod
    def nlerp(cls, q1, q2, t):
        # Handle the easy cases first.
        if t <= 0.0:
            return q1
        elif t >= 1.0:
            return q2
            
        # Determine the angle between the two quaternions.
        q2b = MQuaternion(q2.scalar(), q2.x(), q2.y(), q2.z())
        
        dot = MQuaternion.dotProduct(q1, q2)
        if dot < 0.0:
            q2b = -q2b
        
        # Perform the linear interpolation.
        return (q1 * (1.0 - t) + q2b * t).normalized()

    @classmethod
    def slerp(cls, q1, q2, t):
        # Handle the easy cases first.
        if t <= 0.0:
            return q1
        elif t >= 1.0:
            return q2

        # Determine the angle between the two quaternions.
        q2b = MQuaternion(q2.scalar(), q2.x(), q2.y(), q2.z())
        dot = MQuaternion.dotProduct(q1, q2)
        
        if dot < 0.0:
            q2b = -q2b
            dot = -dot

        # Get the scale factors.  If they are too small,
        # then revert to simple linear interpolation.
        factor1 = 1.0 - t
        factor2 = t

        if (1.0 - dot) > 0.0000001:
            angle = math.acos(max(0, min(1, dot)))
            sinOfAngle = math.sin(angle)
            if sinOfAngle > 0.0000001:
                factor1 = math.sin((1.0 - t) * angle) / sinOfAngle
                factor2 = math.sin(t * angle) / sinOfAngle

        # Construct the result quaternion.
        return q1 * factor1 + q2b * factor2
    
    def x(self):
        return self.__data.x

    def y(self):
        return self.__data.y

    def z(self):
        return self.__data.z

    def scalar(self):
        return self.__data.w

    def vector(self):
        return MVector3D(self.__data.x, self.__data.y, self.__data.z)

    def setX(self, x):
        self.__data.x = x

    def setY(self, y):
        self.__data.y = y

    def setZ(self, z):
        self.__data.z = z

    def setScalar(self, w):
        self.__data.w = w
    
    def data(self):
        return self.__data

    def __lt__(self, other):
        return np.all(self.__data < other.__data)

    def __le__(self, other):
        return np.all(self.__data <= other.__data)

    def __eq__(self, other):
        return np.all(self.__data == other.__data)

    def __ne__(self, other):
        return np.any(self.__data != other.__data)

    def __gt__(self, other):
        return np.all(self.__data > other.__data)

    def __ge__(self, other):
        return np.all(self.__data >= other.__data)

    def __add__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data + other.__data
        else:
            v = self.__data + other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __sub__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data - other.__data
        else:
            v = self.__data - other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __mul__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data * other.__data
            return self.__class__(v)
        elif isinstance(other, MVector3D):
            v = self.toMatrix4x4() * other
            return v
        else:
            v = self.__data * other
            return self.__class__(v.w, v.x, v.y, v.z)

    def __truediv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data / other.__data
        else:
            v = self.__data / other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __floordiv__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data // other.__data
        else:
            v = self.__data // other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __mod__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data % other.__data
        else:
            v = self.__data % other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __pow__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data ** other.__data
        else:
            v = self.__data ** other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __lshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data << other.__data
        else:
            v = self.__data << other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __rshift__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data >> other.__data
        else:
            v = self.__data >> other
        return self.__class__(v.w, v.x, v.y, v.z)

    def __and__(self, other):
        v = self.__data & other.__data
        return self.__class__(v.w, v.x, v.y, v.z)

    def __dataor__(self, other):
        v = self.__data ^ other.__data
        return self.__class__(v.w, v.x, v.y, v.z)

    def __or__(self, other):
        v = self.__data | other.__data
        return self.__class__(v.w, v.x, v.y, v.z)
    
    def __neg__(self):
        return self.__class__(-self.__data.w, -self.__data.x, -self.__data.y, -self.__data.z)

    def __pos__(self):
        return self.__class__(+self.__data.w, +self.__data.x, +self.__data.y, +self.__data.z)

    def __invert__(self):
        return self.__class__(~self.__data.w, ~self.__data.x, ~self.__data.y, ~self.__data.z)


class MMatrix4x4():
    
    def __init__(self, m11=1, m12=0, m13=0, m14=0, m21=0, m22=1, m23=0, m24=0, m31=0, m32=0, m33=1, m34=0, m41=0, m42=0, m43=0, m44=1):
        if isinstance(m11, MMatrix4x4):
            # 行列クラスの場合
            self.__data = np.array([[m11.__data[0, 0], m11.__data[0, 1], m11.__data[0, 2], m11.__data[0, 3]], \
                                    [m11.__data[1, 0], m11.__data[1, 1], m11.__data[1, 2], m11.__data[1, 3]], \
                                    [m11.__data[2, 0], m11.__data[2, 1], m11.__data[2, 2], m11.__data[2, 3]], \
                                    [m11.__data[3, 0], m11.__data[3, 1], m11.__data[3, 2], m11.__data[3, 3]]], dtype=np.float64)
        elif isinstance(m11, np.ndarray):
            # 行列そのものの場合
            self.__data = np.array([[m11[0, 0], m11[0, 1], m11[0, 2], m11[0, 3]], [m11[1, 0], m11[1, 1], m11[1, 2], m11[1, 3]], \
                                    [m11[2, 0], m11[2, 1], m11[2, 2], m11[2, 3]], [m11[3, 0], m11[3, 1], m11[3, 2], m11[3, 3]]], dtype=np.float64)
        else:
            # べた値の場合
            self.__data = np.array([[m11, m12, m13, m14], [m21, m22, m23, m24], [m31, m32, m33, m34], [m41, m42, m43, m44]], dtype=np.float64)

    def copy(self):
        return MMatrix4x4(self.__data)

    def data(self):
        return self.__data
    
    # 逆行列
    def inverted(self):
        return MMatrix4x4(MMathC.inverted(self.__data))

    # 回転行列
    def rotate(self, qq):
        qq_mat = qq.toMatrix4x4()
        self.__data = MMathC.dot2(self.__data, qq_mat.__data)

    # 平行移動行列
    def translate(self, vec3):
        self.__data = MMathC.translate_MMatrix4x4(self.__data, vec3.data())

    # 縮尺行列
    def scale(self, vec3):
        self.__data = MMathC.scale_MMatrix4x4(self.__data, vec3.data())
        
    # 単位行列
    def setToIdentity(self):
        self.__data = MMathC.eye()
    
    def lookAt(self, eye, center, up):
        forward = center - eye
        if forward.is_almost_null():
            # ほぼ0の場合終了
            return
        
        forward.normalize()
        side = MVector3D.crossProduct(forward, up).normalized()
        upVector = MVector3D.crossProduct(side, forward)

        m = MMatrix4x4()
        m.__data[0, :-1] = side.data()
        m.__data[1, :-1] = upVector.data()
        m.__data[2, :-1] = -forward.data()
        m.__data[-1, -1] = 1.0

        self *= m
        self.translate(-eye)
    
    def perspective(self, verticalAngle, aspectRatio, nearPlane, farPlane):
        if nearPlane == farPlane or aspectRatio == 0:
            return

        radians = math.radians(verticalAngle / 2)
        sine = math.sin(radians)

        if sine == 0:
            return
        
        cotan = math.cos(radians) / sine
        clip = farPlane - nearPlane

        m = MMatrix4x4()
        m.__data[0, 0] = cotan / aspectRatio
        m.__data[1, 1] = cotan
        m.__data[2, 2] = -(nearPlane + farPlane) / clip
        m.__data[2, 3] = -(2 * nearPlane * farPlane) / clip
        m.__data[3, 2] = -1

        self *= m
    
    def mapVector(self, vector):
        vec_mat = np.array([vector.x(), vector.y(), vector.z()])
        xyz = np.sum(vec_mat * self.__data[:3, :3], axis=1)

        return MVector3D(xyz[0], xyz[1], xyz[2])
    
    def toQuaternion(self):
        a = [[self.__data[0, 0], self.__data[0, 1], self.__data[0, 2], self.__data[0, 3]],
             [self.__data[1, 0], self.__data[1, 1], self.__data[1, 2], self.__data[1, 3]],
             [self.__data[2, 0], self.__data[2, 1], self.__data[2, 2], self.__data[2, 3]],
             [self.__data[3, 0], self.__data[3, 1], self.__data[3, 2], self.__data[3, 3]]]
        
        q = MQuaternion()
        
        # I removed + 1
        trace = a[0][0] + a[1][1] + a[2][2]
        # I changed M_EPSILON to 0
        if trace > 0:
            s = 0.5 / math.sqrt(trace + 1)
            q.setScalar(0.25 / s)
            q.setX((a[2][1] - a[1][2]) * s)
            q.setY((a[0][2] - a[2][0]) * s)
            q.setZ((a[1][0] - a[0][1]) * s)
        else:
            if a[0][0] > a[1][1] and a[0][0] > a[2][2]:
                s = 2 * math.sqrt(1 + a[0][0] - a[1][1] - a[2][2])
                q.setScalar((a[2][1] - a[1][2]) / s)
                q.setX(0.25 * s)
                q.setY((a[0][1] + a[1][0]) / s)
                q.setZ((a[0][2] + a[2][0]) / s)
            elif a[1][1] > a[2][2]:
                s = 2 * math.sqrt(1 + a[1][1] - a[0][0] - a[2][2])
                q.setScalar((a[0][2] - a[2][0]) / s)
                q.setX((a[0][1] + a[1][0]) / s)
                q.setY(0.25 * s)
                q.setZ((a[1][2] + a[2][1]) / s)
            else:
                s = 2 * math.sqrt(1 + a[2][2] - a[0][0] - a[1][1])
                q.setScalar((a[1][0] - a[0][1]) / s)
                q.setX((a[0][2] + a[2][0]) / s)
                q.setY((a[1][2] + a[2][1]) / s)
                q.setZ(0.25 * s)

        return q

    def __str__(self):
        return "MMatrix4x4({0})".format(self.__data)

    def __lt__(self, other):
        return np.all(self.__data < other.__data)

    def __le__(self, other):
        return np.all(self.__data <= other.__data)

    def __eq__(self, other):
        return np.all(self.__data == other.__data)

    def __ne__(self, other):
        return np.any(self.__data != other.__data)

    def __gt__(self, other):
        return np.all(self.__data > other.__data)

    def __ge__(self, other):
        return np.all(self.__data >= other.__data)

    def __add__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data + other.__data
        else:
            v = self.__data + other
        return self.__class__(v)

    def __sub__(self, other):
        if isinstance(other, MVector2D) or isinstance(other, MVector3D) or isinstance(other, MVector4D) or isinstance(other, MQuaternion) or isinstance(other, MMatrix4x4):
            v = self.__data - other.__data
        else:
            v = self.__data - other
        return self.__class__(v)

    # *演算子
    def __mul__(self, other):
        if isinstance(other, MVector3D):
            vec_mat = np.tile(np.array([other.x(), other.y(), other.z()]), (4, 1))
            data_sum = np.sum(vec_mat * self.__data[:, :3], axis=1) + self.__data[:, 3]

            x = data_sum[0]
            y = data_sum[1]
            z = data_sum[2]
            w = data_sum[3]

            if w == 1.0:
                return MVector3D(x, y, z)
            elif w == 0.0:
                return MVector3D()
            else:
                return MVector3D(x / w, y / w, z / w)
        elif isinstance(other, MVector4D):
            vec_mat = np.tile(np.array([other.x(), other.y(), other.z(), other.w()]), (4, 1))
            data_sum = np.sum(vec_mat * self.__data, axis=1)

            x = data_sum[0]
            y = data_sum[1]
            z = data_sum[2]
            w = data_sum[3]

            return MVector4D(x, y, z, w)
        elif isinstance(other, MMatrix4x4):
            v = np.dot(self.__data, other.__data)
            return self.__class__(v)
        
        v = self.__data * other
        return self.__class__(v)
        
    def __iadd__(self, other):
        self.__data = self.__data + other.__data.T
        return self

    def __isub__(self, other):
        self.__data = self.__data + other.__data.T
        return self

    def __imul__(self, other):
        self.__data = np.dot(self.__data, other.__data)

        return self

    def __itruediv__(self, other):
        self.__data = self.__data / other.__data.T
        return self


def is_almost_null(v):
    return abs(v) < 0.0000001


def get_effective_value(v):
    if math.isnan(v):
        return 0
    
    if math.isinf(v):
        return 0
    
    return v


def get_almost_zero_value(v):
    if get_effective_value(v) == 0:
        return 0
        
    if is_almost_null(v):
        return 0

    return v


