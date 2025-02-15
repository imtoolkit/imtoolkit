# Copyright (c) IMToolkit Development Team
# This toolkit is released under the MIT License, see LICENSE.txt

import numpy as np
from .Modulator import Modulator


class ADSMCode(object):
    """Algebraic differential spatial modulation (ADSM), which was firstly proposed in [1] and was later extended in [2].

    - [1] R. Rajashekar, N. Ishikawa, S. Sugiura, K. V. S. Hari, and L. Hanzo, ``Full-diversity dispersion matrices from algebraic field extensions for differential spatial modulation,'' IEEE Trans. Veh. Technol., vol. 66, no. 1, pp. 385--394, 2017.

    - [2] R. Rajashekar, C. Xu, N. Ishikawa, S. Sugiura, K. V. S. Hari, and L. Hanzo, ``Algebraic differential spatial modulation is capable of approaching the performance of its coherent counterpart,'' IEEE Trans. Commun., vol. 65, no. 10, pp. 4260--4273, 2017.
    """

    def __init__(self, M, modtype, L, u_phase = -1):
        """
        Args:
            M (int): the number of transmit antennas.
            modtype (string): the constellation type.
            L (int): the constellation size.
            u_phase (float): the phase factor of dispersion matrices [0, pi]
        """
        self.M = M
        self.Nc = M * L
        self.B = np.log2(self.Nc)
        
        symbols = Modulator(modtype, L).symbols

        if u_phase == -1:
            u_phase = 2.0 * np.pi / L

        A = np.zeros((M, M), dtype=np.complex)
        A[0, M-1] = np.exp(1j * u_phase)
        for m in range(M-1):
            A[(m+1)%M, m] = 1
        
        As = np.zeros((M, M, M), dtype=np.complex) # M \times M \times M
        for m in range(M):
            As[m] = np.linalg.matrix_power(A, m)
        #print(As)
        
        codestensor = np.kron(symbols, As) # M \times M \times M * L (=Nc)
        self.codes = np.array(np.hsplit(np.hstack(codestensor), self.Nc)) # Nc \times M \times M

    def putRate(self):
        print("B / M = %d / %d = %d [bit/symbol]" % (self.B, self.M, self.B / self.M))

