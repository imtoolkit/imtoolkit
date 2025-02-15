.. imtoolkit documentation master file, created by
   sphinx-quickstart on Tue Apr 23 15:53:04 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=========
Overview
=========

.. image:: https://github.com/imtoolkit/imtoolkit/blob/master/docs/source/_static/imtoolkit-logo.png?raw=true
   :height: 150px
   :width: 150px
   :alt: IMToolkit logo.
   :target: https://ishikawa.cc/imtoolkit/
   :align: right

This webpage introduces an open-source index modulation toolkit (IMToolkit).
This toolkit attempts to facilitate reproducible research in wireless communications.
The major advantages of this toolkit are highlighted as follows:

- It accelerates bit error ratio and average mutual information simulations by relying on a state-of-the-art Nvidia GPU and the massively parallel algorithms proposed in [1].
- It also supports the representative multiplexing schemes for ideal MIMO and OFDM scenarios, in addition to the IM family.
- It contains :doc:`a comprehensive database<db/index>` of designed active indices, that determine the achievable performance of the generalized spatial modulation or the subcarrier-index modulation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   self
   tutorial/index
   db/index
   Modules <module/modules>

Installation Guide
==================

IMToolkit is available from the Python official package repository `PyPi <https://pypi.org/project/imtoolkit/>`_.

.. code-block:: bash

    > pip install imtoolkit

This installation requires NumPy, Pandas, SciPy, SymPy, Numba, and tqdm, all of which are popular Python packages.
Additionally, it is strongly recommended to install `CuPy <https://cupy.chainer.org/>`_ 5.40+. 
IMToolkit is heavily dependent on CuPy to achieve significantly fast Monte-Carlo simulations.
`The key components required by CuPy are listed here. <https://docs-cupy.chainer.org/en/stable/install.html>`_
In case CuPy is not installed in your environment, IMToolkit uses NumPy only.
Note that the CuPy-based simulation is 145 times faster than the NumPy-based calculation, as reported in [1].

`The above PyPi package <https://pypi.org/project/imtoolkit/>`_ excluded the designed active indices due to their large file size, which exceeds 500MB.
Hence, this reduced-size PyPi package will automatically download a required file from `the GitHub repository <https://github.com/imtoolkit/imtoolkit>`_ or a mirror website.
If you need all the project files, to use `imtoolkit` offline, it is recommended to obtain the package from GitHub as follows:

.. code-block:: bash

    > pip install git+https://github.com/imtoolkit/imtoolkit

The IMToolkit development team welcomes other researchers' contributions and pull requests.
In that case, it would be better to install the latest package and activate the editable mode as follows:

.. code-block:: bash

    > git clone https://github.com/imtoolkit/imtoolkit
    > pip install -e ./imtoolkit # this activates the editable mode


How to Use
==========
- :doc:`A detailed tutorial for the imtoolkit command and APIs. <tutorial/index>`
- :doc:`A comprehensive database of the designed active indices. <db/index>`

Citations
=========
It would be very appreciated if you cite the following references when using IMToolkit.

- [1] N. Ishikawa, "`IMToolkit: An open-source index modulation toolkit for reproducible research based on massively parallel algorithms <https://doi.org/10.1109%2Faccess.2019.2928033>`_," IEEE Access, vol. 7, pp. 93830--93846, July 2019.

Of course, if your project relies on CuPy, the following reference is highly recommended.

- [2] R. Okuta, Y. Unno, D. Nishino, S. Hido, and C. Loomis, "`CuPy: A NumPy-compatible library for NVIDIA GPU calculations <http://learningsys.org/nips17/assets/papers/paper_16.pdf>`_," in Conference on Neural Information Processing Systems Workshop, Long Beach, CA, USA, December 4--9, 2017.

Contributor(s)
==============

- Naoki Ishikawa (`Web <https://ishikawa.cc>`_ / `Google Scholar <https://scholar.google.co.jp/citations?user=JHnisGYAAAAJ>`_ / `ResearchGate <https://www.researchgate.net/profile/Naoki_Ishikawa>`_ / `Publons <https://publons.com/researcher/3012020/naoki-ishikawa/>`_)
- You might become a valuable contributor of this project. Any contributions and issues are appreciated.


.. Indices and tables
.. ==================
.. 
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
