import numpy as np

np.set_printoptions(precision=7)
def imped2seq(Z_abc):
    a = np.exp(1j*np.deg2rad(120))
    A = np.array([
        [1., 1., 1.],
        [1., a**2, a],
        [1., a, a**2]
    ])
    return np.linalg.inv(A).dot(Z_abc).dot(A)

# Config 300
Z_abc = np.array([
    [1.3368+1j*1.3343, 0.2101+1j*0.5779, 0.2130+1j*0.5015],
    [0.2101+1j*0.5779, 1.3238+1j*1.3569, 0.2066+1j*0.4591],
    [0.2130+1j*0.5015, 0.2066+1j*0.4591, 1.3294+1j*1.3471]
]) # ohms/mile
B_abc = np.array([
    [5.3350,  -1.5313, -0.9943],
    [-1.5313,  5.0979, -0.6212],
    [-0.9943, -0.6212,  4.8880],
]) # micro Siemens /mile

Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 1
Z_abc = np.array([
    [0.4576+1j*1.0780, 0.1560+1j*0.5017, 0.1535+1j*0.3849],
    [0.1560+1j*0.5017, 0.4666+1j*1.0482, 0.1580+1j*0.4236],
    [0.1535+1j*0.3849, 0.1580+1j*0.4236, 0.4615+1J*1.0651]
])
B_abc = np.array([
    [5.6765,  -1.8319, -0.6982],
    [-1.8319,  5.9809, -1.1645],
    [-0.6982, -1.1645,  5.3971]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 2
Z_abc = np.array([
    [0.4666+1j*1.0482, 0.1580+1j*0.4236, 0.1560+1j*0.5017],
    [0.1580+1j*0.4236, 0.4615+1j*1.0651, 0.1535+1j*0.3849],
    [0.1560+1j*0.5017, 0.1535+1j*0.3849, 0.4576+1j*1.0780]
])
B_abc = np.array([
    [5.9809,  -1.1645, -1.8319],
    [-1.1645,  5.3971, -0.6982],
    [-1.8319, -0.6982,  5.6765]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 3
Z_abc = np.array([
    [0.4615+1j*1.0651, 0.1535+1j*0.3849, 0.1580+1j*0.4236],
    [0.1535+1j*0.3849, 0.4576+1j*1.0780, 0.1560+1j*0.5017],
    [0.1580+1j*0.4236, 0.1560+1j*0.5017, 0.4666+1j*1.0482]
])
B_abc = np.array([
    [5.3971, -0.6982, -1.1645],
    [-0.6982, 5.6765, -1.8319],
    [-1.1645,-1.8319,  5.9809]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 4
Z_abc = np.array([
    [0.4615+1j*1.0651, 0.1580+1j*0.4236, 0.1535+1j*0.3849],
    [0.1580+1j*0.4236, 0.4666+1j*1.0482, 0.1560+1j*0.5017],
    [0.1535+1j*0.3849, 0.1560+1j*0.5017, 0.4576+1j*1.0780]
])
B_abc = np.array([
    [5.3971, -1.1645, -0.6982],
    [-1.1645, 5.9809, -1.8319],
    [-0.6982,-1.8319,  5.6765]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 5
Z_abc = np.array([
    [0.4666+1j*1.0482, 0.1560+1j*0.5017, 0.1580+1j*0.4236],
    [0.1560+1j*0.5017, 0.4576+1j*1.0780, 0.1535+1j*0.3849],
    [0.1580+1j*0.4236, 0.1535+1j*0.3849, 0.4615+1j*1.0651]
])
B_abc = np.array([
    [5.9809, -1.8319, -1.1645]
    [-1.8319, 5.6765, -0.6982]
    [-1.1645,-0.6982,  5.3971]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 6
Z_abc = np.array([
    [0.4576+1j*1.0780, 0.1535+1j*0.3849, 0.1560+1j*0.5017],
    [0.1535+1j*0.3849, 0.4615+1j*1.0651, 0.1580+1j*0.4236],
    [0.1560+1j*0.5017, 0.1580+1j*0.4236, 0.4666+1j*1.0482]
])
B_abc = np.array([
    [5.6765, -0.6982, -1.8319],
    [-0.6982, 5.3971, -1.1645],
    [-1.8319,-1.1645,  5.9809]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 7
Z_abc = np.array([
    [0.4576+1j*1.0780, 0.0000+1j*0.0000, 0.1535+1j*0.3849],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000],
    [0.1535+1j*0.3849, 0.0000+1j*0.0000, 0.4615+1j*1.0651]
])
B_abc = np.array([
    [5.1154, 0.0000, -1.0549],
    [0.0000, 0.0000,  0.0000],
    [-1.0549,0.0000,  5.1704],
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 8
Z_abc = np.array([
    [0.4576+1j*1.0780, 0.1535+1j*0.3849, 0.0000+1j*0.0000],
    [0.1535+1j*0.3849, 0.4615+1j*1.0651, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000]
])
B_abc = np.array([
    [5.1154, -1.0549, 0.0000],
    [-1.0549, 5.1704, 0.0000],
    [0.0000,  0.0000, 0.0000]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 9
Z_abc = np.array([
    [1.3292+1j*1.3475, 0.0000+1j*0.0000, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000]
])
B_abc = np.array([
    [4.5193, 0.0000, 0.0000],
    [0.0000, 0.0000, 0.0000],
    [0.0000, 0.0000, 0.0000]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 10
Z_abc = np.array([
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 1.3292+1j*1.3475, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000]
])
B_abc = np.array([
    [0.0000, 0.0000, 0.0000],
    [0.0000, 4.5193, 0.0000],
    [0.0000, 0.0000, 0.0000]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 11
Z_abc = np.array([
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 0.0000+1j*0.0000],
    [0.0000+1j*0.0000, 0.0000+1j*0.0000, 1.3292+1j*1.3475]
])
B_abc = np.array([
    [0.0000, 0.0000, 0.0000],
    [0.0000, 0.0000, 0.0000],
    [0.0000, 0.0000, 4.5193]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))

# Config 12
Z_abc = np.array([
    [1.5209+1j*0.7521, 0.5198+1j*0.2775, 0.4924+1j*0.2157],
    [0.5198+1j*0.2775, 1.5329+1j*0.7162, 0.5198+1j*0.2775],
    [0.4924+1j*0.2157, 0.5198+1j*0.2775, 1.5209+1j*0.7521]
])
B_abc = np.array([
    [67.2242, 0.0000, 0.0000],
    [0.0000, 67.2242, 0.0000],
    [0.0000,  0.0000, 67.2242]
])
Z_012 = imped2seq(Z_abc) / 1.609344 # ohms/km
B_012 = imped2seq(B_abc) / 1.609344 # micro Siemens/km
print('c1: {}'.format(B_012[1,1].real))
print('r1: {}'.format(Z_012[1,1].real))
print('x1: {}'.format(Z_012[1,1].imag))
print('c0: {}'.format(B_012[0,0].real))
print('r0: {}'.format(Z_012[0,0].real))
print('x0: {}'.format(Z_012[0,0].imag))
