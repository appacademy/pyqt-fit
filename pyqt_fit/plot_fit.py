"""
:Author: Pierre Barbier de Reuille <pierre.barbierdereuille@gmail.com>

This modules implement functions to test and plot parametric regression.
"""

import matplotlib
matplotlib.use('Agg')
from __future__ import division, print_function, absolute_import
from numpy import argsort, std, abs, sqrt, arange, pi, c_, asarray
from .compat import izip
from itertools import chain
from scipy.special import erfinv, gamma
from scipy import stats
#from .kernel_smoothing import LocalLinearKernel1D
from .nonparam_regression import NonParamRegression
from .compat import unicode_csv_writer as csv_writer
from collections import namedtuple

import sys
if sys.version_info >= (3,):
    CSV_WRITE_FLAGS = "wt"
else:
    CSV_WRITE_FLAGS = "wb"


def plot_dist_residuals(res):
    return None

def plot_residuals(xname, xdata, res_desc, res):
    return None


def scaled_location_plot(yname, yopt, scaled_res):
    return None


def qqplot(scaled_res, normq):
    return None

ResultStruct = namedtuple('ResultStruct', "fct fct_desc param_names xdata ydata xname yname "
                          "res_name residuals popt res yopts eval_points interpolation "
                          "sorted_yopts scaled_res normq CI CIs CIresults")


def fit_evaluation(fit, xdata, ydata, eval_points=None,
                   CI=(), CIresults = None, xname="X", yname="Y",
                   fct_desc=None, param_names=(), residuals=None, res_name='Standard'):
    """
    This function takes the output of a curve fitting experiment and store all the relevant
    information for evaluating its success in the result.

    :type  fit: fitting object
    :param fit: object configured for the fitting

    :type  xdata: ndarray of shape (N,) or (k,N) for function with k prefictors
    :param xdata: The independent variable where the data is measured

    :type  ydata: ndarray
    :param ydata: The dependant data

    :type  eval_points: ndarray or None
    :param eval_points: Contain the list of points on which the result must be expressed. It is
        used both for plotting and for the bootstrapping.

    :type  CI: tuple of int
    :param CI: List of confidence intervals to calculate. If empty, none are calculated.

    :type  xname: string
    :param xname: Name of the X axis

    :type  yname: string
    :param yname: Name of the Y axis

    :type  fct_desc: string
    :param fct_desc: Formula of the function

    :type  param_names: tuple of strings
    :param param_names: Name of the various parameters

    :type  residuals: callable
    :param residuals: Residual function

    :type  res_desc: string
    :param res_desc: Description of the residuals

    :rtype: :py:class:`ResultStruct`
    :returns: Data structure summarising the fitting and its evaluation
    """
    return None

ResidualMeasures = namedtuple("ResidualMeasures", "scaled_res res_IX prob normq")


def residual_measures(res):
    """
    Compute quantities needed to evaluate the quality of the estimation, based solely
    on the residuals.

    :rtype: :py:class:`ResidualMeasures`
    :returns: the scaled residuals, their ordering, the theoretical quantile for each residuals,
        and the expected value for each quantile.
    """
    return None

_restestfields = "res_figure residuals scaled_residuals qqplot dist_residuals"
ResTestResult = namedtuple("ResTestResult", _restestfields)
Plot1dResult = namedtuple("Plot1dResult", "figure estimate data CIs " + _restestfields)


def plot1d(result, loc=0, fig=None, res_fig=None):
    """
    Use matplotlib to display the result of a fit, and return the list of plots used

    :rtype: :py:class:`Plot1dResult`
    :returns: hangles to the various figures and plots
    """
    return None


def plot_residual_tests(xdata, yopts, res, fct_name, xname="X", yname='Y', res_name="residuals",
                        sorted_yopts=None, scaled_res=None, normq=None, fig=None):
    """
    Plot, in a single figure, all four residuals evaluation plots: :py:func:`plot_residuals`,
    :py:func:`plot_dist_residuals`, :py:func:`scaled_location_plot` and :py:func:`qqplot`.

    :param ndarray xdata:        Explaining variables
    :param ndarray yopt:         Optimized explained variables
    :param str     fct_name:     Name of the fitted function
    :param str     xname:        Name of the explaining variables
    :param str     yname:        Name of the dependant variables
    :param str     res_name:     Name of the residuals
    :param ndarray sorted_yopts: ``yopt``, sorted to match the scaled residuals
    :param ndarray scaled_res:   Scaled residuals
    :param ndarray normq:        Estimated value of the quantiles for a normal distribution

    :type  fig: handle or None
    :param fig: Handle of the figure to put the plots in, or None to create a new figure

    :rtype: :py:class:`ResTestResult`
    :returns: The handles to all the plots
    """
    return None


def write1d(outfile, result, res_desc, CImethod):
    """
    Write the result of a fitting and its evaluation to a CSV file.

    :param str          outfile:  Name of the file to write to
    :param ResultStruct result:   Result of the fitting evaluation
        (e.g. output of :py:func:`fit_evaluation`)
    :param str          res_desc: Description of the residuals
        (in more details than just the name of the residuals)
    :param str          CImethod: Description of the confidence interval estimation method
    """
    return None


# /home/barbier/prog/python/curve_fitting/test.csv
