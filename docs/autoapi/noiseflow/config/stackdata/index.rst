:py:mod:`noiseflow.config.stackdata`
====================================

.. py:module:: noiseflow.config.stackdata


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   noiseflow.config.stackdata.StackData_Class




.. py:class:: StackData_Class(stack_data, stack_ngood, dt, stack_method, par, stack_all, stack_len, stack_step, pick, median_high, median_low, flag, flag_gap, threads, jobs, py)

   Bases: :py:obj:`object`

   .. py:method:: plot(pair_indx=0, t_min=UTCDateTime('1970-01-01T00:00:00.0'), stack_len=1, stack_step=0, cc_len=None, cc_step=None, win_start=None, win_end=None, lag_start=None, lag_end=None, amp_normalize=True, amp_scale=1, filter=False, f1=None, f2=None, corners=4, zerophase=True, win_interval=None, mode='waveform', cmap='seismic', linewidth=0.8, yticklabel_num=5, figsize=(10, 6), ngood_label=False, save=False, save_path=None, dpi=300)


   .. py:method:: plot_moveout(corr_pair, pair_dist, source_indx=None, receiver_indx=None, dist_start=None, dist_end=None, amp_scale=1, amp_normalize=True, win_num=0, lag_start=None, lag_end=None, filter=False, f1=None, f2=None, corners=4, zerophase=True, dist_interval=None, mode='waveform', cmap='seismic', linewidth=0.8, yticklabel_num=10, figsize=(10, 6), dist_unit='m', velocity=[], save=False, save_path=None, dpi=100)


   .. py:method:: plot_moveout_all(corr_pair, pair_dist, dist_start=None, dist_end=None, amp_scale=1, amp_normalize=True, win_num=0, lag_start=None, lag_end=None, filter=False, f1=None, f2=None, corners=4, zerophase=True, dist_interval=None, mode='waveform', cmap='seismic', linewidth=0.8, yticklabel_num=10, figsize=(10, 6), dist_unit='m', velocity=[], save=False, save_path=None, dpi=30)


   .. py:method:: save(save_path, format='npz', compression=False, h5_compression_format='gzip', h5_compression_opts=3)



