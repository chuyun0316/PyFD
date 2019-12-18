import PyFD.FD as FD


class CsvOutput():

    analysis_type = "fwd"

    output_object_indices = []
    output_group = "atarget"
    target_indices = []

    circle_indices = []

    output_file_path = ""
    output_type = "ave"
    panel_dir = "plus"
    output_separation = "none"

    def revise_analysis_type(*argu):
        if type(CsvOutput.analysis_type) is not str:
            try:
                anal_t = int(CsvOutput.analysis_type)
                return ["fwd", "opt"][anal_t]
            except:
                return "ERROR"
        else:
            anal_t = CsvOutput.analysis_type.lower()
            if anal_t == "fwd" or anal_t == "opt":
                return anal_t
            else: return "ERROR"

    def revise_output_group_name(*argu):
        return None

    def revise_output_group_index(*argu):
        return None


    def get_command_string(*argu):

        command_string = []



        return command_string

    def update_setting(*argu):
        for row in CsvOutput.get_command_string():
            FD.execute(row)