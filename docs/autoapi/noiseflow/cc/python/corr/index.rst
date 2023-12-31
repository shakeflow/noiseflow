:py:mod:`noiseflow.cc.python.corr`
==================================

.. py:module:: noiseflow.cc.python.corr


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   noiseflow.cc.python.corr.CorrClass_python



Functions
~~~~~~~~~

.. autoapisummary::

   noiseflow.cc.python.corr.coherency
   noiseflow.cc.python.corr.deconv
   noiseflow.cc.python.corr.xcorr



.. py:class:: CorrClass_python(rfft_data, dt, corr_method, corr_pair, maxlag, smoothspect_N, flag, jobs)

   Bases: :py:obj:`object`

   .. py:method:: corr(source_data, receiver_data)


   .. py:method:: cut_maxlag(corr_data)


   .. py:method:: irfft(rfft_corr_data)


   .. py:method:: process_chunk(chunk_start, chunk_end)


   .. py:method:: run()



.. py:function:: coherency(source_data, receiver_data, smoothspect_N)


.. py:function:: deconv(source_data, receiver_data, smoothspect_N)


.. py:function:: xcorr(source_data, receiver_data)


