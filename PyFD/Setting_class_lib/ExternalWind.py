import PyFD.FD as FD


class ExternalWind():

    use_outer_airflow = False
    use_outer_flow_contamination = False
    use_outer_flow_other_density_1 = False
    use_outer_flow_other_density_2 = False
    use_outer_flow_other_density_3 = False
    use_outer_flow_drag = False

    outer_airflow_set_type = 0
    outer_airflow_type = 0
    outer_airflow_dir_type = 0
    outer_airflow_dir = 0
    outer_airflow_manual_dir = 0
    outer_airflow_speed = 0
    outer_airflow_height = 10
    outer_airflow_temperature = 25
    outer_airflow_humidity = 60

    outer_flow_contamination = 0
    outer_flow_other_density_1 = 0
    outer_flow_other_density_2 = 0
    outer_flow_other_density_3 = 0

    def get_command_string(*argu):

        command_string = []

        if ExternalWind.use_outer_airflow:
            command_string.append("plugin analyzeplug setraw useouterairflow true");
            command_string.append("plugin analyzeplug setraw outerairflowtype " +
                                  str(ExternalWind.outer_airflow_type));
            command_string.append("plugin analyzeplug setraw outerairflowdirtype " +
                                  str(ExternalWind.outer_airflow_dir_type))
            command_string.append("plugin analyzeplug setraw outerairflowdir " +
                                  str(ExternalWind.outer_airflow_dir))
            command_string.append("plugin analyzeplug setraw outerairflowmanualdir " +
                                  str(ExternalWind.outer_airflow_manual_dir))
            command_string.append("plugin analyzeplug setraw outerairflowspeed " +
                                  str(ExternalWind.outer_airflow_speed))
            command_string.append("plugin analyzeplug setraw outerairflowheight " +
                                  str(ExternalWind.outer_airflow_height))
            command_string.append("plugin analyzeplug setraw outerairflowtemperature " +
                                  str(ExternalWind.outer_airflow_temperature))
            command_string.append("plugin analyzeplug setraw outerairflowhumidity " +
                                  str(ExternalWind.outer_airflow_humidity))
        else:
            command_string.append("plugin analyzeplug setraw useouterairflow false")

        if ExternalWind.use_outer_flow_contamination:
            command_string.append("plugin analyzeplug setraw useouterflowcontamination true")
            command_string.append("plugin analyzeplug setraw outerflowcontamination " +
                                  str(ExternalWind.outer_flow_contamination))
        else:
            command_string.append("plugin analyzeplug setraw useouterflowcontamination false")

        if ExternalWind.use_outer_flow_other_density_1:
            command_string.append("plugin analyzeplug setraw useouterflowotherdensity1 true")
            command_string.append("plugin analyzeplug setraw outerflowotherdensity1 " +
                                  str(ExternalWind.outer_flow_other_density_1))
        else:
            command_string.append("plugin analyzeplug setraw useouterflowotherdensity1 false")

        if ExternalWind.use_outer_flow_other_density_2:
            command_string.append("plugin analyzeplug setraw useouterflowotherdensity2 true");
            command_string.append("plugin analyzeplug setraw outerflowotherdensity2 " +
                                  str(ExternalWind.outer_flow_other_density_2))
        else:
            command_string.append("plugin analyzeplug setraw useouterflowotherdensity2 false")

        if ExternalWind.use_outer_flow_other_density_3:
            command_string.append("plugin analyzeplug setraw useouterflowotherdensity3 true")
            command_string.append("plugin analyzeplug setraw outerflowotherdensity3 " +
                                  str(ExternalWind.outer_flow_other_density_3))
        else:
            command_string.append("plugin analyzeplug setraw useouterflowotherdensity3 false")

        if ExternalWind.use_outer_flow_drag:
            command_string.append("plugin analyzeplug setraw useouterflowdrag true")
        else:
            command_string.append("plugin analyzeplug setraw useouterflowdrag false")

        return command_string

    def update_setting(*argu):
        for row in ExternalWind.get_command_string():
            FD.execute(row)

    def convert_wind_dir(wind_dir, manual=True):

        wind_dir = wind_dir%360

        if manual:
            return (360-wind_dir-90)%360
        else:
            return int(round(wind_dir/22.5, 0) + 1)