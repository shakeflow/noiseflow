:py:mod:`noiseflow.config.rfftdata`
===================================

.. py:module:: noiseflow.config.rfftdata


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   noiseflow.config.rfftdata.RFFTData_Class




.. py:class:: RFFTData_Class(rfft_data, dt, cc_len, cc_step, time_norm, clip_std, smooth_N, freq_norm, freqmin, freqmax, whiten_npad, smoothspect_N, flag, flag_gap, threads, jobs, py)

   Bases: :py:obj:`object`

   .. py:method:: save(save_path, format='npz', compression=False, h5_compression_format='gzip', h5_compression_opts=3)


   .. py:method:: spectrogram(channel_indx=0, win_indx=0, raw_data=None, dbscale=False, log=True, figsize=(10, 4), save=False, save_path=None, dpi=100)



