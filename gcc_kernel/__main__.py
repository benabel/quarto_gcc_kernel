from ipykernel.kernelapp import IPKernelApp
from . import GccKernel

IPKernelApp.launch_instance(kernel_class=GccKernel)
