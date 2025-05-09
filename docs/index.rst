.. DV Flow LibPSS documentation master file, created by
   sphinx-quickstart on Thu May  8 22:38:09 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##############
DV Flow LibPSS
##############

The DV Flow PSS library provides tasks and types for working with Accellera 
Portable Stimulus Specification (PSS) models. 

.. contents::
    :depth: 2

Lib
===
The `Lib` task compiles PSS source into a pre-compiled library. If the 
specific PSS tool does not support pre-compiled libraries, the PSS 
sources will be output by the task.

Example
-------

Consumes
-------- 

* pssSource

Produces
-------- 

* pssLib

Parameters
----------

GenActorSV
==========
The `GenActorSV` task generates SystemVerilog code that is specific
to a given component+action scenario.

Example
-------

Consumes
-------- 

* pssSource
* pssLib

Produces
-------- 

* systemVerilogSource

Parameters
----------

* **root_action** - Specifies the root action of the scenario

GenModelSV
==========
The `GenModelSV` task generates SystemVerilog code that is common
across all scenarios of a given PSS component hierarchy.

Example
-------

Consumes
-------- 

* pssSource

Produces
-------- 

* systemVerilogSource

Parameters
----------

RuntimeSV
=========
The `RuntimeSV` task provides core SystemVerilog runtime sources that
are independent of a specific PSS model.

The `GenModelSV` task generates SystemVerilog code that is common
across all scenarios of a given PSS component hierarchy.

Example
-------

Consumes
-------- 


Produces
-------- 

* systemVerilogSource

Parameters
----------

Tool Support
============

Tasks that support specific PSS tools are implemented in tool-specific packages.
The tasks defined in these packages implement the same interface as the generic
tasks. For example, the full name of the `Zuspec` GenModelSV task is
`pss.zsp.GenModelSV`.

* **psp** - Cadence Perspec
* **zsp** - Zuspec

.. node::
    All trademarks are the property of their respective owners.

