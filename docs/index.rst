.. python-lfu documentation master file, created by
   sphinx-quickstart on Thu Oct 15 11:02:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===========
Python-LFU
===========

.. currentmodule:: lfu_cache

Simplest usage

.. code-block:: python

    from lfu_cache import LFUCache
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3) # will evict 2
    cache.get(2) # raise KeyError

Algorithm can be read at this `research paper <http://dhruvbird.com/lfu.pdf>`_.
The implementation is exactly same where the cache object wraps FrequencyList
linked list whose elements are FrequencyItem. FrequencyItem has an attribute
frequency. FrequencyItem then wraps a NodeList double linked list with NodeItem
as elements of it. NodeItem wraps up the actual key/value provided by
application.


API Documentation
=================

This documentation is automatically generated from Python-LFU source code.

.. module:: lfu_cache

.. autoclass:: LFUCache
   :members: get, put


.. autoclass:: Element
   :members: nextelement, prevelement


.. autoclass:: DLList
   :members:


.. autoexception:: OtherListElement
