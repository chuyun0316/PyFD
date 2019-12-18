from PyFD import FD
from datetime import datetime

# log = ""
# counter = 1
# start_time = None
# end_time = None
#
#
# def pre_get_time():
#
#     global log
#     global counter
#     global start_time
#     global end_time
#
#     start_time = datetime.now()
#     log += "Iteration {} starts at {}\r\n".format(counter, start_time)
#
#
# def post_get_time():
#
#     global log
#     global counter
#     global start_time
#     global end_time
#
#     end_time = datetime.now()
#     log += "Iteration {} ends at {}\r\n".format(counter, end_time)
#     log += "Iteration {} spends {}\r\n".format(counter, end_time-start_time)
#     counter += 1
#
#     return counter <=5
#
#
# FD.preprocess = pre_get_time
# FD.postprocess = post_get_time
#
# FD.loop_start()
#
# print(log)

FD.ExternalWind.use_outer_airflow = True
FD.ExternalWind.outer_airflow_dir_type = 1
FD.ExternalWind.outer_airflow_manual_dir = FD.ExternalWind.convert_wind_dir(28, True)
FD.ExternalWind.update_setting()

