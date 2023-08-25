# Computational aspects of the equivalent-layer technique: review

Review about computational aspects of the equivalent-layer technique to be submitted for [Frontiers in Earth Science](https://www.frontiersin.org/journals/earth-science).

##### Authors:

[Vanderlei C. Oliveira Jr.](https://orcid.org/0000-0002-6338-4086)<sup>1</sup>, [Diego Takahashi](https://orcid.org/0000-0002-5237-6558)<sup>1</sup>, [André L. A. Reis](https://orcid.org/0000-0002-2225-5106)<sup>2</sup> and [Valéria C. F. Barbosa](https://orcid.org/0000-0002-9767-6044)<sup>1</sup>

<sup>1</sup>*[Observatório Nacional](https://www.gov.br/observatorio/pt-br), Brazil*

<sup>2</sup>*[Universidade do Estado do Rio de Janeiro (UERJ)](https://www.fgel.uerj.br/departamentos/depto-de-geologia-aplicada/dgap-quadro-de-pessoal/), Brazil*


##### Abstract

Equivalent-layer technique is a powerful tool for processing potential-field data in the space domain. However, the greatest hindrance for using the equivalent-layer technique is its high computational cost for processing massive data sets. The  large amount of computer memory usage to store the full  sensitivity matrix combined with the computational time required for matrix-vector multiplications and to solve the resulting linear system, are the main  drawbacks that made unfeasible the use of the equivalent-layer technique for a long time. More recently, the advances in computational power propelled the development of methods to overcome the heavy computational cost  associated with the equivalent-layer technique. We present  a comprehensive review of the computation aspects concerning the equivalent-layer technique addressing how previous works have been dealt with the computational cost of this technique. 
Historically, the high computational cost  of the equivalent-layer technique has been overcome by using a variety of strategies such as: moving data-window scheme,   column- and row-action updates of the 
sensitivity matrix, reparametrization, sparsity induction of the sensitivity matrix,  iterative methods using the full sensitivity matrix,  iterative deconvolution  by using the concept of  block-Toeplitz Toeplitz-block (BTTB) matrices and
direct deconvolution.
We compute the number of floating-point operations of some of these strategies adopted in the 
equivalent-layer technique to show their  effectiveness in reducing the computational demand. 
Numerically, we also address the stability of some of these strategies used in the equivalent-layer technique by comparing with the stability via the classic equivalent-layer technique with the zeroth-order Tikhonov regularization.
We show that even for the most computationally efficient methods, which can save up to $10^{9}$ flops, the stability of the linear system is maintained. 
The two most efficient strategies, iterative and direct deconvolutions, can process large datasets quickly and yield good results. 
However, direct deconvolution has some drawbacks. 
Real data from Carajás Mineral Province, Brazil, is also used to validate the results showing a potential field transformation.

##### Note

All results shown here were generated with the Python package **gravmag** (https://doi.org/10.5281/zenodo.8284769).
