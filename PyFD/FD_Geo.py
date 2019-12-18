from __future__ import division
from math import pow, sqrt, acos, sin, pi


def mean(l):
    sum = 0

    for v in l:
        sum += v

    return sum / len(l)


def angof2v(v1, v2):
    v1.unitize()
    v2.unitize()

    a1 = acos(v1.X)
    a2 = acos(v2.X)

    ad = a1 - a2

    if ad < 0: ad = -ad
    if ad > pi: ad = 2 * pi - ad

    return ad


def offsetp(p0, p, p2, dist, convex=True, outward=True):
    v1 = FD_vector(base=p, tip=p0)
    v2 = FD_vector(base=p, tip=p2)

    v1.unitize()
    v2.unitize()

    angle = angof2v(v1, v2) / 2

    move_dist = dist / sin(angle)

    move_vec = FD_vector((v1.X + v2.X) / 2, (v1.Y + v2.Y) / 2, (v1.Z + v2.Z) / 2)
    move_vec.unitize()
    move_vec.scale(move_dist)
    if convex: move_vec.reverse()
    if not outward: move_vec.reverse()
    return p.copy_move(move_vec)


class FD_point:

    def __init__(self, _x, _y, _z=0):
        self.X = _x
        self.Y = _y
        self.Z = _z

    def __repr__(self):
        return '\nPoint object \n' + 'X: ' + str(self.X) + '\n' + 'Y: ' + str(self.Y) + '\n' + 'Z: ' + str(
            self.Z) + '\n'

    def move(self, vec=None, _x=None, _y=None, _z=None):

        if vec is not None:
            _x = vec.X
            _y = vec.Y
            _z = vec.Z

        self.X += _x
        self.Y += _y
        self.Z += _z

    def copy_move(self, vec=None, _x=None, _y=None, _z=0):

        if vec is not None:
            _x = vec.X
            _y = vec.Y
            _z = vec.Z

        return FD_point(self.X + _x, self.Y + _y, self.Z + _z)

    def scale(self, scl, center=None):

        if center is None: center = FD_point(0, 0, 0)

        self.X = center.X + scl * (self.X - center.X)
        self.Y = center.Y + scl * (self.Y - center.Y)
        self.Z = center.Z + scl * (self.Z - center.Z)


class FD_vector(FD_point):

    def __init__(self, _x=None, _y=None, _z=None, base=None, tip=None):
        if base is not None and tip is not None:
            _x = tip.X - base.X
            _y = tip.Y - base.Y
            _z = tip.Z - base.Z

        FD_point.__init__(self, _x, _y, _z)

    def __repr__(self):
        return '\nVector object \n' + 'X: ' + str(self.X) + '\n' + 'Y: ' + str(self.Y) + '\n' + 'Z: ' + str(
            self.Z) + '\n'

    def unitize(self):
        length = sqrt(pow(self.X, 2) + pow(self.Y, 2) + pow(self.Z, 2))

        self.X = self.X / length
        self.Y = self.Y / length
        self.Z = self.Z / length

    def reverse(self):
        self.X = -self.X
        self.Y = -self.Y
        self.Z = -self.Z


class FD_Polyline(list):

    def __init__(self, point_list):

        list.__init__(self)

        for p in point_list:
            self.append(p)

    def __repr__(self):

        ps = []

        for p in self:
            cl = []
            cl.append(round(p.X, 4))
            cl.append(round(p.Y, 4))
            cl.append(round(p.Z, 4))
            ps.append(cl)

        between_lines = '-------------------------------------------\n'
        describe = '\n-------------------------------------------\n'
        describe = '|        |X:        |Y:        |Z:        |\n'
        describe += between_lines

        for i, p in enumerate(ps):
            row = '|Vertex' + str(i)
            for _ in range(9 - len(row)):
                row += ' '
            row += '|' + str(p[0])
            for _ in range(20 - len(row)):
                row += ' '
            row += '|' + str(p[1])
            for _ in range(31 - len(row)):
                row += ' '
            row += '|' + str(p[2])
            for _ in range(42 - len(row)):
                row += ' '
            row += '|\n'
            describe += row

        describe += '-------------------------------------------'
        return describe

    def move(self, vt):
        for p in self:
            p.move(vt)

    def scale(self, scl, center=None):

        if center is None:
            center = self.get_center_point()

        for p in self:
            p.scale(scl, center)

    def get_center_point(self):

        xs = []
        ys = []
        zs = []

        for p in self:
            xs.append(p.X)
            ys.append(p.Y)
            zs.append(p.Z)

        return FD_point(mean(xs), mean(ys), mean(zs))

    def get_normal_factor(self):

        nv = FD_vector(0, 0, 0)

        for i, p in enumerate(self):

            j = i + 1
            if j == len(self): j = 0

            nv.X += (self[i].Z + self[j].Z) * (self[i].Y - self[j].Y)
            nv.Y += (self[i].X + self[j].X) * (self[i].Z - self[j].Z)
            nv.Z += (self[i].Y + self[j].Y) * (self[i].X - self[j].X)

        nv.unitize()

        return nv

    def offset(self, distance, outward=True):

        f = FD_Polyline(point_list=[])

        for i, p in enumerate(self):

            _i = i + 1
            if _i == len(self): _i = 0

            f.append(offsetp(self[i - 1], p, self[_i], dist=distance, outward=outward))

        return f
